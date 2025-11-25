# Relatório de Tipos Inferidos

**Total de linhas analisadas:** 67

**Data de geração:** 2025-11-24 21:24:46


---


## Tabela de Tipos por Linha


| Linha | Contexto | Tipo Inferido | Notação Posfixa |
|-------|----------|---------------|-----------------|
| 1 | `( int mem_store )` | 🔢 `int` | `INT(1) STORE(A)` |
| 2 | `( int mem_store ) #2` | 🔢 `int` | `INT(2) STORE(B)` |
| 3 | `( real mem_store )` | 🔢 `real` | `REAL(3.4) STORE(C)` |
| 4 | `( int res )` | 🔢 `real` | `INT(1) RES` |
| 5 | `( int res ) #2` | 🔢 `real` | `INT(2) RES` |
| 6 | `( memid )` | 🔢 `int` | `REF(A)` |
| 7 | `( memid ) #2` | 🔢 `int` | `REF(B)` |
| 8 | `( int int + )` | 🔢 `int` | `INT(1) INT(2) OP(+)` |
| 9 | `( memid int + )` | 🔢 `int` | `REF(A) INT(2) OP(+)` |
| 10 | `( int memid + )` | 🔢 `int` | `INT(1) REF(B) OP(+)` |
| 11 | `( memid memid + )` | 🔢 `int` | `REF(A) REF(B) OP(+)` |
| 12 | `( int int - )` | 🔢 `int` | `INT(1) INT(2) OP(-)` |
| 13 | `( memid int - )` | 🔢 `int` | `REF(A) INT(2) OP(-)` |
| 14 | `( int memid - )` | 🔢 `int` | `INT(1) REF(B) OP(-)` |
| 15 | `( memid memid - )` | 🔢 `int` | `REF(A) REF(B) OP(-)` |
| 16 | `( int int * )` | 🔢 `int` | `INT(1) INT(2) OP(*)` |
| 17 | `( memid int * )` | 🔢 `int` | `REF(A) INT(2) OP(*)` |
| 18 | `( int memid * )` | 🔢 `int` | `INT(1) REF(B) OP(*)` |
| 19 | `( memid memid * )` | 🔢 `int` | `REF(A) REF(B) OP(*)` |
| 20 | `( int int / )` | 🔢 `int` | `INT(1) INT(2) OP(/)` |
| 21 | `( memid int / )` | 🔢 `int` | `REF(A) INT(2) OP(/)` |
| 22 | `( int memid / )` | 🔢 `int` | `INT(1) REF(B) OP(/)` |
| 23 | `( memid memid / )` | 🔢 `int` | `REF(A) REF(B) OP(/)` |
| 24 | `( int int \| )` | 🔢 `real` | `INT(1) INT(2) OP(|)` |
| 25 | `( memid int \| )` | 🔢 `real` | `REF(A) INT(2) OP(|)` |
| 26 | `( int memid \| )` | 🔢 `real` | `INT(1) REF(B) OP(|)` |
| 27 | `( memid memid \| )` | 🔢 `real` | `REF(A) REF(B) OP(|)` |
| 28 | `( int int % )` | 🔢 `int` | `INT(1) INT(2) OP(%)` |
| 29 | `( memid int % )` | 🔢 `int` | `REF(A) INT(2) OP(%)` |
| 30 | `( int memid % )` | 🔢 `int` | `INT(1) REF(B) OP(%)` |
| 31 | `( memid memid % )` | 🔢 `int` | `REF(A) REF(B) OP(%)` |
| 32 | `( int int ^ )` | 🔢 `int` | `INT(1) INT(2) OP(^)` |
| 33 | `( memid int ^ )` | 🔢 `int` | `REF(A) INT(2) OP(^)` |
| 34 | `( int memid ^ )` | 🔢 `int` | `INT(1) REF(B) OP(^)` |
| 35 | `( memid memid ^ )` | 🔢 `int` | `REF(A) REF(B) OP(^)` |
| 36 | `( int int >= )` | ✅ `bool` | `INT(1) INT(2) OP(>=)` |
| 37 | `( memid int >= )` | ✅ `bool` | `REF(A) INT(2) OP(>=)` |
| 38 | `( int memid >= )` | ✅ `bool` | `INT(1) REF(B) OP(>=)` |
| 39 | `( memid memid >= )` | ✅ `bool` | `REF(A) REF(B) OP(>=)` |
| 40 | `( int int <= )` | ✅ `bool` | `INT(1) INT(2) OP(<=)` |
| 41 | `( memid int <= )` | ✅ `bool` | `REF(A) INT(2) OP(<=)` |
| 42 | `( int memid <= )` | ✅ `bool` | `INT(1) REF(B) OP(<=)` |
| 43 | `( memid memid <= )` | ✅ `bool` | `REF(A) REF(B) OP(<=)` |
| 44 | `( int int > )` | ✅ `bool` | `INT(1) INT(2) OP(>)` |
| 45 | `( memid int > )` | ✅ `bool` | `REF(A) INT(2) OP(>)` |
| 46 | `( int memid > )` | ✅ `bool` | `INT(1) REF(B) OP(>)` |
| 47 | `( memid memid > )` | ✅ `bool` | `REF(A) REF(B) OP(>)` |
| 48 | `( int int < )` | ✅ `bool` | `INT(1) INT(2) OP(<)` |
| 49 | `( memid int < )` | ✅ `bool` | `REF(A) INT(2) OP(<)` |
| 50 | `( int memid < )` | ✅ `bool` | `INT(1) REF(B) OP(<)` |
| 51 | `( memid memid < )` | ✅ `bool` | `REF(A) REF(B) OP(<)` |
| 52 | `( int int == )` | ✅ `bool` | `INT(1) INT(2) OP(==)` |
| 53 | `( memid int == )` | ✅ `bool` | `REF(A) INT(2) OP(==)` |
| 54 | `( int memid == )` | ✅ `bool` | `INT(1) REF(B) OP(==)` |
| 55 | `( memid memid == )` | ✅ `bool` | `REF(A) REF(B) OP(==)` |
| 56 | `( int int != )` | ✅ `bool` | `INT(1) INT(2) OP(!=)` |
| 57 | `( memid int != )` | ✅ `bool` | `REF(A) INT(2) OP(!=)` |
| 58 | `( int memid != )` | ✅ `bool` | `INT(1) REF(B) OP(!=)` |
| 59 | `( memid memid != )` | ✅ `bool` | `REF(A) REF(B) OP(!=)` |
| 60 | `( ( int int < ) ( memid ) while )` | ⚪ `void` | `INT(1) INT(2) OP(<) REF(A) WHILE` |
| 61 | `( ( memid int < ) ( memid ) while )` | ⚪ `void` | `REF(A) INT(2) OP(<) REF(B) WHILE` |
| 62 | `( ( int memid < ) ( int ) while )` | ⚪ `void` | `INT(1) REF(B) OP(<) INT(2) WHILE` |
| 63 | `( ( memid memid < ) ( memid ) while )` | ⚪ `void` | `REF(A) REF(B) OP(<) REF(A) WHILE` |
| 64 | `( ( int int > ) ( int ) ( int ) if )` | 🔢 `int` | `INT(1) INT(2) OP(>) INT(1) INT(2) IF` |
| 65 | `( ( memid int > ) ( memid ) ( int ) if )` | 🔢 `int` | `REF(A) INT(2) OP(>) REF(A) INT(2) IF` |
| 66 | `( ( int memid > ) ( int ) ( memid ) if )` | 🔢 `int` | `INT(1) REF(B) OP(>) INT(1) REF(B) IF` |
| 67 | `( ( memid memid > ) ( memid ) ( memid ) if )` | 🔢 `int` | `REF(A) REF(B) OP(>) REF(A) REF(B) IF` |


---


## Estatísticas


### Distribuição de Tipos

- 🔢 `int`: 32 (47.8%)
- ✅ `bool`: 24 (35.8%)
- 🔢 `real`: 7 (10.4%)
- ⚪ `void`: 4 (6.0%)

### Taxa de Sucesso

**100.0%** das linhas foram tipadas com sucesso.
