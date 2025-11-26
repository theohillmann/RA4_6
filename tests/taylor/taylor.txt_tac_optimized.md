# TAC: taylor.txt_tac_optimized

## Instruções formatadas

```text
  0: MEM[RESULT] = 1.0
  1: MEM[X] = 0.5
  2: MEM[POT1] = 0.25
  3: MEM[N1] = 2.0
  4: MEM[I1] = 1.0
  5: MEM[F1] = 1.0
  6: L0:
  7: t8 = MEM[I1]
  8: t9 = MEM[N1]
  9: t10 = t8 <= t9
 10: ifFalse t10 goto L1
 11: t11 = MEM[F1]
 12: t12 = MEM[I1]
 13: t13 = t11 * t12
 14: MEM[F1] = t13
 15: t14 = MEM[I1]
 16: t16 = t14 + 1.0
 17: MEM[I1] = t16
 18: goto L0
 19: L1:
 20: t17 = MEM[POT1]
 21: t18 = MEM[F1]
 22: t19 = t17 | t18
 23: MEM[FRA1] = t19
 24: t20 = MEM[RESULT]
 25: t21 = MEM[FRA1]
 26: t22 = t20 - t21
 27: MEM[RESULT] = t22
 28: MEM[POT2] = 0.0625
 29: MEM[N2] = 4.0
 30: MEM[I2] = 1.0
 31: MEM[F2] = 1.0
 32: L2:
 33: t29 = MEM[I2]
 34: t30 = MEM[N2]
 35: t31 = t29 <= t30
 36: ifFalse t31 goto L3
 37: t32 = MEM[F2]
 38: t33 = MEM[I2]
 39: t34 = t32 * t33
 40: MEM[F2] = t34
 41: t35 = MEM[I2]
 42: t37 = t35 + 1.0
 43: MEM[I2] = t37
 44: goto L2
 45: L3:
 46: t38 = MEM[POT2]
 47: t39 = MEM[F2]
 48: t40 = t38 | t39
 49: MEM[FRA2] = t40
 50: t41 = MEM[RESULT]
 51: t42 = MEM[FRA2]
 52: t43 = t41 + t42
 53: MEM[RESULT] = t43
 54: MEM[POT3] = 0.015625
 55: MEM[N3] = 6.0
 56: MEM[I3] = 1.0
 57: MEM[F3] = 1.0
 58: L4:
 59: t50 = MEM[I3]
 60: t51 = MEM[N3]
 61: t52 = t50 <= t51
 62: ifFalse t52 goto L5
 63: t53 = MEM[F3]
 64: t54 = MEM[I3]
 65: t55 = t53 * t54
 66: MEM[F3] = t55
 67: t56 = MEM[I3]
 68: t58 = t56 + 1.0
 69: MEM[I3] = t58
 70: goto L4
 71: L5:
 72: t59 = MEM[POT2]
 73: t60 = MEM[F3]
 74: t61 = t59 | t60
 75: MEM[FRA3] = t61
 76: t62 = MEM[RESULT]
 77: t63 = MEM[FRA2]
 78: t64 = t62 - t63
 79: MEM[RESULT] = t64
 80: t65 = MEM[RESULT]
 81: print t65
```

## Tabela de instruções

| # | Label | Op | Dest | Arg1 | OpSymbol | Arg2 |
|---|-------|----|------|------|----------|------|
| 0 |  | mem_store | RESULT | 1.0 |  |  |
| 1 |  | mem_store | X | 0.5 |  |  |
| 2 |  | mem_store | POT1 | 0.25 |  |  |
| 3 |  | mem_store | N1 | 2.0 |  |  |
| 4 |  | mem_store | I1 | 1.0 |  |  |
| 5 |  | mem_store | F1 | 1.0 |  |  |
| 6 | L0 | label |  |  |  |  |
| 7 |  | mem_load | t8 | I1 |  |  |
| 8 |  | mem_load | t9 | N1 |  |  |
| 9 |  | binop | t10 | t8 | <= | t9 |
| 10 | L1 | ifFalse |  | t10 |  |  |
| 11 |  | mem_load | t11 | F1 |  |  |
| 12 |  | mem_load | t12 | I1 |  |  |
| 13 |  | binop | t13 | t11 | * | t12 |
| 14 |  | mem_store | F1 | t13 |  |  |
| 15 |  | mem_load | t14 | I1 |  |  |
| 16 |  | binop | t16 | t14 | + | 1.0 |
| 17 |  | mem_store | I1 | t16 |  |  |
| 18 | L0 | goto |  |  |  |  |
| 19 | L1 | label |  |  |  |  |
| 20 |  | mem_load | t17 | POT1 |  |  |
| 21 |  | mem_load | t18 | F1 |  |  |
| 22 |  | binop | t19 | t17 | | | t18 |
| 23 |  | mem_store | FRA1 | t19 |  |  |
| 24 |  | mem_load | t20 | RESULT |  |  |
| 25 |  | mem_load | t21 | FRA1 |  |  |
| 26 |  | binop | t22 | t20 | - | t21 |
| 27 |  | mem_store | RESULT | t22 |  |  |
| 28 |  | mem_store | POT2 | 0.0625 |  |  |
| 29 |  | mem_store | N2 | 4.0 |  |  |
| 30 |  | mem_store | I2 | 1.0 |  |  |
| 31 |  | mem_store | F2 | 1.0 |  |  |
| 32 | L2 | label |  |  |  |  |
| 33 |  | mem_load | t29 | I2 |  |  |
| 34 |  | mem_load | t30 | N2 |  |  |
| 35 |  | binop | t31 | t29 | <= | t30 |
| 36 | L3 | ifFalse |  | t31 |  |  |
| 37 |  | mem_load | t32 | F2 |  |  |
| 38 |  | mem_load | t33 | I2 |  |  |
| 39 |  | binop | t34 | t32 | * | t33 |
| 40 |  | mem_store | F2 | t34 |  |  |
| 41 |  | mem_load | t35 | I2 |  |  |
| 42 |  | binop | t37 | t35 | + | 1.0 |
| 43 |  | mem_store | I2 | t37 |  |  |
| 44 | L2 | goto |  |  |  |  |
| 45 | L3 | label |  |  |  |  |
| 46 |  | mem_load | t38 | POT2 |  |  |
| 47 |  | mem_load | t39 | F2 |  |  |
| 48 |  | binop | t40 | t38 | | | t39 |
| 49 |  | mem_store | FRA2 | t40 |  |  |
| 50 |  | mem_load | t41 | RESULT |  |  |
| 51 |  | mem_load | t42 | FRA2 |  |  |
| 52 |  | binop | t43 | t41 | + | t42 |
| 53 |  | mem_store | RESULT | t43 |  |  |
| 54 |  | mem_store | POT3 | 0.015625 |  |  |
| 55 |  | mem_store | N3 | 6.0 |  |  |
| 56 |  | mem_store | I3 | 1.0 |  |  |
| 57 |  | mem_store | F3 | 1.0 |  |  |
| 58 | L4 | label |  |  |  |  |
| 59 |  | mem_load | t50 | I3 |  |  |
| 60 |  | mem_load | t51 | N3 |  |  |
| 61 |  | binop | t52 | t50 | <= | t51 |
| 62 | L5 | ifFalse |  | t52 |  |  |
| 63 |  | mem_load | t53 | F3 |  |  |
| 64 |  | mem_load | t54 | I3 |  |  |
| 65 |  | binop | t55 | t53 | * | t54 |
| 66 |  | mem_store | F3 | t55 |  |  |
| 67 |  | mem_load | t56 | I3 |  |  |
| 68 |  | binop | t58 | t56 | + | 1.0 |
| 69 |  | mem_store | I3 | t58 |  |  |
| 70 | L4 | goto |  |  |  |  |
| 71 | L5 | label |  |  |  |  |
| 72 |  | mem_load | t59 | POT2 |  |  |
| 73 |  | mem_load | t60 | F3 |  |  |
| 74 |  | binop | t61 | t59 | | | t60 |
| 75 |  | mem_store | FRA3 | t61 |  |  |
| 76 |  | mem_load | t62 | RESULT |  |  |
| 77 |  | mem_load | t63 | FRA2 |  |  |
| 78 |  | binop | t64 | t62 | - | t63 |
| 79 |  | mem_store | RESULT | t64 |  |  |
| 80 |  | mem_load | t65 | RESULT |  |  |
| 81 |  | print |  | t65 |  |  |

## JSON original

```json
[
  {
    "op": "mem_store",
    "dest": "RESULT",
    "arg1": "1.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "X",
    "arg1": "0.5",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "POT1",
    "arg1": "0.25",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "N1",
    "arg1": "2.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "I1",
    "arg1": "1.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
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
    "dest": "t8",
    "arg1": "I1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t9",
    "arg1": "N1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t10",
    "arg1": "t8",
    "arg2": "t9",
    "label": null,
    "op_symbol": "<="
  },
  {
    "op": "ifFalse",
    "dest": null,
    "arg1": "t10",
    "arg2": null,
    "label": "L1",
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t11",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t12",
    "arg1": "I1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t13",
    "arg1": "t11",
    "arg2": "t12",
    "label": null,
    "op_symbol": "*"
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t13",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t14",
    "arg1": "I1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t16",
    "arg1": "t14",
    "arg2": "1.0",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "I1",
    "arg1": "t16",
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
    "dest": "t17",
    "arg1": "POT1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t18",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t19",
    "arg1": "t17",
    "arg2": "t18",
    "label": null,
    "op_symbol": "|"
  },
  {
    "op": "mem_store",
    "dest": "FRA1",
    "arg1": "t19",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t20",
    "arg1": "RESULT",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t21",
    "arg1": "FRA1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t22",
    "arg1": "t20",
    "arg2": "t21",
    "label": null,
    "op_symbol": "-"
  },
  {
    "op": "mem_store",
    "dest": "RESULT",
    "arg1": "t22",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "POT2",
    "arg1": "0.0625",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "N2",
    "arg1": "4.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "I2",
    "arg1": "1.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F2",
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
    "label": "L2",
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t29",
    "arg1": "I2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t30",
    "arg1": "N2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t31",
    "arg1": "t29",
    "arg2": "t30",
    "label": null,
    "op_symbol": "<="
  },
  {
    "op": "ifFalse",
    "dest": null,
    "arg1": "t31",
    "arg2": null,
    "label": "L3",
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t32",
    "arg1": "F2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t33",
    "arg1": "I2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t34",
    "arg1": "t32",
    "arg2": "t33",
    "label": null,
    "op_symbol": "*"
  },
  {
    "op": "mem_store",
    "dest": "F2",
    "arg1": "t34",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t35",
    "arg1": "I2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t37",
    "arg1": "t35",
    "arg2": "1.0",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "I2",
    "arg1": "t37",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "goto",
    "dest": null,
    "arg1": null,
    "arg2": null,
    "label": "L2",
    "op_symbol": null
  },
  {
    "op": "label",
    "dest": null,
    "arg1": null,
    "arg2": null,
    "label": "L3",
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t38",
    "arg1": "POT2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t39",
    "arg1": "F2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t40",
    "arg1": "t38",
    "arg2": "t39",
    "label": null,
    "op_symbol": "|"
  },
  {
    "op": "mem_store",
    "dest": "FRA2",
    "arg1": "t40",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t41",
    "arg1": "RESULT",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t42",
    "arg1": "FRA2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t43",
    "arg1": "t41",
    "arg2": "t42",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "RESULT",
    "arg1": "t43",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "POT3",
    "arg1": "0.015625",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "N3",
    "arg1": "6.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "I3",
    "arg1": "1.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
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
    "label": "L4",
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t50",
    "arg1": "I3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t51",
    "arg1": "N3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t52",
    "arg1": "t50",
    "arg2": "t51",
    "label": null,
    "op_symbol": "<="
  },
  {
    "op": "ifFalse",
    "dest": null,
    "arg1": "t52",
    "arg2": null,
    "label": "L5",
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t53",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t54",
    "arg1": "I3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t55",
    "arg1": "t53",
    "arg2": "t54",
    "label": null,
    "op_symbol": "*"
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t55",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t56",
    "arg1": "I3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t58",
    "arg1": "t56",
    "arg2": "1.0",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "I3",
    "arg1": "t58",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "goto",
    "dest": null,
    "arg1": null,
    "arg2": null,
    "label": "L4",
    "op_symbol": null
  },
  {
    "op": "label",
    "dest": null,
    "arg1": null,
    "arg2": null,
    "label": "L5",
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t59",
    "arg1": "POT2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t60",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t61",
    "arg1": "t59",
    "arg2": "t60",
    "label": null,
    "op_symbol": "|"
  },
  {
    "op": "mem_store",
    "dest": "FRA3",
    "arg1": "t61",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t62",
    "arg1": "RESULT",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t63",
    "arg1": "FRA2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t64",
    "arg1": "t62",
    "arg2": "t63",
    "label": null,
    "op_symbol": "-"
  },
  {
    "op": "mem_store",
    "dest": "RESULT",
    "arg1": "t64",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t65",
    "arg1": "RESULT",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t65",
    "arg2": null,
    "label": null,
    "op_symbol": null
  }
]
```
