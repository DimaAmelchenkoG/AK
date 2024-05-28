# АК
# Лаборатнорная работа №3 
# Амельченко Дмитрий P3232

- Преподаватели, Пенской Александр Владимирович.
- asm | acc | neum | hw | instr | struct | stream | mem | cstr | prob1 | cache
- Упрощенный вариант

## Язык программирования


```
.data   -   секция данных (переменные)
  x: 0
.code   -   секция кода (инструкции)
  ld x
  halt 
```

```
.data  
  <var_name>: <var_value>
.code  
  <instr> | 
  <instr> <arg>| 
  <label>: | 
```

```
<var_name> - [a-zA-Z]+
<var_value> - [0-9]+  | "[a-zA-Z]+"
<label> - [a-zA-Z]+

<arg>  -  <var_name>       |  &<var_name>         |  [0-9]+  |  "in" | "out" |
          прямая адресация | косвенная адресация
```

|  синтаксис      | OPCODE        |    TICKS   |    DESCRIPTION   |
| ------------- | ------------- | ------------- | ------------- |
| ld  | LOAD  | 4  | AC = MEM(ADR)  |
| st  | ST  | 2  | MEM(ADR) = AC  |
| add  | ADD  |  6 | AC = AC + ARG  |
| sub  | SUB  | 6  | AC = AC - ARG  |
| sub  | MUL  | 6  | AC = AC * ARG  |
| sub  | DIB  | 6  | AC = AC / ARG  |
| mod  | MOD  | 6  | AC = AC % ARG  |
| inc  | INC  | 7  | MEM(ADR) = MEM(ADR) + 1 |
| jmp  | JMP  | 1  | JMP LABEL  |
| jz  | JZ  | 1  | IF AC == 0: JMP LABEL |
| jnz  | JNZ  | 1  | IF AC != 0: JMP LABEL   |
| halt  | HALT  | 1  | STOP  |

## Организация памяти
- архитектура фон неймана
- в 0-евой ячейке лежит адрес первой инструкции
- при обращение к 1-ой и 2-ой ячейке мы работает с внешними устройствами (in и out)
- после всех интрукций, у нас идут ячейки для работы с вводом данных
|  адрес      | содержимое        | 
| ------------- | ------------- | 
| 0  | номер первой инструкции (k)  |
| 1  | 0  | 
| 2  | 0  |  
| 3  | 0  | 
| 4  | data  |
| ...  | ...  | 
| ...  | ...  | 
| k-1  | data  |
| k  | instr  | 
| ...  | ...  | 
| ...  | ...  | 
| n-1  | instr  | 
| n  | 0  | 
| n+1  | data for input  | 
| ...  | ...  | 

## Транслятор
- транслятор реализован в файле translator.py
- Интерфейс командной строки translator.py <input_file> <target_file>"
### Работа транслятора
1. Транслятор проходится по файлу, который мы ему подаем и первым делом находит все переменные
2. Транслятор находит все метки
3. Транслятор считывает инструкции, заменяя имена меток, на их номер по счету

# Процессор
- Интерфейс командной строки: machine.py <machine_code_file> <input_file>
## DataPath
- Реализован в классе DataPath в файле machine.py
## Сигналы:
- latch_acc       
- latch_address_register
- latch_data_register
- latch_memory
- latch_alu_right
- latch_alu_left
- getMUX       -     говорит, какие данные выводить MUX

### Z - флаг (если аккамулятор равен 0, то TRUE, инача False)

![image](https://github.com/DimaAmelchenkoG/AK/assets/144106912/6ec4bc51-15ce-4485-aa49-d37f97eed2cd)

## ControlUnit
- Реализован в классе ControlUnit в файле machine.py
- Цикл симуляции осуществляется в метод execute.
  
![image](https://github.com/DimaAmelchenkoG/AK/assets/144106912/5eafdecd-7d8d-4074-b5ed-10f297606b85)


## Тесты
### Модульные тесты
### Интеграционные тесты

## CI

```text
| ФИО                            | алг   | LoC | code байт | code инстр. | инстр. | такт. | вариант |
| Амельченко Дмитрий Сергеевич | hello | ... | -         | ...         | ...    | ...   | ...     |
| Амельченко Дмитрий Сергеевич | cat   | 1   | -         | 6           | 15     | 28    | ...     |
| Амельченко Дмитрий Сергеевич | cat   | 1   | -         | 6           | 15     | 28    | ...     |
| Амельченко Дмитрий Сергеевич | cat   | 1   | -         | 6           | 15     | 28    | ...     |
```


