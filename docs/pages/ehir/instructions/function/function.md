# Function

В EHIR для того, чтобы определить новую функцию, нужно в секции $func_decls вызвать команду определения функции (задать видимость функции, её имя, параметры и возвращаемый тип):

```ehir
fn %my_function(a: i32, b: i8) -> i1
```

Реализация уже определённой функции имеет следующий вид:

```ehir
impl my_function {
entry:
    ret 0
}
```

Ввиду того, что такая конструкция может оказаться неудобной по причине отсутствия перед глазами аргументов функции, возможен второй вариант этой инструкции:

```ehir
impl my_function(a: i32, b: i8) -> i1 {
entry:
    ret 0
}
```

Во втором случае будут совершены дополнительные проверки на имена и типы аргументов, чтобы они совпадали с определением функции.

---

Блоки `entry` является обязательным для каждой функции. В процессе разрешения сырого EHIR, резолвер дополнительно создаст новый блок `allocations`, в который вынесутся все инструкции динамической аллокации памяти (`caph`). Из этого следует:

- Функция не должна содержать блок с названием `allocations`.
- Функции, внутри которых происходит динамическое выделение памяти, должны быть простыми, так как после разрешения EHIR все `caph` будут вынесены в `allocations`. Таким образом, может происходить выделение памяти под неиспользуемые объекты. Хоть такая память и будет очищена, но все же лишний `caph` негативно отразится на производительности вашей программы.

Так же резолвер проставит все команды освобождения динамической памяти (`free`), которые не возвращаются из функции, в конце каждого `терминального блока` (блок, который заканчивается инструкцией `ret`).
