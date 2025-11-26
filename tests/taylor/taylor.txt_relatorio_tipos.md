# Relatório de Tipos Inferidos

**Total de linhas analisadas:** 24

**Data de geração:** 2025-11-26 02:40:12


---


## Tabela de Tipos por Linha


| Linha | Contexto | Tipo Inferido | Notação Posfixa |
|-------|----------|---------------|-----------------|
| 1 | `( real mem_store )` | 🔢 `real` | `REAL(1.0) STORE(RESULT)` |
| 2 | `( real mem_store ) #2` | 🔢 `real` | `REAL(0.5) STORE(X)` |
| 3 | `( ( real int ^ ) mem_store )` | 🔢 `real` | `REAL(0.5) INT(2) OP(^) STORE(POT1)` |
| 4 | `( int mem_store )` | 🔢 `int` | `INT(2) STORE(N1)` |
| 5 | `( int mem_store ) #2` | 🔢 `int` | `INT(1) STORE(I1)` |
| 6 | `( int mem_store ) #3` | 🔢 `int` | `INT(1) STORE(F1)` |
| 7 | `( ( memid memid <= ) ( ( memid memid * ) mem_store ) ( ( memid int + ) mem_store ) for )` | ⚪ `void` | `REF(I1) REF(N1) OP(<=) REF(F1) REF(I1) OP(*) ST...` |
| 8 | `( ( memid memid \| ) mem_store )` | 🔢 `real` | `REF(POT1) REF(F1) OP(|) STORE(FRA1)` |
| 9 | `( ( memid memid - ) mem_store )` | 🔢 `real` | `REF(RESULT) REF(FRA1) OP(-) STORE(RESULT)` |
| 10 | `( ( real int ^ ) mem_store ) #2` | 🔢 `real` | `REAL(0.5) INT(4) OP(^) STORE(POT2)` |
| 11 | `( int mem_store ) #4` | 🔢 `int` | `INT(4) STORE(N2)` |
| 12 | `( int mem_store ) #5` | 🔢 `int` | `INT(1) STORE(I2)` |
| 13 | `( int mem_store ) #6` | 🔢 `int` | `INT(1) STORE(F2)` |
| 14 | `( ( memid memid <= ) ( ( memid memid * ) mem_store ) ( ( memid int + ) mem_store ) for ) #2` | ⚪ `void` | `REF(I2) REF(N2) OP(<=) REF(F2) REF(I2) OP(*) ST...` |
| 15 | `( ( memid memid \| ) mem_store ) #2` | 🔢 `real` | `REF(POT2) REF(F2) OP(|) STORE(FRA2)` |
| 16 | `( ( memid memid + ) mem_store )` | 🔢 `real` | `REF(RESULT) REF(FRA2) OP(+) STORE(RESULT)` |
| 17 | `( ( real int ^ ) mem_store ) #3` | 🔢 `real` | `REAL(0.5) INT(6) OP(^) STORE(POT3)` |
| 18 | `( int mem_store ) #7` | 🔢 `int` | `INT(6) STORE(N3)` |
| 19 | `( int mem_store ) #8` | 🔢 `int` | `INT(1) STORE(I3)` |
| 20 | `( int mem_store ) #9` | 🔢 `int` | `INT(1) STORE(F3)` |
| 21 | `( ( memid memid <= ) ( ( memid memid * ) mem_store ) ( ( memid int + ) mem_store ) for ) #3` | ⚪ `void` | `REF(I3) REF(N3) OP(<=) REF(F3) REF(I3) OP(*) ST...` |
| 22 | `( ( memid memid \| ) mem_store ) #3` | 🔢 `real` | `REF(POT2) REF(F3) OP(|) STORE(FRA3)` |
| 23 | `( ( memid memid - ) mem_store ) #2` | 🔢 `real` | `REF(RESULT) REF(FRA2) OP(-) STORE(RESULT)` |
| 24 | `( memid )` | 🔢 `real` | `REF(RESULT)` |


---


## Estatísticas


### Distribuição de Tipos

- 🔢 `real`: 12 (50.0%)
- 🔢 `int`: 9 (37.5%)
- ⚪ `void`: 3 (12.5%)

### Taxa de Sucesso

**100.0%** das linhas foram tipadas com sucesso.
