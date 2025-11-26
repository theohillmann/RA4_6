# TAC: fibonacci.txt_tac

## Instruções formatadas

```text
  0: t0 = 0
  1: MEM[A] = t0
  2: t1 = MEM[A]
  3: print t1
  4: t2 = 1
  5: MEM[A] = t2
  6: t3 = MEM[A]
  7: print t3
  8: MEM[F1] = t3
  9: MEM[F3] = t0
 10: t4 = MEM[F1]
 11: t5 = MEM[F3]
 12: t6 = t4 + t5
 13: MEM[A] = t6
 14: t7 = MEM[A]
 15: print t7
 16: MEM[F1] = t7
 17: MEM[F3] = t3
 18: t8 = MEM[F1]
 19: t9 = MEM[F3]
 20: t10 = t8 + t9
 21: MEM[A] = t10
 22: t11 = MEM[A]
 23: print t11
 24: MEM[F1] = t11
 25: MEM[F3] = t7
 26: t12 = MEM[F1]
 27: t13 = MEM[F3]
 28: t14 = t12 + t13
 29: MEM[A] = t14
 30: t15 = MEM[A]
 31: print t15
 32: MEM[F1] = t15
 33: MEM[F3] = t11
 34: t16 = MEM[F1]
 35: t17 = MEM[F3]
 36: t18 = t16 + t17
 37: MEM[A] = t18
 38: t19 = MEM[A]
 39: print t19
 40: MEM[F1] = t19
 41: MEM[F3] = t15
 42: t20 = MEM[F1]
 43: t21 = MEM[F3]
 44: t22 = t20 + t21
 45: MEM[A] = t22
 46: t23 = MEM[A]
 47: print t23
 48: MEM[F1] = t23
 49: MEM[F3] = t19
 50: t24 = MEM[F1]
 51: t25 = MEM[F3]
 52: t26 = t24 + t25
 53: MEM[A] = t26
 54: t27 = MEM[A]
 55: print t27
 56: MEM[F1] = t27
 57: MEM[F3] = t23
 58: t28 = MEM[F1]
 59: t29 = MEM[F3]
 60: t30 = t28 + t29
 61: MEM[A] = t30
 62: t31 = MEM[A]
 63: print t31
 64: MEM[F1] = t31
 65: MEM[F3] = t27
 66: t32 = MEM[F1]
 67: t33 = MEM[F3]
 68: t34 = t32 + t33
 69: MEM[A] = t34
 70: t35 = MEM[A]
 71: print t35
 72: MEM[F1] = t35
 73: MEM[F3] = t31
 74: t36 = MEM[F1]
 75: t37 = MEM[F3]
 76: t38 = t36 + t37
 77: MEM[A] = t38
 78: t39 = MEM[A]
 79: print t39
 80: MEM[F1] = t39
 81: MEM[F3] = t35
 82: t40 = MEM[F1]
 83: t41 = MEM[F3]
 84: t42 = t40 + t41
 85: MEM[A] = t42
 86: t43 = MEM[A]
 87: print t43
 88: MEM[F1] = t43
 89: MEM[F3] = t39
 90: t44 = MEM[F1]
 91: t45 = MEM[F3]
 92: t46 = t44 + t45
 93: MEM[A] = t46
 94: t47 = MEM[A]
 95: print t47
 96: MEM[F1] = t47
 97: MEM[F3] = t43
 98: t48 = MEM[F1]
 99: t49 = MEM[F3]
100: t50 = t48 + t49
101: MEM[A] = t50
102: t51 = MEM[A]
103: print t51
104: MEM[F1] = t51
105: MEM[F3] = t47
106: t52 = MEM[F1]
107: t53 = MEM[F3]
108: t54 = t52 + t53
109: MEM[A] = t54
110: t55 = MEM[A]
111: print t55
112: MEM[F1] = t55
113: MEM[F3] = t51
114: t56 = MEM[F1]
115: t57 = MEM[F3]
116: t58 = t56 + t57
117: MEM[A] = t58
118: t59 = MEM[A]
119: print t59
120: MEM[F1] = t59
121: MEM[F3] = t55
122: t60 = MEM[F1]
123: t61 = MEM[F3]
124: t62 = t60 + t61
125: MEM[A] = t62
126: t63 = MEM[A]
127: print t63
128: MEM[F1] = t63
129: MEM[F3] = t59
130: t64 = MEM[F1]
131: t65 = MEM[F3]
132: t66 = t64 + t65
133: MEM[A] = t66
134: t67 = MEM[A]
135: print t67
136: MEM[F1] = t67
137: MEM[F3] = t63
138: t68 = MEM[F1]
139: t69 = MEM[F3]
140: t70 = t68 + t69
141: MEM[A] = t70
142: t71 = MEM[A]
143: print t71
144: MEM[F1] = t71
145: MEM[F3] = t67
146: t72 = MEM[F1]
147: t73 = MEM[F3]
148: t74 = t72 + t73
149: MEM[A] = t74
150: t75 = MEM[A]
151: print t75
152: MEM[F1] = t75
153: MEM[F3] = t71
154: t76 = MEM[F1]
155: t77 = MEM[F3]
156: t78 = t76 + t77
157: MEM[A] = t78
158: t79 = MEM[A]
159: print t79
160: MEM[F1] = t79
161: MEM[F3] = t75
162: t80 = MEM[F1]
163: t81 = MEM[F3]
164: t82 = t80 + t81
165: MEM[A] = t82
166: t83 = MEM[A]
167: print t83
168: MEM[F1] = t83
169: MEM[F3] = t79
170: t84 = MEM[F1]
171: t85 = MEM[F3]
172: t86 = t84 + t85
173: MEM[A] = t86
174: t87 = MEM[A]
175: print t87
176: MEM[F1] = t87
177: MEM[F3] = t83
178: t88 = MEM[F1]
179: t89 = MEM[F3]
180: t90 = t88 + t89
181: MEM[A] = t90
182: t91 = MEM[A]
183: print t91
184: MEM[F1] = t91
185: MEM[F3] = t87
186: t92 = MEM[F1]
187: t93 = MEM[F3]
188: t94 = t92 + t93
189: MEM[A] = t94
190: t95 = MEM[A]
191: print t95
```

## Tabela de instruções

| # | Label | Op | Dest | Arg1 | OpSymbol | Arg2 |
|---|-------|----|------|------|----------|------|
| 0 |  | assign | t0 | 0 |  |  |
| 1 |  | mem_store | A | t0 |  |  |
| 2 |  | mem_load | t1 | A |  |  |
| 3 |  | print |  | t1 |  |  |
| 4 |  | assign | t2 | 1 |  |  |
| 5 |  | mem_store | A | t2 |  |  |
| 6 |  | mem_load | t3 | A |  |  |
| 7 |  | print |  | t3 |  |  |
| 8 |  | mem_store | F1 | t3 |  |  |
| 9 |  | mem_store | F3 | t0 |  |  |
| 10 |  | mem_load | t4 | F1 |  |  |
| 11 |  | mem_load | t5 | F3 |  |  |
| 12 |  | binop | t6 | t4 | + | t5 |
| 13 |  | mem_store | A | t6 |  |  |
| 14 |  | mem_load | t7 | A |  |  |
| 15 |  | print |  | t7 |  |  |
| 16 |  | mem_store | F1 | t7 |  |  |
| 17 |  | mem_store | F3 | t3 |  |  |
| 18 |  | mem_load | t8 | F1 |  |  |
| 19 |  | mem_load | t9 | F3 |  |  |
| 20 |  | binop | t10 | t8 | + | t9 |
| 21 |  | mem_store | A | t10 |  |  |
| 22 |  | mem_load | t11 | A |  |  |
| 23 |  | print |  | t11 |  |  |
| 24 |  | mem_store | F1 | t11 |  |  |
| 25 |  | mem_store | F3 | t7 |  |  |
| 26 |  | mem_load | t12 | F1 |  |  |
| 27 |  | mem_load | t13 | F3 |  |  |
| 28 |  | binop | t14 | t12 | + | t13 |
| 29 |  | mem_store | A | t14 |  |  |
| 30 |  | mem_load | t15 | A |  |  |
| 31 |  | print |  | t15 |  |  |
| 32 |  | mem_store | F1 | t15 |  |  |
| 33 |  | mem_store | F3 | t11 |  |  |
| 34 |  | mem_load | t16 | F1 |  |  |
| 35 |  | mem_load | t17 | F3 |  |  |
| 36 |  | binop | t18 | t16 | + | t17 |
| 37 |  | mem_store | A | t18 |  |  |
| 38 |  | mem_load | t19 | A |  |  |
| 39 |  | print |  | t19 |  |  |
| 40 |  | mem_store | F1 | t19 |  |  |
| 41 |  | mem_store | F3 | t15 |  |  |
| 42 |  | mem_load | t20 | F1 |  |  |
| 43 |  | mem_load | t21 | F3 |  |  |
| 44 |  | binop | t22 | t20 | + | t21 |
| 45 |  | mem_store | A | t22 |  |  |
| 46 |  | mem_load | t23 | A |  |  |
| 47 |  | print |  | t23 |  |  |
| 48 |  | mem_store | F1 | t23 |  |  |
| 49 |  | mem_store | F3 | t19 |  |  |
| 50 |  | mem_load | t24 | F1 |  |  |
| 51 |  | mem_load | t25 | F3 |  |  |
| 52 |  | binop | t26 | t24 | + | t25 |
| 53 |  | mem_store | A | t26 |  |  |
| 54 |  | mem_load | t27 | A |  |  |
| 55 |  | print |  | t27 |  |  |
| 56 |  | mem_store | F1 | t27 |  |  |
| 57 |  | mem_store | F3 | t23 |  |  |
| 58 |  | mem_load | t28 | F1 |  |  |
| 59 |  | mem_load | t29 | F3 |  |  |
| 60 |  | binop | t30 | t28 | + | t29 |
| 61 |  | mem_store | A | t30 |  |  |
| 62 |  | mem_load | t31 | A |  |  |
| 63 |  | print |  | t31 |  |  |
| 64 |  | mem_store | F1 | t31 |  |  |
| 65 |  | mem_store | F3 | t27 |  |  |
| 66 |  | mem_load | t32 | F1 |  |  |
| 67 |  | mem_load | t33 | F3 |  |  |
| 68 |  | binop | t34 | t32 | + | t33 |
| 69 |  | mem_store | A | t34 |  |  |
| 70 |  | mem_load | t35 | A |  |  |
| 71 |  | print |  | t35 |  |  |
| 72 |  | mem_store | F1 | t35 |  |  |
| 73 |  | mem_store | F3 | t31 |  |  |
| 74 |  | mem_load | t36 | F1 |  |  |
| 75 |  | mem_load | t37 | F3 |  |  |
| 76 |  | binop | t38 | t36 | + | t37 |
| 77 |  | mem_store | A | t38 |  |  |
| 78 |  | mem_load | t39 | A |  |  |
| 79 |  | print |  | t39 |  |  |
| 80 |  | mem_store | F1 | t39 |  |  |
| 81 |  | mem_store | F3 | t35 |  |  |
| 82 |  | mem_load | t40 | F1 |  |  |
| 83 |  | mem_load | t41 | F3 |  |  |
| 84 |  | binop | t42 | t40 | + | t41 |
| 85 |  | mem_store | A | t42 |  |  |
| 86 |  | mem_load | t43 | A |  |  |
| 87 |  | print |  | t43 |  |  |
| 88 |  | mem_store | F1 | t43 |  |  |
| 89 |  | mem_store | F3 | t39 |  |  |
| 90 |  | mem_load | t44 | F1 |  |  |
| 91 |  | mem_load | t45 | F3 |  |  |
| 92 |  | binop | t46 | t44 | + | t45 |
| 93 |  | mem_store | A | t46 |  |  |
| 94 |  | mem_load | t47 | A |  |  |
| 95 |  | print |  | t47 |  |  |
| 96 |  | mem_store | F1 | t47 |  |  |
| 97 |  | mem_store | F3 | t43 |  |  |
| 98 |  | mem_load | t48 | F1 |  |  |
| 99 |  | mem_load | t49 | F3 |  |  |
| 100 |  | binop | t50 | t48 | + | t49 |
| 101 |  | mem_store | A | t50 |  |  |
| 102 |  | mem_load | t51 | A |  |  |
| 103 |  | print |  | t51 |  |  |
| 104 |  | mem_store | F1 | t51 |  |  |
| 105 |  | mem_store | F3 | t47 |  |  |
| 106 |  | mem_load | t52 | F1 |  |  |
| 107 |  | mem_load | t53 | F3 |  |  |
| 108 |  | binop | t54 | t52 | + | t53 |
| 109 |  | mem_store | A | t54 |  |  |
| 110 |  | mem_load | t55 | A |  |  |
| 111 |  | print |  | t55 |  |  |
| 112 |  | mem_store | F1 | t55 |  |  |
| 113 |  | mem_store | F3 | t51 |  |  |
| 114 |  | mem_load | t56 | F1 |  |  |
| 115 |  | mem_load | t57 | F3 |  |  |
| 116 |  | binop | t58 | t56 | + | t57 |
| 117 |  | mem_store | A | t58 |  |  |
| 118 |  | mem_load | t59 | A |  |  |
| 119 |  | print |  | t59 |  |  |
| 120 |  | mem_store | F1 | t59 |  |  |
| 121 |  | mem_store | F3 | t55 |  |  |
| 122 |  | mem_load | t60 | F1 |  |  |
| 123 |  | mem_load | t61 | F3 |  |  |
| 124 |  | binop | t62 | t60 | + | t61 |
| 125 |  | mem_store | A | t62 |  |  |
| 126 |  | mem_load | t63 | A |  |  |
| 127 |  | print |  | t63 |  |  |
| 128 |  | mem_store | F1 | t63 |  |  |
| 129 |  | mem_store | F3 | t59 |  |  |
| 130 |  | mem_load | t64 | F1 |  |  |
| 131 |  | mem_load | t65 | F3 |  |  |
| 132 |  | binop | t66 | t64 | + | t65 |
| 133 |  | mem_store | A | t66 |  |  |
| 134 |  | mem_load | t67 | A |  |  |
| 135 |  | print |  | t67 |  |  |
| 136 |  | mem_store | F1 | t67 |  |  |
| 137 |  | mem_store | F3 | t63 |  |  |
| 138 |  | mem_load | t68 | F1 |  |  |
| 139 |  | mem_load | t69 | F3 |  |  |
| 140 |  | binop | t70 | t68 | + | t69 |
| 141 |  | mem_store | A | t70 |  |  |
| 142 |  | mem_load | t71 | A |  |  |
| 143 |  | print |  | t71 |  |  |
| 144 |  | mem_store | F1 | t71 |  |  |
| 145 |  | mem_store | F3 | t67 |  |  |
| 146 |  | mem_load | t72 | F1 |  |  |
| 147 |  | mem_load | t73 | F3 |  |  |
| 148 |  | binop | t74 | t72 | + | t73 |
| 149 |  | mem_store | A | t74 |  |  |
| 150 |  | mem_load | t75 | A |  |  |
| 151 |  | print |  | t75 |  |  |
| 152 |  | mem_store | F1 | t75 |  |  |
| 153 |  | mem_store | F3 | t71 |  |  |
| 154 |  | mem_load | t76 | F1 |  |  |
| 155 |  | mem_load | t77 | F3 |  |  |
| 156 |  | binop | t78 | t76 | + | t77 |
| 157 |  | mem_store | A | t78 |  |  |
| 158 |  | mem_load | t79 | A |  |  |
| 159 |  | print |  | t79 |  |  |
| 160 |  | mem_store | F1 | t79 |  |  |
| 161 |  | mem_store | F3 | t75 |  |  |
| 162 |  | mem_load | t80 | F1 |  |  |
| 163 |  | mem_load | t81 | F3 |  |  |
| 164 |  | binop | t82 | t80 | + | t81 |
| 165 |  | mem_store | A | t82 |  |  |
| 166 |  | mem_load | t83 | A |  |  |
| 167 |  | print |  | t83 |  |  |
| 168 |  | mem_store | F1 | t83 |  |  |
| 169 |  | mem_store | F3 | t79 |  |  |
| 170 |  | mem_load | t84 | F1 |  |  |
| 171 |  | mem_load | t85 | F3 |  |  |
| 172 |  | binop | t86 | t84 | + | t85 |
| 173 |  | mem_store | A | t86 |  |  |
| 174 |  | mem_load | t87 | A |  |  |
| 175 |  | print |  | t87 |  |  |
| 176 |  | mem_store | F1 | t87 |  |  |
| 177 |  | mem_store | F3 | t83 |  |  |
| 178 |  | mem_load | t88 | F1 |  |  |
| 179 |  | mem_load | t89 | F3 |  |  |
| 180 |  | binop | t90 | t88 | + | t89 |
| 181 |  | mem_store | A | t90 |  |  |
| 182 |  | mem_load | t91 | A |  |  |
| 183 |  | print |  | t91 |  |  |
| 184 |  | mem_store | F1 | t91 |  |  |
| 185 |  | mem_store | F3 | t87 |  |  |
| 186 |  | mem_load | t92 | F1 |  |  |
| 187 |  | mem_load | t93 | F3 |  |  |
| 188 |  | binop | t94 | t92 | + | t93 |
| 189 |  | mem_store | A | t94 |  |  |
| 190 |  | mem_load | t95 | A |  |  |
| 191 |  | print |  | t95 |  |  |

## JSON original

```json
[
  {
    "op": "assign",
    "dest": "t0",
    "arg1": "0",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t0",
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
    "op": "assign",
    "dest": "t2",
    "arg1": "1",
    "arg2": null,
    "label": null,
    "op_symbol": null
  },
  {
    "op": "mem_store",
    "dest": "A",
    "arg1": "t2",
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
    "arg1": "t0",
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
