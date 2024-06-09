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
- init_memory - записывает данные и команды в память перед началом исполнения
- latch_acc - запись в аккамулятор       
- latch_address_register - запись в регистр адресов
- latch_data_register - запись в регистр данных
- latch_memory - запись или чтение из памяти
- latch_alu_right - записсь в правый вход ALU
- latch_alu_left - запись в левый вход ALU
- getMUX       -     говорит, какие данные выводить MUX
- Z - флаг (если аккамулятор равен 0, то TRUE, инача False)

![image](https://github.com/DimaAmelchenkoG/AK/assets/144106912/da7b52f4-5e70-4447-a629-0a82d4e77426)



## ControlUnit
- Реализован в классе ControlUnit в файле machine.py
- Цикл симуляции осуществляется в метод execute.
- instruction_pointer - указатель на текущую исполняемую команду
  
![image](https://github.com/DimaAmelchenkoG/AK/assets/144106912/5eafdecd-7d8d-4074-b5ed-10f297606b85)


## Тестирование
Тестирование выполняется при помощи golden-тестов на базе Pytest Golden

Тестовое покрытие:
- hello_user_name - выделение памяти под строку и ее заполнение
- cat - ввод-вывод
- hello - вывод и работа со строками
- prob1 - алгоритм из варианта, вычисляет сумму всех чисел, кратных 3 и 5 до 1000

Пример запуска тестов:
```
PS C:\Users\mitya\PycharmProjects\AK> poetry run pytest . -v
========================================================================================================= test session starts =========================================================================================================
platform win32 -- Python 3.11.2, pytest-8.2.1, pluggy-1.5.0 -- C:\Users\mitya\AppData\Local\Programs\Python\Python311\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\mitya\PycharmProjects\AK
configfile: pyproject.toml
plugins: golden-0.2.2
collected 4 items

golden_test.py::test_translator_asm_and_machine[golden/cat.yml] PASSED                                                                                                                                                           [ 25%]
golden_test.py::test_translator_asm_and_machine[golden/hello.yml] PASSED                                                                                                                                                         [ 50%]
golden_test.py::test_translator_asm_and_machine[golden/hello_user_name.yml] PASSED                                                                                                                                               [ 75%]
golden_test.py::test_translator_asm_and_machine[golden/prob1.yml] PASSED                                                                                                                                                         [100%]

========================================================================================================== 4 passed in 1.96s ========================================================================================================== 
```

## CI

```text
| ФИО                          | алг             | LoC       | code байт   | code инстр. | инстр. | такт.   | вариант                                                                          |
| Амельченко Дмитрий Сергеевич | cat             | 25        | -           | 18          | 44     | 108     | asm | acc | neum | hw | instr | struct | stream | mem | cstr | prob1 | cache     |
| Амельченко Дмитрий Сергеевич | hello           | 11        | -           | 7           | 58     | 160     | asm | acc | neum | hw | instr | struct | stream | mem | cstr | prob1 | cache     |
| Амельченко Дмитрий Сергеевич | hello_user_name | 39        | -           | 30          | 174    | 468     | asm | acc | neum | hw | instr | struct | stream | mem | cstr | prob1 | cache     |
| Амельченко Дмитрий Сергеевич | cat             | 24        | -           | 19          | 11940  | 45092   | asm | acc | neum | hw | instr | struct | stream | mem | cstr | prob1 | cache     |
```


