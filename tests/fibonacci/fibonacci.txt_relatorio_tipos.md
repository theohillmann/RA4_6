# Relatório de Tipos Inferidos

**Total de linhas analisadas:** 8

**Data de geração:** 2025-11-25 00:53:20


---


## Tabela de Tipos por Linha


| Linha | Contexto | Tipo Inferido | Notação Posfixa |
|-------|----------|---------------|-----------------|
| 1 | `( int mem_store )` | 🔢 `int` | `INT(0) STORE(A)` |
| 2 | `( int mem_store ) #2` | 🔢 `int` | `INT(1) STORE(B)` |
| 3 | `( int mem_store ) #3` | 🔢 `int` | `INT(1) STORE(I)` |
| 4 | `( ( memid int <= ) ( ( memid memid + ) mem_store ) while )` | ⚪ `void` | `REF(I) INT(5) OP(<=) REF(A) REF(B) OP(+) STORE(...` |
| 5 | `( ( int int <= ) ( ( memid mem_store ) mem_store ) while )` | ⚪ `void` | `INT(1) INT(1) OP(<=) REF(C) STORE(B) STORE(B) W...` |
| 6 | `( ( int int <= ) ( ( memid mem_store ) mem_store ) while ) #2` | ⚪ `void` | `INT(1) INT(1) OP(<=) REF(B) STORE(A) STORE(A) W...` |
| 7 | `( ( memid int + ) mem_store )` | 🔢 `int` | `REF(I) INT(1) OP(+) STORE(I)` |
| 8 | `( memid )` | 🔢 `int` | `REF(A)` |


---


## Estatísticas


### Distribuição de Tipos

- 🔢 `int`: 5 (62.5%)
- ⚪ `void`: 3 (37.5%)

### Taxa de Sucesso

**100.0%** das linhas foram tipadas com sucesso.
