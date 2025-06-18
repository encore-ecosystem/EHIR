# Sectors

Любая инструкции в EHIR должны быть распределены строго по следующим секциям:

- imports
- sdecls
- sdef
- fdecl
- fdef

`Header` в EHIR - все публичные символы во всех секциях, кроме секции fdef.

`Module` в EHIR - `Header` + приватные символы + секция fdef.

Таким образом, структура программы на EHIR выглядит так:

```ehir
$import
<import instructions>

$sdecl
<structure declaration instructions>

$sdef
<structure definition instructions>

$fdecl
<function declaration instructions>

$fdef
<function definition instructions>
```
