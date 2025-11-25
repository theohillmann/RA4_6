# Relatório de Tipos Inferidos

**Total de linhas analisadas:** 36

**Data de geração:** 2025-11-25 01:02:07


---


## Tabela de Tipos por Linha


| Linha | Contexto | Tipo Inferido | Notação Posfixa |
|-------|----------|---------------|-----------------|
| 1 | `( real mem_store )` | 🔢 `real` | `REAL(1.4) STORE(A)` |
| 2 | `( ( int int + ) mem_store )` | 🔢 `int` | `INT(1) INT(2) OP(+) STORE(A)` |
| 3 | `( memid )` | 🔢 `real` | `REF(A)` |
| 4 | `( ( int int - ) mem_store )` | 🔢 `int` | `INT(2) INT(1) OP(-) STORE(A)` |
| 5 | `( memid ) #2` | 🔢 `real` | `REF(A)` |
| 6 | `( ( int int * ) mem_store )` | 🔢 `int` | `INT(1) INT(2) OP(*) STORE(A)` |
| 7 | `( memid ) #3` | 🔢 `real` | `REF(A)` |
| 8 | `( ( int int \| ) mem_store )` | 🔢 `real` | `INT(13) INT(6) OP(|) STORE(A)` |
| 9 | `( memid ) #4` | 🔢 `real` | `REF(A)` |
| 10 | `( ( int int / ) mem_store )` | 🔢 `int` | `INT(1) INT(2) OP(/) STORE(A)` |
| 11 | `( memid ) #5` | 🔢 `real` | `REF(A)` |
| 12 | `( ( int int ^ ) mem_store )` | 🔢 `int` | `INT(1) INT(2) OP(^) STORE(A)` |
| 13 | `( memid ) #6` | 🔢 `real` | `REF(A)` |
| 14 | `( ( int int % ) mem_store )` | 🔢 `int` | `INT(1) INT(2) OP(%) STORE(A)` |
| 15 | `( memid ) #7` | 🔢 `real` | `REF(A)` |
| 16 | `( ( int res ) mem_store )` | 🔢 `real` | `INT(8) RES STORE(A)` |
| 17 | `( memid ) #8` | 🔢 `real` | `REF(A)` |
| 18 | `( ( int int > ) ( int mem_store ) ( int mem_store ) if )` | 🔢 `int` | `INT(2) INT(1) OP(>) INT(5) STORE(A) INT(6) STOR...` |
| 19 | `( memid ) #9` | 🔢 `real` | `REF(A)` |
| 20 | `( ( int int < ) ( int mem_store ) ( int mem_store ) if )` | 🔢 `int` | `INT(2) INT(1) OP(<) INT(5) STORE(A) INT(6) STOR...` |
| 21 | `( memid ) #10` | 🔢 `real` | `REF(A)` |
| 22 | `( ( int int >= ) ( int mem_store ) ( int mem_store ) if )` | 🔢 `int` | `INT(1) INT(1) OP(>=) INT(5) STORE(A) INT(6) STO...` |
| 23 | `( memid ) #11` | 🔢 `real` | `REF(A)` |
| 24 | `( ( int int <= ) ( int mem_store ) ( int mem_store ) if )` | 🔢 `int` | `INT(2) INT(2) OP(<=) INT(5) STORE(A) INT(6) STO...` |
| 25 | `( memid ) #12` | 🔢 `real` | `REF(A)` |
| 26 | `( ( int int == ) ( int mem_store ) ( int mem_store ) if )` | 🔢 `int` | `INT(2) INT(1) OP(==) INT(5) STORE(A) INT(6) STO...` |
| 27 | `( memid ) #13` | 🔢 `real` | `REF(A)` |
| 28 | `( ( int int == ) ( int mem_store ) ( int mem_store ) if ) #2` | 🔢 `int` | `INT(1) INT(1) OP(==) INT(5) STORE(A) INT(6) STO...` |
| 29 | `( memid ) #14` | 🔢 `real` | `REF(A)` |
| 30 | `( int mem_store )` | 🔢 `int` | `INT(1) STORE(A)` |
| 31 | `( ( memid int < ) ( ( memid int * ) mem_store ) while )` | ⚪ `void` | `REF(A) INT(5) OP(<) REF(A) INT(5) OP(*) STORE(A...` |
| 32 | `( memid ) #15` | 🔢 `real` | `REF(A)` |
| 33 | `( int mem_store ) #2` | 🔢 `int` | `INT(1) STORE(A)` |
| 34 | `( int mem_store ) #3` | 🔢 `int` | `INT(0) STORE(B)` |
| 35 | `( ( memid int < ) ( ( memid int + ) mem_store ) ( ( memid int + ) mem_store ) for )` | ⚪ `void` | `REF(A) INT(5) OP(<) REF(B) INT(5) OP(+) STORE(B...` |
| 36 | `( memid ) #16` | 🔢 `int` | `REF(B)` |


---


## Estatísticas


### Distribuição de Tipos

- 🔢 `real`: 18 (50.0%)
- 🔢 `int`: 16 (44.4%)
- ⚪ `void`: 2 (5.6%)

### Taxa de Sucesso

**100.0%** das linhas foram tipadas com sucesso.
