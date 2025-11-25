from lexical_analyzer.ler_arquivo import lerArquivo
from lexical_analyzer.parse_expressao import parseExpressao
from lexical_analyzer.executar_expressao import executar_expressao


def lexical_analysis(expressions_file):
    """
    Função principal que processa as expressões de um arquivo

    Args:
        expressions_file (str): Caminho para o arquivo contendo as expressões.
    """

    operations = lerArquivo(expressions_file)
    all_tokens = []

    for operation in operations:
        expression = parseExpressao(operation)
        all_tokens.append(expression)

    return all_tokens
