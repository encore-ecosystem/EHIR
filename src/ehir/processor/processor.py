from abc import ABC, abstractmethod
from pathlib import Path
from ..builder import EHIR_AbstractBuilder
from ..mod import EHIR_Module

class EHIR_AbstractProcessor(ABC):
    @abstractmethod
    def parse_file(self, filepath: Path) -> EHIR_AbstractBuilder:
        raise NotImplementedError

    @abstractmethod
    def on_dump_unresolved_ehir(self, module: EHIR_Module):
        raise NotImplementedError

    @abstractmethod
    def on_dump_resolved_ehir(self, module: EHIR_Module):
        raise NotImplementedError
