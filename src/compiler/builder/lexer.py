from pathlib import Path
from dataclasses import dataclass

@dataclass
class Token:
    pass

@dataclass
class T_Sector(Token):
    name: str


@dataclass
class T_Identifier(Token):
    literal: str

@dataclass
class T_Keyword_imp(T_Identifier):
    pass

#

class Lexer:
    consumed  : int = 0
    program   : str = "" 
    
    def tokenize(self, path: Path) -> list[Token]:
        with path.open("r") as file:
            self.program = file.read()
        
        tokens = []
        
        while self.consumed < len(self.program):
            current_char = self._get_current_char()
            
            if current_char == "$":
                tokens.append(self._consume_sector())
                continue
            
            if current_char == " ":
                self._consume()
                continue
            
            if current_char == ";":
                while self._get_current_char() not in ("", "\n"):
                    self._consume()
                self._safe_consume("\n")
                continue
            
            if current_char == "\n":
                self._consume()
                continue
            
            if current_char == "":
                break
            
            if current_char.isalpha():
                tokens.append(self._consume_alpha())
                continue

            err = f"Unexpected char <{current_char}>"
            raise RuntimeError(err)

        return tokens
    
    #
    def _consume_alpha(self) -> T_Identifier:
        literal = self.__consume_identifier()
        
        if literal == "imp":
            return T_Keyword_imp(literal)
        
        return T_Identifier(literal)

    def _consume_sector(self) -> T_Sector:
        self._safe_consume("$")
        sector_name = self.__consume_identifier()
        return T_Sector(name=sector_name)
    
    def __consume_identifier(self) -> str:
        result = ""
        
        current_char = self._get_current_char()
        while current_char.isalpha() or current_char == "_":
            current_char = self._consume()
            
            if current_char in ("", "\n", " ", ","):
                break
            
            result += current_char
            
        return result

    #
    
    def _get_current_char(self) -> str:
        if self.consumed < len(self.program):
            return self.program[self.consumed]
        return ""

    def _get_next_char(self) -> str:
        if self.consumed + 1 < len(self.program):
            return self.program[self.consumed + 1]
        return ""

    def _safe_long_consume(self, expected_string: str) -> str:
        for char in expected_string:
            self._safe_consume(char)
        return expected_string
    
    def _safe_consume(self, char: str) -> str:
        if self._get_current_char() == char:
            return self._consume()

        err = f"Expected char <{char}> but got {self._get_current_char()}"
        raise RuntimeError(err)

    def _consume(self) -> str:
        result = self._get_current_char()
        self.consumed += 1
        return result
