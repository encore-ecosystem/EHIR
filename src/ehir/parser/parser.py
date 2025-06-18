from ..processor import EHIR_AbstractProcessor
from pathlib import Path
from ehir.mod import EHIR_Module


class EHIR_Parser(EHIR_AbstractProcessor):
    def __init__(self):
        pass
    
    def parse_file(self, filepath: Path) -> EHIR_Module:
        raise NotImplementedError
