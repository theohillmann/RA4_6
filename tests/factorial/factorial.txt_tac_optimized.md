# TAC: factorial.txt_tac_optimized

## Instruções formatadas

```text
  0: MEM[N] = 8.0
  1: MEM[I] = 1.0
  2: MEM[F] = 1.0
  3: L0:
  4: t3 = MEM[I]
  5: t4 = MEM[N]
  6: t5 = t3 <= t4
  7: ifFalse t5 goto L1
  8: t6 = MEM[F]
  9: t7 = MEM[I]
 10: t8 = t6 * t7
 11: MEM[F] = t8
 12: t9 = MEM[I]
 13: t11 = t9 + 1.0
 14: MEM[I] = t11
 15: goto L0
 16: L1:
 17: t12 = MEM[F]
 18: print t12
```

## Tabela de instruções

| # | Label | Op | Dest | Arg1 | OpSymbol | Arg2 |
|---|-------|----|------|------|----------|------|
| 0 |  | mem_store | N | 8.0 |  |  |
| 1 |  | mem_store | I | 1.0 |  |  |
| 2 |  | mem_store | F | 1.0 |  |  |
| 3 | L0 | label |  |  |  |  |
| 4 |  | mem_load | t3 | I |  |  |
| 5 |  | mem_load | t4 | N |  |  |
| 6 |  | binop | t5 | t3 | <= | t4 |
| 7 | L1 | ifFalse |  | t5 |  |  |
| 8 |  | mem_load | t6 | F |  |  |
| 9 |  | mem_load | t7 | I |  |  |
| 10 |  | binop | t8 | t6 | * | t7 |
| 11 |  | mem_store | F | t8 |  |  |
| 12 |  | mem_load | t9 | I |  |  |
| 13 |  | binop | t11 | t9 | + | 1.0 |
| 14 |  | mem_store | I | t11 |  |  |
| 15 | L0 | goto |  |  |  |  |
| 16 | L1 | label |  |  |  |  |
| 17 |  | mem_load | t12 | F |  |  |
| 18 |  | print |  | t12 |  |  |

## JSON original

```json
[
  {
    "op": "mem_store",
    "dest": "N",
    "arg1": "8.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "I",
    "arg1": "1.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F",
    "arg1": "1.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "label",
    "dest": null,
    "arg1": null,
    "arg2": null,
    "label": "L0",
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t3",
    "arg1": "I",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t4",
    "arg1": "N",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t5",
    "arg1": "t3",
    "arg2": "t4",
    "label": null,
    "op_symbol": "<="
  },
  {
    "op": "ifFalse",
    "dest": null,
    "arg1": "t5",
    "arg2": null,
    "label": "L1",
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t6",
    "arg1": "F",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t7",
    "arg1": "I",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t8",
    "arg1": "t6",
    "arg2": "t7",
    "label": null,
    "op_symbol": "*"
  },
  {
    "op": "mem_store",
    "dest": "F",
    "arg1": "t8",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t9",
    "arg1": "I",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t11",
    "arg1": "t9",
    "arg2": "1.0",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "I",
    "arg1": "t11",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "goto",
    "dest": null,
    "arg1": null,
    "arg2": null,
    "label": "L0",
    "op_symbol": null
  },
  {
    "op": "label",
    "dest": null,
    "arg1": null,
    "arg2": null,
    "label": "L1",
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t12",
    "arg1": "F",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t12",
    "arg2": null,
    "label": null,
    "op_symbol": null
  }
]
```
