from .lexer import Token, T_Sector, T_Keyword_imp, T_Identifier
from ehir.instructions import EHIR_Instruction, EHIR_Instruction_imp
from enum import Enum, auto


class ParserSector(str, Enum):
    IMPORTS = auto()



class Parser:
    consumed : int = 0
    tokens   : list[Token]

    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current_sector : ParserSector | None = None
    
    def parse_imports(self) -> list[EHIR_Instruction_imp]:
        imports = []
        
        self.current_sector = self._safe_consume(T_Sector)
        if self.current_sector.name != "imports":
            err = f"Expected sector <imports> but got {self.current_sector}"
            raise RuntimeError(err)

        while not isinstance(self._get_current_token(), T_Sector):
            imports.append(self._parse_imports())

        return imports
    
    #
    
    def _parse_imports(self) -> EHIR_Instruction_imp:
        self._safe_consume(T_Keyword_imp)
        module = self._safe_consume(T_Identifier)
        symbol = self._safe_consume(T_Identifier)
        return EHIR_Instruction_imp(
            module_name = module.literal,
            symbol      = symbol.literal,
        )

    #
    
    def _get_current_token(self) -> Token:
        return self.tokens[self.consumed]

    def _safe_consume(self, token_type: type[Token]) -> Token:
        token = self._consume()
        if isinstance(token, token_type):
            return token
        
        err = f"Expected token {token_type} but got {token}"
        raise RuntimeError(err)
    
    def _consume(self) -> Token:
        self.consumed += 1
        return self.tokens[self.consumed - 1]
