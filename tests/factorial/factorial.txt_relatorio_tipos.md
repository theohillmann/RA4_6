# Relatório de Tipos Inferidos

**Total de linhas analisadas:** 5

**Data de geração:** 2025-11-25 23:34:20


---


## Tabela de Tipos por Linha


| Linha | Contexto | Tipo Inferido | Notação Posfixa |
|-------|----------|---------------|-----------------|
| 1 | `( int mem_store )` | 🔢 `int` | `INT(8) STORE(N)` |
| 2 | `( int mem_store ) #2` | 🔢 `int` | `INT(1) STORE(I)` |
| 3 | `( int mem_store ) #3` | 🔢 `int` | `INT(1) STORE(F)` |
| 4 | `( ( memid memid <= ) ( ( memid memid * ) mem_store ) ( ( memid int + ) mem_store ) for )` | ⚪ `void` | `REF(I) REF(N) OP(<=) REF(F) REF(I) OP(*) STORE(...` |
| 5 | `( memid )` | 🔢 `int` | `REF(F)` |


---


## Estatísticas


### Distribuição de Tipos

- 🔢 `int`: 4 (80.0%)
- ⚪ `void`: 1 (20.0%)

### Taxa de Sucesso

**100.0%** das linhas foram tipadas com sucesso.
