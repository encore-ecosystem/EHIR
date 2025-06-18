from ..aggregate import EHIR_StructureInitialization, EHIR_StructureDefinition, EHIR_StructureDeclaration

class EHIR_Structure_Integer(EHIR_StructureInitialization):
    def __init__(self, value: int, size: int):
        assert size > 0
        self.definition = EHIR_StructureDefinition(
            declaration = EHIR_StructureDeclaration(is_public=False, name=f"i{size}"),
            fields      = (),
        )
        self.args = (value, )
