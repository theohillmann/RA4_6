import json
import argparse
from semantic_analyzer.main import semantic_analysis
from lexical_analyzer.lexical_analyzer import lexical_analysis
from syntactic_analyzer.main import main as syntactic_analysis
from intermediate_code.tac_generator.tac_generator import TACGenerator
from intermediate_code.tac_generator.format_tac import format_tac
from intermediate_code.tac_optimization.tac_optmization import TACOptimizer
from generate_assembly.generate_assembly import TACToAVRAssembly


DEFAULT_SAMPLE_FILE = "tests/fibonacci/fibonacci.txt"


def main(sample_file):
    sample_file = sample_file or DEFAULT_SAMPLE_FILE

    ### Lexical Analysis ###
    tokens = lexical_analysis(sample_file)
    for index, token in enumerate(tokens):
        if "Error" in token:
            print(f"File {sample_file}, expression {index}")
            print(f"    {token}")
            print()
            return

    ### Syntactic Analysis ###
    with open(sample_file, "r") as file:
        source_lines = [ln.strip() for ln in file if ln.strip()]

    syntactic_error_count = syntactic_analysis(
        sample_file, debug=False, source_lines=source_lines
    )
    if syntactic_error_count > 0:
        return

    ### Semantic Analysis ###
    semantic_ok = semantic_analysis(sample_file)
    if not semantic_ok:
        return

    ### intermediate code ###
    with open(f"{sample_file}_arvore_atribuida.json", "r") as file:
        attributed_tree = json.load(file)

    tac_generator = TACGenerator()
    tac_instructions = tac_generator.gerar_tac(attributed_tree)

    with open(f"{sample_file}_tac.json", "w") as file:
        json.dump(tac_instructions, file, indent=2)

    print("=== TAC ORIGINAL ===")
    for instr in tac_instructions:
        print(format_tac(instr))

    opt = TACOptimizer()
    tac_optimized = opt.optimize(tac_instructions)
    with open(f"{sample_file}_tac_optimized.json", "w") as file:
        json.dump(tac_optimized, file, indent=2)

    print("\n=== TAC OTIMIZADO ===")
    for instr in tac_optimized:
        print(format_tac(instr))

    asm_code = TACToAVRAssembly().convert(tac_optimized)
    with open("output.s", "w") as f:
        f.write(asm_code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run analyzer pipeline on a sample file."
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="sample_file",
        default=None,
        help=f"Path to file (default: {DEFAULT_SAMPLE_FILE})",
    )
    args = parser.parse_args()
    main(args.sample_file)
