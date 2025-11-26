# TAC: fibonacci.txt_tac_optimized

## Instruções formatadas

```text
  0: MEM[A] = 0.0
  1: t1 = MEM[A]
  2: print t1
  3: MEM[A] = 1.0
  4: t3 = MEM[A]
  5: print t3
  6: MEM[F1] = t3
  7: MEM[F3] = 0.0
  8: t4 = MEM[F1]
  9: t5 = MEM[F3]
 10: t6 = t4 + t5
 11: MEM[A] = t6
 12: t7 = MEM[A]
 13: print t7
 14: MEM[F1] = t7
 15: MEM[F3] = t3
 16: t8 = MEM[F1]
 17: t9 = MEM[F3]
 18: t10 = t8 + t9
 19: MEM[A] = t10
 20: t11 = MEM[A]
 21: print t11
 22: MEM[F1] = t11
 23: MEM[F3] = t7
 24: t12 = MEM[F1]
 25: t13 = MEM[F3]
 26: t14 = t12 + t13
 27: MEM[A] = t14
 28: t15 = MEM[A]
 29: print t15
 30: MEM[F1] = t15
 31: MEM[F3] = t11
 32: t16 = MEM[F1]
 33: t17 = MEM[F3]
 34: t18 = t16 + t17
 35: MEM[A] = t18
 36: t19 = MEM[A]
 37: print t19
 38: MEM[F1] = t19
 39: MEM[F3] = t15
 40: t20 = MEM[F1]
 41: t21 = MEM[F3]
 42: t22 = t20 + t21
 43: MEM[A] = t22
 44: t23 = MEM[A]
 45: print t23
 46: MEM[F1] = t23
 47: MEM[F3] = t19
 48: t24 = MEM[F1]
 49: t25 = MEM[F3]
 50: t26 = t24 + t25
 51: MEM[A] = t26
 52: t27 = MEM[A]
 53: print t27
 54: MEM[F1] = t27
 55: MEM[F3] = t23
 56: t28 = MEM[F1]
 57: t29 = MEM[F3]
 58: t30 = t28 + t29
 59: MEM[A] = t30
 60: t31 = MEM[A]
 61: print t31
 62: MEM[F1] = t31
 63: MEM[F3] = t27
 64: t32 = MEM[F1]
 65: t33 = MEM[F3]
 66: t34 = t32 + t33
 67: MEM[A] = t34
 68: t35 = MEM[A]
 69: print t35
 70: MEM[F1] = t35
 71: MEM[F3] = t31
 72: t36 = MEM[F1]
 73: t37 = MEM[F3]
 74: t38 = t36 + t37
 75: MEM[A] = t38
 76: t39 = MEM[A]
 77: print t39
 78: MEM[F1] = t39
 79: MEM[F3] = t35
 80: t40 = MEM[F1]
 81: t41 = MEM[F3]
 82: t42 = t40 + t41
 83: MEM[A] = t42
 84: t43 = MEM[A]
 85: print t43
 86: MEM[F1] = t43
 87: MEM[F3] = t39
 88: t44 = MEM[F1]
 89: t45 = MEM[F3]
 90: t46 = t44 + t45
 91: MEM[A] = t46
 92: t47 = MEM[A]
 93: print t47
 94: MEM[F1] = t47
 95: MEM[F3] = t43
 96: t48 = MEM[F1]
 97: t49 = MEM[F3]
 98: t50 = t48 + t49
 99: MEM[A] = t50
100: t51 = MEM[A]
101: print t51
102: MEM[F1] = t51
103: MEM[F3] = t47
104: t52 = MEM[F1]
105: t53 = MEM[F3]
106: t54 = t52 + t53
107: MEM[A] = t54
108: t55 = MEM[A]
109: print t55
110: MEM[F1] = t55
111: MEM[F3] = t51
112: t56 = MEM[F1]
113: t57 = MEM[F3]
114: t58 = t56 + t57
115: MEM[A] = t58
116: t59 = MEM[A]
117: print t59
118: MEM[F1] = t59
119: MEM[F3] = t55
120: t60 = MEM[F1]
121: t61 = MEM[F3]
122: t62 = t60 + t61
123: MEM[A] = t62
124: t63 = MEM[A]
125: print t63
126: MEM[F1] = t63
127: MEM[F3] = t59
128: t64 = MEM[F1]
129: t65 = MEM[F3]
130: t66 = t64 + t65
131: MEM[A] = t66
132: t67 = MEM[A]
133: print t67
134: MEM[F1] = t67
135: MEM[F3] = t63
136: t68 = MEM[F1]
137: t69 = MEM[F3]
138: t70 = t68 + t69
139: MEM[A] = t70
140: t71 = MEM[A]
141: print t71
142: MEM[F1] = t71
143: MEM[F3] = t67
144: t72 = MEM[F1]
145: t73 = MEM[F3]
146: t74 = t72 + t73
147: MEM[A] = t74
148: t75 = MEM[A]
149: print t75
150: MEM[F1] = t75
151: MEM[F3] = t71
152: t76 = MEM[F1]
153: t77 = MEM[F3]
154: t78 = t76 + t77
155: MEM[A] = t78
156: t79 = MEM[A]
157: print t79
158: MEM[F1] = t79
159: MEM[F3] = t75
160: t80 = MEM[F1]
161: t81 = MEM[F3]
162: t82 = t80 + t81
163: MEM[A] = t82
164: t83 = MEM[A]
165: print t83
166: MEM[F1] = t83
167: MEM[F3] = t79
168: t84 = MEM[F1]
169: t85 = MEM[F3]
170: t86 = t84 + t85
171: MEM[A] = t86
172: t87 = MEM[A]
173: print t87
174: MEM[F1] = t87
175: MEM[F3] = t83
176: t88 = MEM[F1]
177: t89 = MEM[F3]
178: t90 = t88 + t89
179: MEM[A] = t90
180: t91 = MEM[A]
181: print t91
182: MEM[F1] = t91
183: MEM[F3] = t87
184: t92 = MEM[F1]
185: t93 = MEM[F3]
186: t94 = t92 + t93
187: MEM[A] = t94
188: t95 = MEM[A]
189: print t95
```

## Tabela de instruções

| # | Label | Op | Dest | Arg1 | OpSymbol | Arg2 |
|---|-------|----|------|------|----------|------|
| 0 |  | mem_store | A | 0.0 |  |  |
| 1 |  | mem_load | t1 | A |  |  |
| 2 |  | print |  | t1 |  |  |
| 3 |  | mem_store | A | 1.0 |  |  |
| 4 |  | mem_load | t3 | A |  |  |
| 5 |  | print |  | t3 |  |  |
| 6 |  | mem_store | F1 | t3 |  |  |
| 7 |  | mem_store | F3 | 0.0 |  |  |
| 8 |  | mem_load | t4 | F1 |  |  |
| 9 |  | mem_load | t5 | F3 |  |  |
| 10 |  | binop | t6 | t4 | + | t5 |
| 11 |  | mem_store | A | t6 |  |  |
| 12 |  | mem_load | t7 | A |  |  |
| 13 |  | print |  | t7 |  |  |
| 14 |  | mem_store | F1 | t7 |  |  |
| 15 |  | mem_store | F3 | t3 |  |  |
| 16 |  | mem_load | t8 | F1 |  |  |
| 17 |  | mem_load | t9 | F3 |  |  |
| 18 |  | binop | t10 | t8 | + | t9 |
| 19 |  | mem_store | A | t10 |  |  |
| 20 |  | mem_load | t11 | A |  |  |
| 21 |  | print |  | t11 |  |  |
| 22 |  | mem_store | F1 | t11 |  |  |
| 23 |  | mem_store | F3 | t7 |  |  |
| 24 |  | mem_load | t12 | F1 |  |  |
| 25 |  | mem_load | t13 | F3 |  |  |
| 26 |  | binop | t14 | t12 | + | t13 |
| 27 |  | mem_store | A | t14 |  |  |
| 28 |  | mem_load | t15 | A |  |  |
| 29 |  | print |  | t15 |  |  |
| 30 |  | mem_store | F1 | t15 |  |  |
| 31 |  | mem_store | F3 | t11 |  |  |
| 32 |  | mem_load | t16 | F1 |  |  |
| 33 |  | mem_load | t17 | F3 |  |  |
| 34 |  | binop | t18 | t16 | + | t17 |
| 35 |  | mem_store | A | t18 |  |  |
| 36 |  | mem_load | t19 | A |  |  |
| 37 |  | print |  | t19 |  |  |
| 38 |  | mem_store | F1 | t19 |  |  |
| 39 |  | mem_store | F3 | t15 |  |  |
| 40 |  | mem_load | t20 | F1 |  |  |
| 41 |  | mem_load | t21 | F3 |  |  |
| 42 |  | binop | t22 | t20 | + | t21 |
| 43 |  | mem_store | A | t22 |  |  |
| 44 |  | mem_load | t23 | A |  |  |
| 45 |  | print |  | t23 |  |  |
| 46 |  | mem_store | F1 | t23 |  |  |
| 47 |  | mem_store | F3 | t19 |  |  |
| 48 |  | mem_load | t24 | F1 |  |  |
| 49 |  | mem_load | t25 | F3 |  |  |
| 50 |  | binop | t26 | t24 | + | t25 |
| 51 |  | mem_store | A | t26 |  |  |
| 52 |  | mem_load | t27 | A |  |  |
| 53 |  | print |  | t27 |  |  |
| 54 |  | mem_store | F1 | t27 |  |  |
| 55 |  | mem_store | F3 | t23 |  |  |
| 56 |  | mem_load | t28 | F1 |  |  |
| 57 |  | mem_load | t29 | F3 |  |  |
| 58 |  | binop | t30 | t28 | + | t29 |
| 59 |  | mem_store | A | t30 |  |  |
| 60 |  | mem_load | t31 | A |  |  |
| 61 |  | print |  | t31 |  |  |
| 62 |  | mem_store | F1 | t31 |  |  |
| 63 |  | mem_store | F3 | t27 |  |  |
| 64 |  | mem_load | t32 | F1 |  |  |
| 65 |  | mem_load | t33 | F3 |  |  |
| 66 |  | binop | t34 | t32 | + | t33 |
| 67 |  | mem_store | A | t34 |  |  |
| 68 |  | mem_load | t35 | A |  |  |
| 69 |  | print |  | t35 |  |  |
| 70 |  | mem_store | F1 | t35 |  |  |
| 71 |  | mem_store | F3 | t31 |  |  |
| 72 |  | mem_load | t36 | F1 |  |  |
| 73 |  | mem_load | t37 | F3 |  |  |
| 74 |  | binop | t38 | t36 | + | t37 |
| 75 |  | mem_store | A | t38 |  |  |
| 76 |  | mem_load | t39 | A |  |  |
| 77 |  | print |  | t39 |  |  |
| 78 |  | mem_store | F1 | t39 |  |  |
| 79 |  | mem_store | F3 | t35 |  |  |
| 80 |  | mem_load | t40 | F1 |  |  |
| 81 |  | mem_load | t41 | F3 |  |  |
| 82 |  | binop | t42 | t40 | + | t41 |
| 83 |  | mem_store | A | t42 |  |  |
| 84 |  | mem_load | t43 | A |  |  |
| 85 |  | print |  | t43 |  |  |
| 86 |  | mem_store | F1 | t43 |  |  |
| 87 |  | mem_store | F3 | t39 |  |  |
| 88 |  | mem_load | t44 | F1 |  |  |
| 89 |  | mem_load | t45 | F3 |  |  |
| 90 |  | binop | t46 | t44 | + | t45 |
| 91 |  | mem_store | A | t46 |  |  |
| 92 |  | mem_load | t47 | A |  |  |
| 93 |  | print |  | t47 |  |  |
| 94 |  | mem_store | F1 | t47 |  |  |
| 95 |  | mem_store | F3 | t43 |  |  |
| 96 |  | mem_load | t48 | F1 |  |  |
| 97 |  | mem_load | t49 | F3 |  |  |
| 98 |  | binop | t50 | t48 | + | t49 |
| 99 |  | mem_store | A | t50 |  |  |
| 100 |  | mem_load | t51 | A |  |  |
| 101 |  | print |  | t51 |  |  |
| 102 |  | mem_store | F1 | t51 |  |  |
| 103 |  | mem_store | F3 | t47 |  |  |
| 104 |  | mem_load | t52 | F1 |  |  |
| 105 |  | mem_load | t53 | F3 |  |  |
| 106 |  | binop | t54 | t52 | + | t53 |
| 107 |  | mem_store | A | t54 |  |  |
| 108 |  | mem_load | t55 | A |  |  |
| 109 |  | print |  | t55 |  |  |
| 110 |  | mem_store | F1 | t55 |  |  |
| 111 |  | mem_store | F3 | t51 |  |  |
| 112 |  | mem_load | t56 | F1 |  |  |
| 113 |  | mem_load | t57 | F3 |  |  |
| 114 |  | binop | t58 | t56 | + | t57 |
| 115 |  | mem_store | A | t58 |  |  |
| 116 |  | mem_load | t59 | A |  |  |
| 117 |  | print |  | t59 |  |  |
| 118 |  | mem_store | F1 | t59 |  |  |
| 119 |  | mem_store | F3 | t55 |  |  |
| 120 |  | mem_load | t60 | F1 |  |  |
| 121 |  | mem_load | t61 | F3 |  |  |
| 122 |  | binop | t62 | t60 | + | t61 |
| 123 |  | mem_store | A | t62 |  |  |
| 124 |  | mem_load | t63 | A |  |  |
| 125 |  | print |  | t63 |  |  |
| 126 |  | mem_store | F1 | t63 |  |  |
| 127 |  | mem_store | F3 | t59 |  |  |
| 128 |  | mem_load | t64 | F1 |  |  |
| 129 |  | mem_load | t65 | F3 |  |  |
| 130 |  | binop | t66 | t64 | + | t65 |
| 131 |  | mem_store | A | t66 |  |  |
| 132 |  | mem_load | t67 | A |  |  |
| 133 |  | print |  | t67 |  |  |
| 134 |  | mem_store | F1 | t67 |  |  |
| 135 |  | mem_store | F3 | t63 |  |  |
| 136 |  | mem_load | t68 | F1 |  |  |
| 137 |  | mem_load | t69 | F3 |  |  |
| 138 |  | binop | t70 | t68 | + | t69 |
| 139 |  | mem_store | A | t70 |  |  |
| 140 |  | mem_load | t71 | A |  |  |
| 141 |  | print |  | t71 |  |  |
| 142 |  | mem_store | F1 | t71 |  |  |
| 143 |  | mem_store | F3 | t67 |  |  |
| 144 |  | mem_load | t72 | F1 |  |  |
| 145 |  | mem_load | t73 | F3 |  |  |
| 146 |  | binop | t74 | t72 | + | t73 |
| 147 |  | mem_store | A | t74 |  |  |
| 148 |  | mem_load | t75 | A |  |  |
| 149 |  | print |  | t75 |  |  |
| 150 |  | mem_store | F1 | t75 |  |  |
| 151 |  | mem_store | F3 | t71 |  |  |
| 152 |  | mem_load | t76 | F1 |  |  |
| 153 |  | mem_load | t77 | F3 |  |  |
| 154 |  | binop | t78 | t76 | + | t77 |
| 155 |  | mem_store | A | t78 |  |  |
| 156 |  | mem_load | t79 | A |  |  |
| 157 |  | print |  | t79 |  |  |
| 158 |  | mem_store | F1 | t79 |  |  |
| 159 |  | mem_store | F3 | t75 |  |  |
| 160 |  | mem_load | t80 | F1 |  |  |
| 161 |  | mem_load | t81 | F3 |  |  |
| 162 |  | binop | t82 | t80 | + | t81 |
| 163 |  | mem_store | A | t82 |  |  |
| 164 |  | mem_load | t83 | A |  |  |
| 165 |  | print |  | t83 |  |  |
| 166 |  | mem_store | F1 | t83 |  |  |
| 167 |  | mem_store | F3 | t79 |  |  |
| 168 |  | mem_load | t84 | F1 |  |  |
| 169 |  | mem_load | t85 | F3 |  |  |
| 170 |  | binop | t86 | t84 | + | t85 |
| 171 |  | mem_store | A | t86 |  |  |
| 172 |  | mem_load | t87 | A |  |  |
| 173 |  | print |  | t87 |  |  |
| 174 |  | mem_store | F1 | t87 |  |  |
| 175 |  | mem_store | F3 | t83 |  |  |
| 176 |  | mem_load | t88 | F1 |  |  |
| 177 |  | mem_load | t89 | F3 |  |  |
| 178 |  | binop | t90 | t88 | + | t89 |
| 179 |  | mem_store | A | t90 |  |  |
| 180 |  | mem_load | t91 | A |  |  |
| 181 |  | print |  | t91 |  |  |
| 182 |  | mem_store | F1 | t91 |  |  |
| 183 |  | mem_store | F3 | t87 |  |  |
| 184 |  | mem_load | t92 | F1 |  |  |
| 185 |  | mem_load | t93 | F3 |  |  |
| 186 |  | binop | t94 | t92 | + | t93 |
| 187 |  | mem_store | A | t94 |  |  |
| 188 |  | mem_load | t95 | A |  |  |
| 189 |  | print |  | t95 |  |  |

## JSON original

```json
[
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "0.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t1",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "1.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t3",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "0.0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t4",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t5",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t6",
    "arg1": "t4",
    "arg2": "t5",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t6",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t7",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t7",
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
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t8",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t9",
    "arg1": "F3",
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
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t10",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t11",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t11",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t11",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t7",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t12",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t13",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t14",
    "arg1": "t12",
    "arg2": "t13",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t14",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t15",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t15",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t15",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t11",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t16",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t17",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t18",
    "arg1": "t16",
    "arg2": "t17",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t18",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t19",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t19",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t19",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t15",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t20",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t21",
    "arg1": "F3",
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
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t22",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t23",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t23",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t23",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t19",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t24",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t25",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t26",
    "arg1": "t24",
    "arg2": "t25",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t26",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t27",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t27",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t27",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t23",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t28",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t29",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t30",
    "arg1": "t28",
    "arg2": "t29",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t30",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t31",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t31",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t31",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t27",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t32",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t33",
    "arg1": "F3",
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
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t34",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t35",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t35",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t35",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t31",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t36",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t37",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t38",
    "arg1": "t36",
    "arg2": "t37",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t38",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t39",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t39",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t39",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t35",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t40",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t41",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t42",
    "arg1": "t40",
    "arg2": "t41",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t42",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t43",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t43",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t43",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t39",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t44",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t45",
    "arg1": "F3",
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
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t46",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t47",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t47",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t47",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t43",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t48",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t49",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t50",
    "arg1": "t48",
    "arg2": "t49",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t50",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t51",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t51",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t51",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t47",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t52",
    "arg1": "F1",
    "arg2": null,
    "label": null,
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
    "op": "binop",
    "dest": "t54",
    "arg1": "t52",
    "arg2": "t53",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t54",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t55",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t55",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t55",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t51",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t56",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t57",
    "arg1": "F3",
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
    "dest": "A",
    "arg1": "t58",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t59",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t59",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t59",
    "arg2": null,
    "label": null,
    "op_symbol": null
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
    "dest": "t60",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t61",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t62",
    "arg1": "t60",
    "arg2": "t61",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t62",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t63",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t63",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t63",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t59",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t64",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t65",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t66",
    "arg1": "t64",
    "arg2": "t65",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t66",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t67",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t67",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t67",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t63",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t68",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t69",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t70",
    "arg1": "t68",
    "arg2": "t69",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t70",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t71",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t71",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t71",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t67",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t72",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t73",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t74",
    "arg1": "t72",
    "arg2": "t73",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t74",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t75",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t75",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t75",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t71",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t76",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t77",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t78",
    "arg1": "t76",
    "arg2": "t77",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t78",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t79",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t79",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t79",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t75",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t80",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t81",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t82",
    "arg1": "t80",
    "arg2": "t81",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t82",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t83",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t83",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t83",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t79",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t84",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t85",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t86",
    "arg1": "t84",
    "arg2": "t85",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t86",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t87",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t87",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t87",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t83",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t88",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t89",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t90",
    "arg1": "t88",
    "arg2": "t89",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t90",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t91",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t91",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F1",
    "arg1": "t91",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "F3",
    "arg1": "t87",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t92",
    "arg1": "F1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t93",
    "arg1": "F3",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "binop",
    "dest": "t94",
    "arg1": "t92",
    "arg2": "t93",
    "label": null,
    "op_symbol": "+"
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t94",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_load",
    "dest": "t95",
    "arg1": "A",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "print",
    "dest": null,
    "arg1": "t95",
    "arg2": null,
    "label": null,
    "op_symbol": null
  }
]
```
