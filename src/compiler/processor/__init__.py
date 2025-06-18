from ehir.processor import EHIR_AbstractProcessor
from ..builder import Builder
from ehir.mod import EHIR_Module
from pathlib import Path


class Processor(EHIR_AbstractProcessor):
    def parse_file(self, filepath: Path) -> Builder:
        print(filepath)
        builder = Builder(filepath)
        return builder

    def on_dump_unresolved_ehir(self, module: EHIR_Module):
        raise NotImplementedError

    def on_dump_resolved_ehir(self, module: EHIR_Module):
        raise NotImplementedError
