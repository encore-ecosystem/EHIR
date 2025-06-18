from pathlib import Path
from ehir.processor import EHIR_AbstractProcessor
from ehir.mod import EHIR_Module


class EHIR_ProjectTree:
    def __init__(self, processor: EHIR_AbstractProcessor):
        self._processor = processor
        self._ptree : dict[str, tuple[EHIR_Module, list[EHIR_Module]]] = {}
        self._entry : EHIR_Module | None = None

    def build_from(self, entry_file_path: Path):
        self._ptree.clear()
        self._entry = self._add_node(entry_file_path)
    
    def _add_node(self, filepath: Path) -> EHIR_Module:
        builder = self._processor.parse_file(filepath)
        module = builder.get_raw_modulue()
        self._ptree[module.path] = (module, [])

        # 1: Add imports
        builder.build_imports()

        # 2: Add structures declaration
        builder.build_structure_declarations()
        for imp in module.header.imports:
            dep_path = module.path.parent / f"{imp.module_name}.enc"
            if dep_path in self._ptree:
                dep, _ = self._ptree[dep_path]
            else:
                dep = self._add_node(dep_path)

            if imp.symbol in dep.header.structure_decls:
                module.structure_decls[imp.symbol] = dep.header.structure_decls[imp.symbol]
                continue

        # 3: Add structures definitions
        builder.build_structure_definitions()
        ignored_imports = []
        while module.header.imports:
            imp = module.header.imports.pop(0)
            dep_path = module.path.parent / f"{imp.module_name}.enc"
            dep, _ = self._ptree[dep_path]
            if imp.symbol in dep.header.structure_defs:
                module.structure_defs[imp.symbol] = dep.header.structure_defs[imp.symbol]
                continue
            ignored_imports.append(imp)
        module.header.imports = ignored_imports
        
        # 4. Add function declarations
        builder.build_function_declarations()
        ignored_imports = []
        while module.header.imports:
            imp = module.header.imports.pop(0)
            dep_path = module.path.parent / f"{imp.module_name}.enc"
            dep, _ = self._ptree[dep_path]
            if imp.symbol in dep.header.function_decls:
                module.function_decls[imp.symbol] = dep.header.function_decls[imp.symbol]
                continue
            ignored_imports.append(imp)
        
        if len(ignored_imports) != 0:
            err = "Unkown symbols:\n"
            for imp in ignored_imports:
                err += f"\t{imp}\n"
            raise RuntimeError(err)

        self._check_function_args(module)
        
        # 5. Add function definitions
        builder.build_function_definitions()
        
        # 6. Dump unresolved EHIR
        self._processor.on_dump_unresolved_ehir(module)

        # 7: Finalize imports
        module.resolve()
        
        # 8. Dump resolved EHIR
        self._processor.on_dump_resolved_ehir(module)
        
        return module
    
    def _check_function_args(self, module: EHIR_Module):
        for function in module.function_decls.values():
            for arg in function.declaration.params:
                arg_type = arg.points_to.name
                if arg_type not in module.structure_decls and arg_type not in module.header.structure_decls:
                    err = f"Unknown argument type {arg_type} of {arg.name} in function {function.declaration.name}. "
                    err += f"Possible solution is import structure {arg_type}."
                    raise RuntimeError(err)
