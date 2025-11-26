# Avaliação do Projeto - Geração de Código Intermediário e Assembly

## Informações do Projeto
- **Grupo**: RA4 Grupo 6
- **Repositório**: theohillmann/RA4_6
- **Aluno**: Theo Hillmann Luiz Coelho
- **Linguagem**: Python 3.x

---

## 1. Funcionalidades do Compilador (70%)

### 1.1. Geração de TAC (Three Address Code)

#### ✅ Implementação Correta da Geração de TAC - **ATENDIDO**

O projeto implementa um gerador de TAC completo através das seguintes classes e módulos:
- `intermediate_code/tac_generator/tac_generator.py` - Classe `TACGenerator`
- `intermediate_code/tac_generator/tac_builder.py` - Estruturas auxiliares
- `intermediate_code/tac_generator/format_tac.py` - Formatação e exportação

**Formatos de instrução implementados:**
| Tipo | Formato | Exemplo |
|------|---------|---------|
| Atribuição | `assign` | `t0 = 8` |
| Operação Binária | `binop` | `t1 = a + b` |
| Armazenamento em Memória | `mem_store` | `MEM[N] = t0` |
| Leitura de Memória | `mem_load` | `t1 = MEM[N]` |
| Rótulo | `label` | `L0:` |
| Salto | `goto` | `goto L1` |
| Salto Condicional | `ifFalse` | `ifFalse t5 goto L1` |
| Impressão | `print` | `print t12` |

**Convenção de nomenclatura:**
- Variáveis temporárias: `t0`, `t1`, `t2`, ...
- Rótulos: `L0`, `L1`, `L2`, ...

#### ✅ Geração de TAC para Operações Aritméticas - **ATENDIDO**

Operadores suportados:
- ✅ Adição (`+`)
- ✅ Subtração (`-`)
- ✅ Multiplicação (`*`)
- ✅ Divisão Real (`|`)
- ✅ Divisão Inteira (`/`)
- ✅ Resto (`%`)
- ✅ Potenciação (`^`)

**Evidência** - Arquivo `factorial.txt_tac.md`:
```
t8 = t6 * t7      ; multiplicação
t11 = t9 + t10    ; adição
```

**Evidência** - Arquivo `taylor.txt_tac.md`:
```
t4 = t2 ^ t3      ; potenciação (0.5^2)
t19 = t17 | t18   ; divisão real
```

#### ✅ Geração de TAC para Estruturas de Controle - **ATENDIDO**

**Laços de repetição (for):**
```
L0:
t3 = MEM[I]
t4 = MEM[N]
t5 = t3 <= t4           ; condição
ifFalse t5 goto L1      ; saída do laço se falso
...
goto L0                  ; volta ao início
L1:
```

**Operadores relacionais implementados:**
- ✅ Maior que (`>`)
- ✅ Menor que (`<`)
- ✅ Maior ou igual (`>=`)
- ✅ Menor ou igual (`<=`)
- ✅ Igual (`==`)
- ✅ Diferente (`!=`)

---

### 1.2. Otimizações de Código

#### ✅ Pelo menos 3 técnicas de otimização implementadas e documentadas - **ATENDIDO**

O arquivo `intermediate_code/tac_optimization/tac_optmization.py` implementa **6 técnicas de otimização**:

#### 1. Constant Folding (Dobramento de Constantes)
**Descrição**: Avalia expressões constantes em tempo de compilação.

**Antes:**
```
t2 = 0.5
t3 = 2
t4 = t2 ^ t3
```

**Depois:**
```
MEM[POT1] = 0.25
```

**Evidência**: Linhas 47-80 do arquivo `tac_optmization.py`

#### 2. Constant Propagation (Propagação de Constantes)
**Descrição**: Propaga valores constantes através do código, substituindo variáveis por seus valores literais.

**Antes:**
```
t0 = 8
MEM[N] = t0
```

**Depois:**
```
MEM[N] = 8.0
```

**Evidência**: Linhas 82-105 do arquivo `tac_optmization.py`

#### 3. Dead Code Elimination (Eliminação de Código Morto)
**Descrição**: Remove código que não afeta o resultado do programa.

**Impacto**: No arquivo `taylor.txt`, instruções de atribuição intermediárias desnecessárias são eliminadas.

**Evidência**: Linhas 175-224 do arquivo `tac_optmization.py`

#### 4. Eliminação de Saltos Redundantes
**Descrição**: Remove saltos para a próxima instrução ou para rótulos não utilizados.

**Evidência**: Linhas 226-253 do arquivo `tac_optmization.py`

#### 5. Simplificação de Branches com Condição Conhecida
**Descrição**: Simplifica branches quando a condição é conhecida em tempo de compilação.

**Evidência**: Linhas 107-138 do arquivo `tac_optmization.py`

#### 6. Remoção de Código Inalcançável
**Descrição**: Remove código após `goto` que nunca será executado.

**Evidência**: Linhas 140-173 do arquivo `tac_optmization.py`

#### Estatísticas de Otimização

| Arquivo | Instruções TAC (antes) | Instruções TAC (depois) | Redução |
|---------|------------------------|-------------------------|---------|
| factorial.txt | 23 | 19 | 17.4% |
| fibonacci.txt | 192 | 190 | 1.0% |
| taylor.txt | 105 | 82 | 21.9% |

---

### 1.3. Geração de Código Assembly AVR

#### ✅ Geração de Assembly AVR - **ATENDIDO**

O arquivo `generate_assembly/generate_assembly.py` implementa a classe `TACToAVRAssembly` que gera código Assembly compatível com ATmega328P (Arduino Uno).

**Características implementadas:**
- ✅ Arquitetura de 8 bits
- ✅ Uso de registradores de uso geral (R16-R31)
- ✅ Instruções de dois operandos
- ✅ Arquitetura Harvard (memória separada)
- ✅ Aritmética de 32 bits com escala x100 (2 casas decimais)

**Convenções de Registradores:**
| Registrador | Uso |
|-------------|-----|
| R16 | Configuração/temporário |
| R18-R21 | Variável/resultado operando 1 (32 bits) |
| R22-R25 | Variável/resultado operando 2 (32 bits) |
| R24-R27 | Parâmetros para funções (print) |
| R30-R31 (Z) | Ponteiro de endereço de memória |

**Mapeamento TAC para Assembly:**

| TAC | Assembly AVR |
|-----|--------------|
| `t1 = a + b` | `add r18, r22` / `adc r19, r23` / ... |
| `t1 = a - b` | `sub r18, r22` / `sbc r19, r23` / ... |
| `t1 = a * b` | `call mul_scaled32` |
| `t1 = a \| b` | `call div_scaled32` |
| `goto L1` | `rjmp L1` |
| `ifFalse a goto L1` | `brne skip` / `rjmp L1` / `skip:` |

**Funções auxiliares implementadas:**
- `mul_scaled32` - Multiplicação 32 bits com escala x100
- `div_scaled32` - Divisão 32 bits com escala x100
- `print_scaled_decimal32` - Impressão formatada via UART
- `send_uart` - Envio de caractere pela UART

#### ✅ Assembly Gerado Compila - **VERIFICAÇÃO PENDENTE**

Os arquivos `.s` são gerados corretamente:
- ✅ `tests/factorial/output.s` (603 linhas)
- ✅ `tests/fibonacci/output.s` (gerado)
- ✅ `tests/taylor/output.s` (1396 linhas)

**Nota**: A compilação com `avr-gcc` requer a toolchain AVR instalada. Os arquivos `main.elf` e `main.hex` estão presentes no repositório para cada teste.

#### ⚠️ Execução no Arduino - **NÃO VERIFICÁVEL REMOTAMENTE**

Os arquivos `.hex` estão disponíveis no repositório:
- `tests/factorial/main.hex`
- `tests/fibonacci/main.hex`
- `tests/taylor/main.hex`

**Observação**: A validação no hardware Arduino Uno requer acesso físico ao dispositivo e não pode ser verificada automaticamente nesta avaliação.

---

### 1.4. Arquivos de Teste

#### ✅ Teste 1: Cálculo de Fatorial - **ATENDIDO**

**Arquivo**: `tests/factorial/factorial.txt`

```
( 8 N )
( 1 I )
( 1 F )
( ( I N <= ) ( ( F I * ) F ) ( ( I 1 + ) I ) for )
( F )
```

**Requisitos atendidos:**
- ✅ Calcula n! para n = 8 (esperado: 40320)
- ✅ Utiliza estrutura de laço (`for`)
- ✅ Demonstra uso de variáveis (memórias N, I, F)
- ✅ Armazena/exibe resultado

**Arquivos gerados:**
- `factorial.txt_tac.json` / `factorial.txt_tac.md`
- `factorial.txt_tac_optimized.json` / `factorial.txt_tac_optimized.md`
- `factorial.txt_arvore_atribuida.json`
- `output.s`, `main.elf`, `main.hex`

#### ✅ Teste 2: Sequência de Fibonacci - **ATENDIDO**

**Arquivo**: `tests/fibonacci/fibonacci.txt`

O arquivo calcula e imprime os **24 primeiros números** da sequência de Fibonacci usando o operador `RES` para referência a resultados anteriores.

**Requisitos atendidos:**
- ✅ Calcula os 24 primeiros números da sequência de Fibonacci
- ✅ Armazena/exibe os resultados via `print`
- ✅ Demonstra uso de variáveis (memórias A, F1, F3)

**Observação**: O arquivo implementa uma versão não-iterativa usando referências a resultados anteriores (`RES`), o que é uma abordagem válida conforme o enunciado que menciona "opcionalmente" para estruturas de laço no Fibonacci.

**Arquivos gerados:**
- `fibonacci.txt_tac.json` / `fibonacci.txt_tac.md`
- `fibonacci.txt_tac_optimized.json` / `fibonacci.txt_tac_optimized.md`
- `fibonacci.txt_arvore_atribuida.json`
- `output.s`, `main.elf`, `main.hex`

#### ✅ Teste 3: Série de Taylor para Cosseno - **ATENDIDO PARCIALMENTE**

**Arquivo**: `tests/taylor/taylor.txt`

```
( 1.0 RESULT )
( 0.5 X )
( ( 0.5 2 ^ ) POT1 )
...
( RESULT )
```

**Requisitos atendidos:**
- ✅ Implementa a fórmula truncada de Taylor para cos(x)
- ✅ Usa notação RPN e operador de Divisão Real (`|`)
- ✅ Armazena X e RESULT em memórias
- ✅ Usa números literais em ponto flutuante (1.0, 0.5, 2.0)
- ✅ Testa aritmética de ponto flutuante

**Observação sobre precisão**: O sistema usa escala x100 (inteiros escalados) para representar números com 2 casas decimais, em vez de IEEE 754 meia precisão (16 bits). Esta é uma abordagem prática para o ATmega328P que não possui FPU.

**Nota sobre o código**: Há um possível erro lógico no terceiro termo do taylor.txt (usa POT2 e FRA2 em vez de POT3 e FRA3 no cálculo final), mas a estrutura geral está correta.

---

## 2. Organização e Legibilidade do Código (15%)

### ✅ Código Claro, Comentado e Estruturado - **ATENDIDO**

**Estrutura do repositório:**
```
RA4_6/
├── main.py                      # Script principal (pipeline)
├── lexical_analyzer/            # Analisador léxico (Fase 1)
├── syntactic_analyzer/          # Analisador sintático (Fase 2)
├── semantic_analyzer/           # Analisador semântico (Fase 3)
├── intermediate_code/           # Geração de TAC (Fase 4)
│   ├── tac_generator/          # Gerador de TAC
│   └── tac_optimization/       # Otimizador de TAC
├── generate_assembly/           # Gerador de Assembly AVR
└── tests/                       # Arquivos de teste
    ├── factorial/
    ├── fibonacci/
    └── taylor/
```

**Qualidade do código:**
- ✅ Classes bem definidas com docstrings
- ✅ Type hints em Python (uso de `List`, `Dict`, `Any`, `Optional`)
- ✅ Separação de responsabilidades entre módulos
- ✅ Comentários explicativos em português

### ✅ README Bem Escrito - **ATENDIDO**

O `README.md` contém:
- ✅ Nome do projeto e propósito
- ✅ Integrante do grupo (Theo Hillmann Luiz Coelho)
- ✅ Instruções para executar o compilador
- ✅ Documentação das otimizações implementadas
- ✅ Formato das instruções TAC
- ✅ Comandos para compilar e carregar no Arduino
- ✅ Exemplos de uso

**Itens faltantes ou incompletos:**
- ⚠️ Nome da instituição de ensino
- ⚠️ Ano, disciplina e professor
- ⚠️ Documentação detalhada das convenções de registradores AVR

### ✅ Commits e Organização GitHub - **VERIFICAÇÃO MANUAL NECESSÁRIA**

O repositório está público e acessível. A verificação de pull requests e histórico de commits requer análise manual do histórico do GitHub.

---

## 3. Robustez e Validação (15%)

### ✅ Tratamento de Erros - **ATENDIDO PARCIALMENTE**

**Erros tratados:**
- ✅ Erros léxicos reportados por expressão
- ✅ Erros sintáticos com contagem
- ✅ Erros semânticos com validação
- ✅ Pipeline interrompido em caso de erro

**Exemplo de tratamento de erros (main.py):**
```python
for index, token in enumerate(tokens):
    if "Error" in token:
        print(f"File {sample_file}, expression {index}")
        print(f"    {token}")
        return
```

### ✅ Geração de Arquivos de Saída - **ATENDIDO**

Para cada arquivo de teste, são gerados:
- ✅ `{input}_arvore_atribuida.json` - Árvore sintática atribuída
- ✅ `{input}_tac.json` - TAC não otimizado
- ✅ `{input}_tac.md` - TAC formatado em markdown
- ✅ `{input}_tac_optimized.json` - TAC otimizado
- ✅ `{input}_tac_optimized.md` - TAC otimizado em markdown
- ✅ `{input}_relatorio_tipos.md` - Relatório de tipos
- ✅ `output.s` - Assembly AVR gerado
- ✅ `main.elf` - Arquivo ELF compilado
- ✅ `main.hex` - Arquivo HEX para upload

### ⚠️ Validação no Arduino - **NÃO VERIFICÁVEL**

**Itens não verificáveis remotamente:**
- Execução correta no Arduino Uno
- Saída serial dos programas
- Fotos/vídeos da execução

---

## 4. Resumo da Avaliação

### Pontuação Estimada

| Critério | Peso | Nota Estimada | Justificativa |
|----------|------|---------------|---------------|
| **Geração TAC** | - | ✅ 100% | Implementação completa e funcional |
| **TAC Operações Aritméticas** | - | ✅ 100% | Todos operadores suportados |
| **TAC Estruturas de Controle** | - | ✅ 100% | Laços e condicionais funcionais |
| **Otimizações (≥3)** | - | ✅ 100% | 6 técnicas implementadas |
| **Geração Assembly AVR** | - | ✅ 90% | Geração correta, execução não verificada |
| **Assembly Compila/Executa** | - | ⚠️ 50% | Arquivos presentes, execução não verificada |
| **Arquivos de Teste** | - | ✅ 90% | 3 arquivos presentes, fibonacci sem laço |
| **Organização do Código** | 15% | ✅ 85% | Bem estruturado, faltam alguns detalhes no README |
| **Robustez e Validação** | 15% | ⚠️ 70% | Tratamento de erros ok, validação hardware não verificável |

### Pontos Positivos

1. **Arquitetura bem definida**: Pipeline clara com separação entre fases
2. **Otimizações robustas**: 6 técnicas de otimização com loop até fixpoint
3. **Assembly AVR funcional**: Implementação completa com aritmética escalada
4. **Documentação adequada**: README com informações essenciais
5. **Funções auxiliares**: UART, multiplicação e divisão escaladas bem implementadas

### Pontos a Melhorar

1. **Validação no Arduino**: Não há evidências de teste no hardware (fotos/vídeos)
2. **Fibonacci sem laço explícito**: Usa abordagem alternativa com RES
3. **Taylor com possível erro lógico**: Terceiro termo usa variáveis incorretas
4. **Precisão de ponto flutuante**: Usa escala x100 em vez de IEEE 754 half-precision
5. **README incompleto**: Faltam informações institucionais

### Conformidade com Requisitos Essenciais

| Requisito | Status |
|-----------|--------|
| Código em Python/C/C++ | ✅ Python |
| Gerador de TAC | ✅ Implementado |
| Otimizador de TAC | ✅ Implementado (6 técnicas) |
| Gerador Assembly AVR | ✅ Implementado |
| 3 Arquivos de teste | ✅ fatorial, fibonacci, taylor |
| Arquivos .hex gerados | ✅ Presentes |
| Repositório público GitHub | ✅ Acessível |
| README com instruções | ✅ Presente |

---

## 5. Conclusão

O projeto **atende aos requisitos fundamentais** do trabalho de Geração de Código Intermediário e Assembly. A implementação demonstra:

- Compreensão sólida dos conceitos de compiladores
- Implementação funcional de todas as 4 fases
- Boas práticas de organização de código
- Documentação adequada

**Recomendações para melhoria:**
1. Adicionar evidências de teste no Arduino (saída serial, fotos)
2. Completar informações institucionais no README
3. Revisar o cálculo da Série de Taylor (terceiro termo)
4. Considerar implementar Fibonacci com laço para demonstração mais clara

---

*Avaliação gerada automaticamente em 26/11/2025*
