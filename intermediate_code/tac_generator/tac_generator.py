from intermediate_code.tac_generator.tac_builder import (
    TACBuilder,
    BinOpNode,
    ConstNode,
    MemRefNode,
    StoreNode,
    ResNode,
    WhileNode,
    IfNode,
    ForNode,
)


class TACGenerator:

    def __init__(self):
        self.temp_counter = 0
        self.label_counter = 0
        self.instruction = []
        self.line_results = {}

    def gerar_tac(self, program):
        builder = TACBuilder()

        for line in program["lines"]:
            line_number = line["line"]
            tokens = line["postfix"]

            root = builder.build_from_postfix(tokens)
            result_temp = self.generate_node(root, line_number)
            self.line_results[line_number] = result_temp
            if result_temp is not None and self.is_print_line(tokens):
                self.emit("print", arg1=result_temp)

        return self.instruction

    def is_print_line(self, tokens):
        if len(tokens) != 1:
            return False

        kind = tokens[0]["kind"]
        return kind in ("INT", "REAL", "REF")

    def generate_node(self, node, line_number):

        if isinstance(node, ConstNode):
            temp = self.new_temp()
            self.emit("assign", dest=temp, arg1=str(node.value))
            return temp

        if isinstance(node, MemRefNode):
            t = self.new_temp()
            self.emit("mem_load", dest=t, arg1=node.name)
            return t

        if isinstance(node, StoreNode):
            value_temp = self.generate_node(node.expr, line_number)
            self.emit("mem_store", dest=node.name, arg1=value_temp)
            return value_temp

        if isinstance(node, BinOpNode):
            left_temp = self.generate_node(node.left, line_number)
            right_temp = self.generate_node(node.right, line_number)
            t = self.new_temp()
            self.emit(
                "binop",
                dest=t,
                arg1=left_temp,
                arg2=right_temp,
                op_symbol=node.op,
            )
            return t

        if isinstance(node, ResNode):
            target_line = line_number - node.offset
            return self.line_results[target_line]

        if isinstance(node, WhileNode):
            self.gen_while(node, line_number)
            return None

        if isinstance(node, IfNode):
            return self.gen_if(node, line_number)

        if isinstance(node, ForNode):
            self.gen_for(node, line_number)
            return None

    def new_temp(self) -> str:
        name = f"t{self.temp_counter}"
        self.temp_counter += 1
        return name

    def emit(self, op, dest=None, arg1=None, arg2=None, label=None, op_symbol=None):
        self.instruction.append(
            {
                "op": op,
                "dest": dest,
                "arg1": arg1,
                "arg2": arg2,
                "label": label,
                "op_symbol": op_symbol,
            }
        )

    def gen_while(self, node, current_line):
        l_cond = self.new_label()
        l_end = self.new_label()

        self.emit("label", label=l_cond)

        cond_temp = self.generate_node(node.condition, current_line)
        self.emit("ifFalse", arg1=cond_temp, label=l_end)

        _ = self.generate_node(node.body, current_line)

        self.emit("goto", label=l_cond)

        self.emit("label", label=l_end)

    def gen_if(self, node, current_line):
        l_false = self.new_label()
        l_end = self.new_label()

        cond_temp = self.generate_node(node.cond, current_line)
        self.emit("ifFalse", arg1=cond_temp, label=l_false)

        then_temp = self.generate_node(node.then_expr, current_line)
        res_temp = self.new_temp()
        self.emit("copy", dest=res_temp, arg1=then_temp)

        self.emit("goto", label=l_end)

        self.emit("label", label=l_false)

        else_temp = self.generate_node(node.else_expr, current_line)
        self.emit("copy", dest=res_temp, arg1=else_temp)

        self.emit("label", label=l_end)

        return res_temp

    def new_label(self) -> str:
        name = f"L{self.label_counter}"
        self.label_counter += 1
        return name

    def gen_for(self, node: ForNode, current_line: int) -> None:

        l_cond = self.new_label()
        l_end = self.new_label()

        self.emit("label", label=l_cond)

        cond_temp = self.generate_node(node.cond, current_line)
        assert cond_temp is not None
        self.emit("ifFalse", arg1=cond_temp, label=l_end)

        _ = self.generate_node(node.body, current_line)

        _ = self.generate_node(node.step, current_line)

        self.emit("goto", label=l_cond)

        self.emit("label", label=l_end)
