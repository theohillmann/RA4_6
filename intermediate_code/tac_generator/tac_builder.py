class ConstNode:

    def __init__(self, value):
        self.value = value


class MemRefNode:
    def __init__(self, name):
        self.name = name


class StoreNode:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class BinOpNode:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class ResNode:
    def __init__(self, offset):
        self.offset = offset


class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class ForNode:
    def __init__(self, cond, body, step):
        self.cond = cond
        self.body = body
        self.step = step


class IfNode:
    def __init__(self, cond, then_expr, else_expr):
        self.cond = cond
        self.then_expr = then_expr
        self.else_expr = else_expr


class TACBuilder:

    def __init__(self):
        self.stack = []

    def build_from_postfix(self, tokens):
        self.stack = []

        for token in tokens:
            kind = token["kind"]

            if kind in ["INT", "REAL"]:
                self.treat_literal(token)

            elif kind == "REF":
                self.treat_reference(token)

            elif kind == "OP":
                self.treat_binop(token)

            elif kind == "STORE":
                self.treat_store(token)

            elif kind == "RES":
                self.treat_restore()

            elif kind == "WHILE":
                self.treat_while()

            elif kind == "IF":
                self.treat_if()

            elif kind == "FOR":
                self.treat_for()

            else:
                raise Exception(f"[TAC] Unknown token kind: {kind}")

        if len(self.stack) != 1:
            raise Exception(
                f"[TAC] Stack not empty after processing: {len(self.stack)}"
            )

        return self.stack.pop()

    def treat_literal(self, token):
        self.stack.append(ConstNode(token["value"]))

    def treat_reference(self, token):
        self.stack.append(MemRefNode(token["value"]))

    def treat_binop(self, token):
        right = self.stack.pop()
        left = self.stack.pop()
        self.stack.append(BinOpNode(token["value"], left, right))

    def treat_store(self, token):
        expr = self.stack.pop()
        self.stack.append(StoreNode(token["value"], expr))

    def treat_restore(self):
        offset = self.stack.pop()
        self.stack.append(ResNode(int(offset.value)))

    def treat_while(self):
        body = self.stack.pop()
        condition = self.stack.pop()
        self.stack.append(WhileNode(condition, body))

    def treat_if(self):
        else_expr = self.stack.pop()
        then_expr = self.stack.pop()
        cond = self.stack.pop()
        self.stack.append(IfNode(cond, then_expr, else_expr))

    def treat_for(self):
        step = self.stack.pop()
        body = self.stack.pop()
        cond = self.stack.pop()
        self.stack.append(ForNode(cond=cond, body=body, step=step))
