from ehir.builder import EHIR_AbstractBuilder
from ehir.mod import EHIR_Module, EHIR_Header
from pathlib import Path
from .lexer import Lexer
from .parser import Parser


class Builder(EHIR_AbstractBuilder):
    def __init__(self, filepath: Path):
        self._parser = Parser(Lexer().tokenize(filepath))

        self._header = EHIR_Header.default()
        self._module = EHIR_Module(
            name   = filepath.name,
            path   = filepath,
            header = self._header,

            structure_decls = {},
            structure_defs  = {},
            function_decls  = {},
            function_defs   = {},
        )
    
    def build_imports(self):
        imports = self._parser.parse_imports()
        self._header.imports += imports
    
    def build_structure_declarations(self):
        raise NotImplementedError
    
    def build_structure_definitions(self):
        raise NotImplementedError
    
    def build_function_declarations(self):
        raise NotImplementedError

    def build_function_definitions(self):
        raise NotImplementedError

    def get_raw_modulue(self) -> EHIR_Module:
        return self._module

