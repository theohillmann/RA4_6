# Compilador

Este repositório contém uma pipeline de análise e geração de código para uma linguagem simples (analisador léxico, sintático e semântico), geração de código intermediário (TAC — Three Address Code), otimizações sobre o TAC e um gerador de Assembly AVR (ATmega328P / Arduino Uno) que produz `output.s`.

Este README explica o propósito do projeto, a estrutura dos arquivos, descreve detalhadamente cada otimização implementada no otimizador de TAC, o formato das instruções TAC usadas, e como rodar a pipeline e gerar/flashar o código em um Arduino.

Sumário
- Sobre o projeto
- Requisitos
- Estrutura do repositório
- Pipeline (passo a passo)
- Formato das instruções TAC
- Otimizações implementadas (detalhadas)
- Como rodar (exemplos de comandos)
- Arquivos gerados
- Limitações conhecidas e próximos passos
- Contato / Créditos

Sobre o projeto
----------------
O projeto implementa um fluxo clássico de compilador para uma linguagem de expressões/pequenas estruturas de controle:
1. Análise léxica
2. Análise sintática
3. Análise semântica
4. Geração de código intermediário em TAC
5. Otimizações sobre TAC
6. Geração de Assembly AVR (32-bit com escala fixa)

O gerador de assembly trabalha com números escalados (x100) para representar números com duas casas decimais usando inteiros de 32 bits.

Requisitos
-----------
- Python 3.8+ (desenvolvido com CPython 3.10, recomenda-se 3.10)
- Para montar/gerar .hex e enviar ao Arduino
  - avr-gcc
  - avr-binutils
  - avrdude
  - No macOS: instale via Homebrew: `brew install avr-gcc avrdude`

Estrutura principal do repositório
----------------------------------
(arquivos e pastas mais relevantes)

- `main.py` — script principal que encadeia todo o pipeline.
- `lexical_analyzer/` — analisador léxico e utilitários.
- `syntactic_analyzer/` — análise sintática (parser) e geração de árvores.
- `semantic_analyzer/` — checagens semânticas e atribuição de tipos/endereços.
- `intermediate_code/tac_generator/` — constrói TAC a partir da árvore (inclui `tac_builder.py`, `tac_generator.py` e `format_tac.py`).
- `intermediate_code/tac_optimization/tac_optmization.py` — otimizador de TAC (implementa várias transformações).
- `generate_assembly/generate_assembly.py` — converte TAC em Assembly AVR (ATmega328P) com suporte a operações, print e funções auxiliares (multiplicação/divisão escaladas, UART, impressão formatada).
- `tests/` — exemplos de entrada (por exemplo, `tests/fibonacci/fibonacci.txt`).

Pipeline (o que `main.py` faz)
------------------------------
- Executa análise léxica sobre o arquivo de entrada.
- Executa análise sintática e produz uma árvore sintática (arquivo `*_arvore_atribuida.json`).
- Executa análise semântica; se houver erros, a execução para.
- Gera TAC a partir da árvore e salva em `*_tac.json`.
- Executa o otimizador e salva o TAC otimizado em `*_tac_optimized.json`.
- Gera `output.s` com o Assembly AVR a partir do TAC otimizado.

Formato das instruções TAC
--------------------------
Cada instrução TAC é um dicionário com as chaves:
- `op`: operação (string) — ex.: `assign`, `binop`, `mem_store`, `mem_load`, `print`, `label`, `goto`, `ifFalse`, `copy`.
- `dest`: destino (nome de variável / temporário) ou `None`.
- `arg1`: primeiro argumento (nome de variável, temporário ou literal) ou `None`.
- `arg2`: segundo argumento (para `binop`) ou `None`.
- `label`: nome do rótulo (para `label`, `goto`, `ifFalse`) ou `None`.
- `op_symbol`: operador textual para `binop` (ex.: `+`, `-`, `*`, `/`, `|` (divisão real), `%`, `<`, `>`, `<=`, `>=`, `==`, `!=`).

Exemplos legíveis (formatados por `format_tac.py`):
- `t0 = 2` (assign)
- `t1 = t0 + t2` (binop)
- `MEM[x] = t3` (mem_store)
- `t4 = MEM[x]` (mem_load)
- `L0:` (label)
- `goto L1` (goto)
- `ifFalse t5 goto L2` (condicional)
- `print t7` (print)

O gerador de Assembly espera valores numéricos representados como literais (strings que podem ser convertidas para float) ou nomes de variáveis temporárias.

Otimizações implementadas
--------------------------
O arquivo `intermediate_code/tac_optimization/tac_optmization.py` implementa um otimizador em várias fases que é executado iterativamente até fixpoint (ou máximo de 10 iterações). As transformações aplicadas são:

1) Constant Folding (dobramento de constantes)
- O que faz: avalia operações binárias (`binop`) cujos dois operandos são constantes numéricas detectadas em tempo de compilação e substitui a operação por um `assign` com o resultado.
- Exemplo: `t1 = 2 + 3` → `t1 = 5`.
- Observações: lida com operadores aritméticos (+, -, *, /, %, ^) e comparações (>, <, >=, <=, ==, !=). Para divisões por zero, evita dobrar (retorna None e mantém a operação original).

2) Constant Propagation (propagação de constantes)
- O que faz: identifica `assign` onde o `arg1` é uma constante e propaga esse valor para usos futuros substituindo ocorrências do identificador por seu valor literal.
- Exemplo: `a = 5` … `b = a` → `b = 5`.
- Observações: a propagação é simples e reinicializada em cada chamada do método (não é globalmente interprocedural). Propaga apenas literais simples detectáveis como floats.

3) Simplificação de branches com condição conhecida
- O que faz: para instruções `ifFalse`, se a condição é conhecida em tempo de compilação: 
  - Se cond == 0 → converte `ifFalse cond L` em `goto L` (sempre pula).
  - Se cond != 0 → remove o `ifFalse` (nunca pula).
- Exemplo: `ifFalse 0 goto L` → `goto L`.
- Observações: isso pode expor código inalcançável que será então removido pela próxima fase.

4) Remoção de código inalcançável após `goto`
- O que faz: quando encontra um `goto`, remove as instruções seguintes até o próximo rótulo (`label`), pois esse bloco nunca será executado diretamente após o `goto`.
- Exemplo: `goto L; x = 2; y = 3; L:` → `x = 2; y = 3;` removidos (dependendo de rótulos usados).
- Observações: implementado de forma linear, detectando rótulos e pulando até o próximo rótulo.

5) Dead Code Elimination (eliminação de código morto)
- O que faz: varre o TAC de trás para frente para descobrir quais destinos (temporários/variáveis) são efetivamente usados por operações importantes (print, mem_store, ifFalse, goto, label, mem_load etc.). Remove atribuições cujo destino não é usado.
- Exemplo: `t1 = ...; t2 = t1 + 1` se `t2` não for usado em efeito colateral, a atribuição para `t1` pode ser removida.
- Observações: considera `mem_load` sempre preservada; mantém rótulos que são alvo de `goto`/`ifFalse`.

6) Remoção de saltos redundantes (`_remove_redundant_jumps`)
- O que faz: detecta `goto L` que apontam para o rótulo imediatamente seguinte no fluxo e remove esses saltos redundantes.
- Exemplo: `goto L1; L1:` → o `goto` é removido.
- Observações: compara posições de rótulos e a instrução seguinte para decidir se é redundante.

Fluxo iterativo
- O otimizador aplica essas fases em loop até que não haja mais mudanças (fixpoint) ou até 10 iterações. Isso permite que transformações como propagação+folding+eliminação sejam compostas e alcancem mais oportunidades de otimização.

Formato resultante / S-expression
- O otimizador também expõe `to_s_expression(tac)` para imprimir o TAC em uma forma tipo S-expression (útil para debugging/visualização).

Como rodar
----------
A seguir, passos básicos para executar a pipeline com Python.

1) Rodar a pipeline completa (usa arquivo de teste por padrão)

```bash
# na raiz do repositório
python3 main.py
```

2) Rodar com arquivo específico

```bash
python3 main.py -f tests/fibonacci/fibonacci.txt
```

3) Saída esperada da execução
- Se tudo ocorrer bem, serão criados/atualizados os arquivos:
  - `{input}_arvore_atribuida.json` — árvore sintática depois da análise semântica.
  - `{input}_tac.json` — TAC gerado (antes da otimização).
  - `{input}_tac_optimized.json` — TAC após otimizacões.
  - `output.s` — Assembly AVR gerado a partir do TAC otimizado.
- O console também imprime o TAC original e o TAC otimizado (usando `format_tac`).

4) Montar `output.s` em `.hex` e enviar para Arduino

Observação: os comandos abaixo pressupõem que você tenha `avr-gcc`, `avr-objcopy` e `avrdude` instalados e conheça a porta serial do seu Arduino. No macOS a porta costuma ser `/dev/tty.usbmodem...` ou `/dev/tty.usbserial...`.

```bash
# exemplo: gerar ELF, gerar HEX e enviar (ajuste a MCU e a porta conforme necessário)
avr-gcc -mmcu=atmega328p -Os -o main.elf output.s
avr-objcopy -O ihex -R .eeprom main.elf main.hex
# enviar para Arduino (substitua /dev/tty.usbmodem14101 pela sua porta e -c/baud conforme seu programador)
avrdude -v -p m328p -c arduino -P /dev/tty.usbmodemXXXX -b 115200 -D -U flash:w:main.hex:i
```

Se você não quiser fazer upload, basta inspecionar `output.s` e os arquivos JSON gerados para entender o que o compilador fez.

Exemplo rápido com o arquivo de teste Fibonacci

```bash
python3 main.py -f tests/fibonacci/fibonacci.txt
# irá gerar: tests/fibonacci/fibonacci.txt_tac.json
#                tests/fibonacci/fibonacci.txt_tac_optimized.json
#                tests/fibonacci/fibonacci.txt_arvore_atribuida.json
#                output.s
```

Arquivos gerados e propósito
- `*_arvore_atribuida.json`: representa a árvore de análise sintática com informações semânticas (tipos/endereços). É a entrada para o gerador de TAC.
- `*_tac.json`: TAC não-otimizado (transcrição direta do algoritmo em três endereços temporais).
- `*_tac_optimized.json`: TAC otimizado.
- `output.s`: Assembly AVR gerado.

Limitações conhecidas e cuidados
- O otimizador de constantes e propagação é local e relativamente simples — não lida com aliasing complexo, efeitos colaterais externos, nem com Análise de Fluxo de Dados interprocedural.
- O gerador de Assembly é específico para ATmega328P (Arduino Uno) e usa registradores e convenções específicas.

Theo Hillmann Luiz Coelho - 2025 RA4 grupo 6



