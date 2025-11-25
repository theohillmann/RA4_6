def format_tac(instr):
    op = instr["op"]
    d = instr["dest"]
    a1 = instr["arg1"]
    a2 = instr["arg2"]
    lbl = instr["label"]
    sym = instr["op_symbol"]

    if op in ("assign", "copy"):
        return f"{d} = {a1}"

    if op == "binop":
        return f"{d} = {a1} {sym} {a2}"

    if op == "mem_load":
        return f"{d} = MEM[{a1}]"

    if op == "mem_store":
        return f"MEM[{d}] = {a1}"

    if op == "goto":
        return f"goto {lbl}"

    if op == "ifFalse":
        return f"ifFalse {a1} goto {lbl}"

    if op == "if":
        return f"if {a1} goto {lbl}"

    if op == "label":
        return f"{lbl}:"

    if op == "print":
        return f"print {a1}"

    return f"# {op} {d} {a1} {a2} {lbl}"
