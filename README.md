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

<arg>  -  <var_name>       |  &<var_name>         |  [0-9]+
          прямая адресация | косвенная адресация
```

|  синтаксис      | OPCODE        |    TICKS   |    DESCRIPTION   |
| ------------- | ------------- | ------------- | ------------- |
| ld  | LOAD  | 4  | AC = MEM(ADR)  |
| st  | ST  | 2  | MEM(ADR) = AC  |
| add  | ADD  |  6 | AC = AC + ARG  |
| sub  | SUB  | 6  | AC = AC - ARG  |
| mod  | MOD  | 6  | AC = AC % ARG  |
| inc  | INC  | 7  | MEM(ADR) = MEM(ADR) + 1 |
| jmp  | JMP  | 1  | JMP ARG  |
| jz  | JZ  | 1  | IF AC == 0: JMP ARG |
| jnz  | JNZ  | 1  | IF AC != 0: JMP ARG   |
| print  | PRINT  | -  | OUTPUT =  MEM(ADR)|
| read  | READ  | -  | MEM(ADR) = INPUT  |
| halt  | HALT  | 1  | STOP  |

## Организация памяти

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
1. 1
2. 2
3. 3
4. 4
5. 5

## Процессор
### DataPath
### ControlUnit

## Тесты
### Модульные тесты
### Интеграционные тесты

## CI



