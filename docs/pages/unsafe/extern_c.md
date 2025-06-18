# Extern libc Attribute

Аттрибут, указывающий компилятору, что отмеченная функция берётся из libc (Стандартная библиотека C)

```fn
#[from_libc, unsafe]
pub fn malloc(usize size) -> i8*
```

