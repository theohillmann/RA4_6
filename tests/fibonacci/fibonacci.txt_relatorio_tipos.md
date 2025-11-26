# Relatório de Tipos Inferidos

**Total de linhas analisadas:** 96

**Data de geração:** 2025-11-26 02:40:05


---


## Tabela de Tipos por Linha


| Linha | Contexto | Tipo Inferido | Notação Posfixa |
|-------|----------|---------------|-----------------|
| 1 | `( int mem_store )` | 🔢 `int` | `INT(0) STORE(A)` |
| 2 | `( memid )` | 🔢 `int` | `REF(A)` |
| 3 | `( int mem_store ) #2` | 🔢 `int` | `INT(1) STORE(A)` |
| 4 | `( memid ) #2` | 🔢 `int` | `REF(A)` |
| 5 | `( ( int res ) mem_store )` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 6 | `( ( int res ) mem_store ) #2` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 7 | `( ( memid memid + ) mem_store )` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 8 | `( memid ) #3` | 🔢 `int` | `REF(A)` |
| 9 | `( ( int res ) mem_store ) #3` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 10 | `( ( int res ) mem_store ) #4` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 11 | `( ( memid memid + ) mem_store ) #2` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 12 | `( memid ) #4` | 🔢 `int` | `REF(A)` |
| 13 | `( ( int res ) mem_store ) #5` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 14 | `( ( int res ) mem_store ) #6` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 15 | `( ( memid memid + ) mem_store ) #3` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 16 | `( memid ) #5` | 🔢 `int` | `REF(A)` |
| 17 | `( ( int res ) mem_store ) #7` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 18 | `( ( int res ) mem_store ) #8` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 19 | `( ( memid memid + ) mem_store ) #4` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 20 | `( memid ) #6` | 🔢 `int` | `REF(A)` |
| 21 | `( ( int res ) mem_store ) #9` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 22 | `( ( int res ) mem_store ) #10` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 23 | `( ( memid memid + ) mem_store ) #5` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 24 | `( memid ) #7` | 🔢 `int` | `REF(A)` |
| 25 | `( ( int res ) mem_store ) #11` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 26 | `( ( int res ) mem_store ) #12` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 27 | `( ( memid memid + ) mem_store ) #6` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 28 | `( memid ) #8` | 🔢 `int` | `REF(A)` |
| 29 | `( ( int res ) mem_store ) #13` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 30 | `( ( int res ) mem_store ) #14` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 31 | `( ( memid memid + ) mem_store ) #7` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 32 | `( memid ) #9` | 🔢 `int` | `REF(A)` |
| 33 | `( ( int res ) mem_store ) #15` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 34 | `( ( int res ) mem_store ) #16` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 35 | `( ( memid memid + ) mem_store ) #8` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 36 | `( memid ) #10` | 🔢 `int` | `REF(A)` |
| 37 | `( ( int res ) mem_store ) #17` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 38 | `( ( int res ) mem_store ) #18` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 39 | `( ( memid memid + ) mem_store ) #9` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 40 | `( memid ) #11` | 🔢 `int` | `REF(A)` |
| 41 | `( ( int res ) mem_store ) #19` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 42 | `( ( int res ) mem_store ) #20` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 43 | `( ( memid memid + ) mem_store ) #10` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 44 | `( memid ) #12` | 🔢 `int` | `REF(A)` |
| 45 | `( ( int res ) mem_store ) #21` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 46 | `( ( int res ) mem_store ) #22` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 47 | `( ( memid memid + ) mem_store ) #11` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 48 | `( memid ) #13` | 🔢 `int` | `REF(A)` |
| 49 | `( ( int res ) mem_store ) #23` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 50 | `( ( int res ) mem_store ) #24` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 51 | `( ( memid memid + ) mem_store ) #12` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 52 | `( memid ) #14` | 🔢 `int` | `REF(A)` |
| 53 | `( ( int res ) mem_store ) #25` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 54 | `( ( int res ) mem_store ) #26` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 55 | `( ( memid memid + ) mem_store ) #13` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 56 | `( memid ) #15` | 🔢 `int` | `REF(A)` |
| 57 | `( ( int res ) mem_store ) #27` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 58 | `( ( int res ) mem_store ) #28` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 59 | `( ( memid memid + ) mem_store ) #14` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 60 | `( memid ) #16` | 🔢 `int` | `REF(A)` |
| 61 | `( ( int res ) mem_store ) #29` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 62 | `( ( int res ) mem_store ) #30` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 63 | `( ( memid memid + ) mem_store ) #15` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 64 | `( memid ) #17` | 🔢 `int` | `REF(A)` |
| 65 | `( ( int res ) mem_store ) #31` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 66 | `( ( int res ) mem_store ) #32` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 67 | `( ( memid memid + ) mem_store ) #16` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 68 | `( memid ) #18` | 🔢 `int` | `REF(A)` |
| 69 | `( ( int res ) mem_store ) #33` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 70 | `( ( int res ) mem_store ) #34` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 71 | `( ( memid memid + ) mem_store ) #17` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 72 | `( memid ) #19` | 🔢 `int` | `REF(A)` |
| 73 | `( ( int res ) mem_store ) #35` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 74 | `( ( int res ) mem_store ) #36` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 75 | `( ( memid memid + ) mem_store ) #18` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 76 | `( memid ) #20` | 🔢 `int` | `REF(A)` |
| 77 | `( ( int res ) mem_store ) #37` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 78 | `( ( int res ) mem_store ) #38` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 79 | `( ( memid memid + ) mem_store ) #19` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 80 | `( memid ) #21` | 🔢 `int` | `REF(A)` |
| 81 | `( ( int res ) mem_store ) #39` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 82 | `( ( int res ) mem_store ) #40` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 83 | `( ( memid memid + ) mem_store ) #20` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 84 | `( memid ) #22` | 🔢 `int` | `REF(A)` |
| 85 | `( ( int res ) mem_store ) #41` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 86 | `( ( int res ) mem_store ) #42` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 87 | `( ( memid memid + ) mem_store ) #21` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 88 | `( memid ) #23` | 🔢 `int` | `REF(A)` |
| 89 | `( ( int res ) mem_store ) #43` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 90 | `( ( int res ) mem_store ) #44` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 91 | `( ( memid memid + ) mem_store ) #22` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 92 | `( memid ) #24` | 🔢 `int` | `REF(A)` |
| 93 | `( ( int res ) mem_store ) #45` | 🔢 `int` | `INT(1) RES STORE(F1)` |
| 94 | `( ( int res ) mem_store ) #46` | 🔢 `int` | `INT(5) RES STORE(F3)` |
| 95 | `( ( memid memid + ) mem_store ) #23` | 🔢 `int` | `REF(F1) REF(F3) OP(+) STORE(A)` |
| 96 | `( memid ) #25` | 🔢 `int` | `REF(A)` |


---


## Estatísticas


### Distribuição de Tipos

- 🔢 `int`: 96 (100.0%)

### Taxa de Sucesso

**100.0%** das linhas foram tipadas com sucesso.
