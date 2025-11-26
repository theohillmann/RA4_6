# TAC: factorial.txt_tac

## Instruções formatadas

```text
  0: t0 = 8
  1: MEM[N] = t0
  2: t1 = 1
  3: MEM[I] = t1
  4: t2 = 1
  5: MEM[F] = t2
  6: L0:
  7: t3 = MEM[I]
  8: t4 = MEM[N]
  9: t5 = t3 <= t4
 10: ifFalse t5 goto L1
 11: t6 = MEM[F]
 12: t7 = MEM[I]
 13: t8 = t6 * t7
 14: MEM[F] = t8
 15: t9 = MEM[I]
 16: t10 = 1
 17: t11 = t9 + t10
 18: MEM[I] = t11
 19: goto L0
 20: L1:
 21: t12 = MEM[F]
 22: print t12
```

## Tabela de instruções

| # | Label | Op | Dest | Arg1 | OpSymbol | Arg2 |
|---|-------|----|------|------|----------|------|
| 0 |  | assign | t0 | 8 |  |  |
| 1 |  | mem_store | N | t0 |  |  |
| 2 |  | assign | t1 | 1 |  |  |
| 3 |  | mem_store | I | t1 |  |  |
| 4 |  | assign | t2 | 1 |  |  |
| 5 |  | mem_store | F | t2 |  |  |
| 6 | L0 | label |  |  |  |  |
| 7 |  | mem_load | t3 | I |  |  |
| 8 |  | mem_load | t4 | N |  |  |
| 9 |  | binop | t5 | t3 | <= | t4 |
| 10 | L1 | ifFalse |  | t5 |  |  |
| 11 |  | mem_load | t6 | F |  |  |
| 12 |  | mem_load | t7 | I |  |  |
| 13 |  | binop | t8 | t6 | * | t7 |
| 14 |  | mem_store | F | t8 |  |  |
| 15 |  | mem_load | t9 | I |  |  |
| 16 |  | assign | t10 | 1 |  |  |
| 17 |  | binop | t11 | t9 | + | t10 |
| 18 |  | mem_store | I | t11 |  |  |
| 19 | L0 | goto |  |  |  |  |
| 20 | L1 | label |  |  |  |  |
| 21 |  | mem_load | t12 | F |  |  |
| 22 |  | print |  | t12 |  |  |

## JSON original

```json
[
  {
    "op": "assign",
    "dest": "t0",
    "arg1": "8",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "N",
    "arg1": "t0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t1",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "I",
    "arg1": "t1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t2",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F",
    "arg1": "t2",
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
    "op": "assign",
    "dest": "t10",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t11",
    "arg1": "t9",
    "arg2": "t10",
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
