from abc import ABC, abstractmethod
from ehir.mod import EHIR_Module


class EHIR_AbstractBuilder(ABC):
    @abstractmethod
    def build_imports(self):
        raise NotImplementedError
    
    @abstractmethod
    def build_structure_declarations(self):
        raise NotImplementedError
    
    @abstractmethod
    def build_structure_definitions(self):
        raise NotImplementedError
    
    @abstractmethod
    def build_function_declarations(self):
        raise NotImplementedError

    @abstractmethod
    def build_function_definitions(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_raw_modulue(self) -> EHIR_Module:
        raise NotImplementedError
