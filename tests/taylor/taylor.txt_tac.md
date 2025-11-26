# TAC: taylor.txt_tac

## Instruções formatadas

```text
  0: t0 = 1.0
  1: MEM[RESULT] = t0
  2: t1 = 0.5
  3: MEM[X] = t1
  4: t2 = 0.5
  5: t3 = 2
  6: t4 = t2 ^ t3
  7: MEM[POT1] = t4
  8: t5 = 2
  9: MEM[N1] = t5
 10: t6 = 1
 11: MEM[I1] = t6
 12: t7 = 1
 13: MEM[F1] = t7
 14: L0:
 15: t8 = MEM[I1]
 16: t9 = MEM[N1]
 17: t10 = t8 <= t9
 18: ifFalse t10 goto L1
 19: t11 = MEM[F1]
 20: t12 = MEM[I1]
 21: t13 = t11 * t12
 22: MEM[F1] = t13
 23: t14 = MEM[I1]
 24: t15 = 1
 25: t16 = t14 + t15
 26: MEM[I1] = t16
 27: goto L0
 28: L1:
 29: t17 = MEM[POT1]
 30: t18 = MEM[F1]
 31: t19 = t17 | t18
 32: MEM[FRA1] = t19
 33: t20 = MEM[RESULT]
 34: t21 = MEM[FRA1]
 35: t22 = t20 - t21
 36: MEM[RESULT] = t22
 37: t23 = 0.5
 38: t24 = 4
 39: t25 = t23 ^ t24
 40: MEM[POT2] = t25
 41: t26 = 4
 42: MEM[N2] = t26
 43: t27 = 1
 44: MEM[I2] = t27
 45: t28 = 1
 46: MEM[F2] = t28
 47: L2:
 48: t29 = MEM[I2]
 49: t30 = MEM[N2]
 50: t31 = t29 <= t30
 51: ifFalse t31 goto L3
 52: t32 = MEM[F2]
 53: t33 = MEM[I2]
 54: t34 = t32 * t33
 55: MEM[F2] = t34
 56: t35 = MEM[I2]
 57: t36 = 1
 58: t37 = t35 + t36
 59: MEM[I2] = t37
 60: goto L2
 61: L3:
 62: t38 = MEM[POT2]
 63: t39 = MEM[F2]
 64: t40 = t38 | t39
 65: MEM[FRA2] = t40
 66: t41 = MEM[RESULT]
 67: t42 = MEM[FRA2]
 68: t43 = t41 + t42
 69: MEM[RESULT] = t43
 70: t44 = 0.5
 71: t45 = 6
 72: t46 = t44 ^ t45
 73: MEM[POT3] = t46
 74: t47 = 6
 75: MEM[N3] = t47
 76: t48 = 1
 77: MEM[I3] = t48
 78: t49 = 1
 79: MEM[F3] = t49
 80: L4:
 81: t50 = MEM[I3]
 82: t51 = MEM[N3]
 83: t52 = t50 <= t51
 84: ifFalse t52 goto L5
 85: t53 = MEM[F3]
 86: t54 = MEM[I3]
 87: t55 = t53 * t54
 88: MEM[F3] = t55
 89: t56 = MEM[I3]
 90: t57 = 1
 91: t58 = t56 + t57
 92: MEM[I3] = t58
 93: goto L4
 94: L5:
 95: t59 = MEM[POT2]
 96: t60 = MEM[F3]
 97: t61 = t59 | t60
 98: MEM[FRA3] = t61
 99: t62 = MEM[RESULT]
100: t63 = MEM[FRA2]
101: t64 = t62 - t63
102: MEM[RESULT] = t64
103: t65 = MEM[RESULT]
104: print t65
```

## Tabela de instruções

| # | Label | Op | Dest | Arg1 | OpSymbol | Arg2 |
|---|-------|----|------|------|----------|------|
| 0 |  | assign | t0 | 1.0 |  |  |
| 1 |  | mem_store | RESULT | t0 |  |  |
| 2 |  | assign | t1 | 0.5 |  |  |
| 3 |  | mem_store | X | t1 |  |  |
| 4 |  | assign | t2 | 0.5 |  |  |
| 5 |  | assign | t3 | 2 |  |  |
| 6 |  | binop | t4 | t2 | ^ | t3 |
| 7 |  | mem_store | POT1 | t4 |  |  |
| 8 |  | assign | t5 | 2 |  |  |
| 9 |  | mem_store | N1 | t5 |  |  |
| 10 |  | assign | t6 | 1 |  |  |
| 11 |  | mem_store | I1 | t6 |  |  |
| 12 |  | assign | t7 | 1 |  |  |
| 13 |  | mem_store | F1 | t7 |  |  |
| 14 | L0 | label |  |  |  |  |
| 15 |  | mem_load | t8 | I1 |  |  |
| 16 |  | mem_load | t9 | N1 |  |  |
| 17 |  | binop | t10 | t8 | <= | t9 |
| 18 | L1 | ifFalse |  | t10 |  |  |
| 19 |  | mem_load | t11 | F1 |  |  |
| 20 |  | mem_load | t12 | I1 |  |  |
| 21 |  | binop | t13 | t11 | * | t12 |
| 22 |  | mem_store | F1 | t13 |  |  |
| 23 |  | mem_load | t14 | I1 |  |  |
| 24 |  | assign | t15 | 1 |  |  |
| 25 |  | binop | t16 | t14 | + | t15 |
| 26 |  | mem_store | I1 | t16 |  |  |
| 27 | L0 | goto |  |  |  |  |
| 28 | L1 | label |  |  |  |  |
| 29 |  | mem_load | t17 | POT1 |  |  |
| 30 |  | mem_load | t18 | F1 |  |  |
| 31 |  | binop | t19 | t17 | | | t18 |
| 32 |  | mem_store | FRA1 | t19 |  |  |
| 33 |  | mem_load | t20 | RESULT |  |  |
| 34 |  | mem_load | t21 | FRA1 |  |  |
| 35 |  | binop | t22 | t20 | - | t21 |
| 36 |  | mem_store | RESULT | t22 |  |  |
| 37 |  | assign | t23 | 0.5 |  |  |
| 38 |  | assign | t24 | 4 |  |  |
| 39 |  | binop | t25 | t23 | ^ | t24 |
| 40 |  | mem_store | POT2 | t25 |  |  |
| 41 |  | assign | t26 | 4 |  |  |
| 42 |  | mem_store | N2 | t26 |  |  |
| 43 |  | assign | t27 | 1 |  |  |
| 44 |  | mem_store | I2 | t27 |  |  |
| 45 |  | assign | t28 | 1 |  |  |
| 46 |  | mem_store | F2 | t28 |  |  |
| 47 | L2 | label |  |  |  |  |
| 48 |  | mem_load | t29 | I2 |  |  |
| 49 |  | mem_load | t30 | N2 |  |  |
| 50 |  | binop | t31 | t29 | <= | t30 |
| 51 | L3 | ifFalse |  | t31 |  |  |
| 52 |  | mem_load | t32 | F2 |  |  |
| 53 |  | mem_load | t33 | I2 |  |  |
| 54 |  | binop | t34 | t32 | * | t33 |
| 55 |  | mem_store | F2 | t34 |  |  |
| 56 |  | mem_load | t35 | I2 |  |  |
| 57 |  | assign | t36 | 1 |  |  |
| 58 |  | binop | t37 | t35 | + | t36 |
| 59 |  | mem_store | I2 | t37 |  |  |
| 60 | L2 | goto |  |  |  |  |
| 61 | L3 | label |  |  |  |  |
| 62 |  | mem_load | t38 | POT2 |  |  |
| 63 |  | mem_load | t39 | F2 |  |  |
| 64 |  | binop | t40 | t38 | | | t39 |
| 65 |  | mem_store | FRA2 | t40 |  |  |
| 66 |  | mem_load | t41 | RESULT |  |  |
| 67 |  | mem_load | t42 | FRA2 |  |  |
| 68 |  | binop | t43 | t41 | + | t42 |
| 69 |  | mem_store | RESULT | t43 |  |  |
| 70 |  | assign | t44 | 0.5 |  |  |
| 71 |  | assign | t45 | 6 |  |  |
| 72 |  | binop | t46 | t44 | ^ | t45 |
| 73 |  | mem_store | POT3 | t46 |  |  |
| 74 |  | assign | t47 | 6 |  |  |
| 75 |  | mem_store | N3 | t47 |  |  |
| 76 |  | assign | t48 | 1 |  |  |
| 77 |  | mem_store | I3 | t48 |  |  |
| 78 |  | assign | t49 | 1 |  |  |
| 79 |  | mem_store | F3 | t49 |  |  |
| 80 | L4 | label |  |  |  |  |
| 81 |  | mem_load | t50 | I3 |  |  |
| 82 |  | mem_load | t51 | N3 |  |  |
| 83 |  | binop | t52 | t50 | <= | t51 |
| 84 | L5 | ifFalse |  | t52 |  |  |
| 85 |  | mem_load | t53 | F3 |  |  |
| 86 |  | mem_load | t54 | I3 |  |  |
| 87 |  | binop | t55 | t53 | * | t54 |
| 88 |  | mem_store | F3 | t55 |  |  |
| 89 |  | mem_load | t56 | I3 |  |  |
| 90 |  | assign | t57 | 1 |  |  |
| 91 |  | binop | t58 | t56 | + | t57 |
| 92 |  | mem_store | I3 | t58 |  |  |
| 93 | L4 | goto |  |  |  |  |
| 94 | L5 | label |  |  |  |  |
| 95 |  | mem_load | t59 | POT2 |  |  |
| 96 |  | mem_load | t60 | F3 |  |  |
| 97 |  | binop | t61 | t59 | | | t60 |
| 98 |  | mem_store | FRA3 | t61 |  |  |
| 99 |  | mem_load | t62 | RESULT |  |  |
| 100 |  | mem_load | t63 | FRA2 |  |  |
| 101 |  | binop | t64 | t62 | - | t63 |
| 102 |  | mem_store | RESULT | t64 |  |  |
| 103 |  | mem_load | t65 | RESULT |  |  |
| 104 |  | print |  | t65 |  |  |

## JSON original

```json
[
  {
    "op": "assign",
    "dest": "t0",
    "arg1": "1.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "RESULT",
    "arg1": "t0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t1",
    "arg1": "0.5",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "X",
    "arg1": "t1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t2",
    "arg1": "0.5",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t3",
    "arg1": "2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t4",
    "arg1": "t2",
    "arg2": "t3",
    "label": null,
    "op_symbol": "^"
  },
  {
    "op": "mem_store",
    "dest": "POT1",
    "arg1": "t4",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t5",
    "arg1": "2",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "N1",
    "arg1": "t5",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t6",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "I1",
    "arg1": "t6",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t7",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t7",
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
    "op": "assign",
    "dest": "t15",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t16",
    "arg1": "t14",
    "arg2": "t15",
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
    "op": "assign",
    "dest": "t23",
    "arg1": "0.5",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t24",
    "arg1": "4",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t25",
    "arg1": "t23",
    "arg2": "t24",
    "label": null,
    "op_symbol": "^"
  },
  {
    "op": "mem_store",
    "dest": "POT2",
    "arg1": "t25",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t26",
    "arg1": "4",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "N2",
    "arg1": "t26",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t27",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "I2",
    "arg1": "t27",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t28",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F2",
    "arg1": "t28",
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
    "op": "assign",
    "dest": "t36",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t37",
    "arg1": "t35",
    "arg2": "t36",
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
    "op": "assign",
    "dest": "t44",
    "arg1": "0.5",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t45",
    "arg1": "6",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t46",
    "arg1": "t44",
    "arg2": "t45",
    "label": null,
    "op_symbol": "^"
  },
  {
    "op": "mem_store",
    "dest": "POT3",
    "arg1": "t46",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t47",
    "arg1": "6",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "N3",
    "arg1": "t47",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t48",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "I3",
    "arg1": "t48",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "assign",
    "dest": "t49",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t49",
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
    "op": "assign",
    "dest": "t57",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t58",
    "arg1": "t56",
    "arg2": "t57",
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
