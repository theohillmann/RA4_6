import os
import json


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


def tac_to_markdown(tac, filename):

    if not filename.lower().endswith(".md"):
        filename = filename + ".md"

    base_name = os.path.splitext(os.path.basename(filename))[0]

    lines = []

    # Título
    lines.append(f"# TAC: {base_name}")
    lines.append("")
    lines.append("## Instruções formatadas")
    lines.append("")
    lines.append("```text")
    for i, instr in enumerate(tac):
        pretty = format_tac(instr)
        lines.append(f"{i:>3}: {pretty}")
    lines.append("```")
    lines.append("")

    # Tabela
    lines.append("## Tabela de instruções")
    lines.append("")
    lines.append("| # | Label | Op | Dest | Arg1 | OpSymbol | Arg2 |")
    lines.append("|---|-------|----|------|------|----------|------|")
    for i, instr in enumerate(tac):
        op = instr.get("op") or ""
        dest = instr.get("dest") or ""
        arg1 = instr.get("arg1") or ""
        arg2 = instr.get("arg2") or ""
        label = instr.get("label") or ""
        op_symbol = instr.get("op_symbol") or ""
        lines.append(
            f"| {i} | {label} | {op} | {dest} | {arg1} | {op_symbol} | {arg2} |"
        )
    lines.append("")

    # JSON original
    lines.append("## JSON original")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(tac, indent=2, ensure_ascii=False))
    lines.append("```")
    lines.append("")

    markdown_content = "\n".join(lines)

    # Salva o arquivo
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    return filename
