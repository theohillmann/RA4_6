"""
Compilador RPN - Fase 3: Analisador Semântico
Instituição: PUC PR
Disciplina: Linguagens Formais e Compiladores
Aluno: Theo Hillmann Luiz Coelho
Grupo Canvas: RA3_6
Data: 2025/2
"""

import re
import json
from .define_grammar.define_grammar import definirGramaticaAtributos
from .semantic_analyzer.analyzer import analisarSemantica
from .semantic_analyzer.semantic_memory import analisarSemanticaMemoria
from .semantic_analyzer.semantic_control import analisarSemanticaControle
from .define_grammar.utils.symbols import SymbolTable
from .semantic_analyzer.attribute_tree import (
    salvar_arquivos_saida,
    gerar_arvore_atribuida,
)


# FILE_PATH = args.FILE_PATH


def semantic_analysis(file_path):
    grammar = definirGramaticaAtributos()
    st = grammar["symbol_table"]
    table = SymbolTable()

    with open(file_path.replace("txt", "json"), "r") as file:
        ast = json.load(file)

    types, errors, anot = analisarSemantica(ast, grammar)

    errors += analisarSemanticaMemoria(ast, table)
    errors += analisarSemanticaControle(ast, table)

    arvore_atribuida = gerar_arvore_atribuida(anot, table)
    prefixo = file_path.replace(".json", "")

    if errors:
        pattern = r"ERRO SEMÂNTICO \[Linha (\d+)\]: (.+)"
        for erro in errors:
            match = re.search(pattern, erro)
            line = match.group(1)
            message = match.group(2)
            print(f"{file_path}, expression {line}")
            print(f"    Error: {message}\n")
            return False

    salvar_arquivos_saida(arvore_atribuida, prefixo=prefixo)
    return True
