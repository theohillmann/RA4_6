from typing import List, Dict, Any, Optional, Set
import copy


class TACOptimizer:
    """
    Otimizador de TAC (Three Address Code) que aplica várias técnicas de otimização:
    - Constant Folding
    - Constant Propagation
    - Dead Code Elimination
    - Eliminação de Saltos Redundantes
    - Branch Prediction Simplification
    """

    def __init__(self):
        self.constant_values: Dict[str, Any] = {}
        self.used_variables: Set[str] = set()
        self.labels_used: Set[str] = set()

    def optimize(self, tac: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Aplica todas as otimizações ao TAC fornecido.

        Args:
            tac: Lista de instruções TAC

        Returns:
            Lista de instruções TAC otimizadas
        """
        optimized = copy.deepcopy(tac)
        previous = None
        iteration = 0
        max_iterations = 10

        while previous != optimized and iteration < max_iterations:
            previous = copy.deepcopy(optimized)
            optimized = self._constant_folding(optimized)
            optimized = self._constant_propagation(optimized)
            optimized = self._simplify_branches(optimized)
            optimized = self._remove_unreachable_code(optimized)
            optimized = self._dead_code_elimination(optimized)
            optimized = self._remove_redundant_jumps(optimized)
            iteration += 1

        return optimized

    def _constant_folding(self, tac: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Avalia expressões constantes em tempo de compilação.
        Exemplo: t1 = 2 + 3 → t1 = 5
        """
        optimized = []

        for instr in tac:
            if instr["op"] == "binop":
                arg1 = instr["arg1"]
                arg2 = instr["arg2"]
                op_symbol = instr["op_symbol"]

                val1 = self._try_parse_const(arg1)
                val2 = self._try_parse_const(arg2)

                if val1 is not None and val2 is not None:
                    result = self._execute_binop(val1, val2, op_symbol)
                    if result is not None:
                        optimized.append(
                            {
                                "op": "assign",
                                "dest": instr["dest"],
                                "arg1": str(result),
                                "arg2": None,
                                "label": None,
                                "op_symbol": None,
                            }
                        )
                        continue

            optimized.append(instr)

        return optimized

    def _constant_propagation(self, tac: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Propaga valores constantes através do código.
        """
        self.constant_values = {}
        for instr in tac:
            if instr["op"] == "assign":
                val = self._try_parse_const(instr["arg1"])
                if val is not None:
                    self.constant_values[instr["dest"]] = val

        optimized = []
        for instr in tac:
            new_instr = copy.deepcopy(instr)

            if new_instr["arg1"] in self.constant_values:
                new_instr["arg1"] = str(self.constant_values[new_instr["arg1"]])

            if new_instr["arg2"] in self.constant_values:
                new_instr["arg2"] = str(self.constant_values[new_instr["arg2"]])

            optimized.append(new_instr)

        return optimized

    def _simplify_branches(self, tac: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Simplifica branches com condições conhecidas em tempo de compilação.
        - Se ifFalse com condição != 0: remove o branch (nunca pula)
        - Se ifFalse com condição == 0: converte para goto (sempre pula)
        """
        optimized = []

        for instr in tac:
            if instr["op"] == "ifFalse":
                cond = instr["arg1"]
                val = self._try_parse_const(cond)

                if val is not None:
                    if val == 0.0 or val == 0:
                        # Condição sempre falsa (pula sempre)
                        optimized.append(
                            {
                                "op": "goto",
                                "dest": None,
                                "arg1": None,
                                "arg2": None,
                                "label": instr["label"],
                                "op_symbol": None,
                            }
                        )
                    # Se val != 0, nunca pula - remover o ifFalse
                    continue

            optimized.append(instr)

        return optimized

    def _remove_unreachable_code(
        self, tac: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Remove código inalcançável após goto (antes do próximo rótulo).
        """
        # Primeiro, identificar todos os rótulos
        label_set = set()
        for instr in tac:
            if instr["op"] == "label":
                label_set.add(instr["label"])

        optimized = []
        i = 0
        while i < len(tac):
            instr = tac[i]
            optimized.append(instr)

            # Se encontramos um goto, pular código até encontrar um rótulo
            if instr["op"] == "goto":
                i += 1
                # Pular instruções até encontrar um rótulo
                while i < len(tac):
                    next_instr = tac[i]
                    if next_instr["op"] == "label":
                        # Parar de pular quando encontrar um rótulo
                        break
                    i += 1
                # Decrementar i para processar o rótulo na próxima iteração
                i -= 1

            i += 1

        return optimized

    def _dead_code_elimination(self, tac: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Remove código que não afeta o resultado do programa.
        """
        # Primeiro: identificar rótulos usados
        used_labels = set()
        for instr in tac:
            if instr["op"] in ["goto", "ifFalse"]:
                if instr["label"]:
                    used_labels.add(instr["label"])

        # Segundo: varredura para trás para marcar variáveis realmente usadas
        used_vars = set()
        important_ops = {"print", "mem_store", "ifFalse", "goto", "label"}

        for instr in reversed(tac):
            if instr["op"] in important_ops:
                if instr["arg1"]:
                    used_vars.add(instr["arg1"])
                if instr["arg2"]:
                    used_vars.add(instr["arg2"])
            elif instr["dest"]:
                if instr["dest"] in used_vars:
                    if instr["arg1"]:
                        used_vars.add(instr["arg1"])
                    if instr["arg2"]:
                        used_vars.add(instr["arg2"])

        # Terceiro: remover instruções desnecessárias
        optimized = []
        for instr in tac:
            # Manter rótulos usados
            if instr["op"] == "label":
                if instr["label"] in used_labels:
                    optimized.append(instr)
                continue

            # Manter operações com efeito colateral
            if instr["op"] in important_ops:
                optimized.append(instr)
                continue

            # Manter se o destino é usado
            if instr["dest"] and instr["dest"] in used_vars:
                optimized.append(instr)
            elif instr["op"] == "mem_load":
                # mem_load sempre mantém
                optimized.append(instr)

        return optimized

    def _remove_redundant_jumps(
        self, tac: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Remove saltos para a próxima instrução.
        """
        label_positions = {}
        for i, instr in enumerate(tac):
            if instr["op"] == "label":
                label_positions[instr["label"]] = i

        optimized = []
        for i, instr in enumerate(tac):
            if instr["op"] == "goto":
                target_pos = label_positions.get(instr["label"])
                # Se o rótulo é a próxima instrução (não vazia), é redundante
                if target_pos is not None:
                    next_real_instr = i + 1
                    if (
                        next_real_instr < len(tac)
                        and tac[next_real_instr]["op"] == "label"
                    ):
                        if tac[next_real_instr]["label"] == instr["label"]:
                            continue

            optimized.append(instr)

        return optimized

    def _try_parse_const(self, value: Any) -> Optional[float]:
        """
        Tenta converter um valor em constante numérica.
        """
        if value is None:
            return None

        try:
            return float(value)
        except (ValueError, TypeError):
            return None

    def _execute_binop(self, val1: float, val2: float, op: str) -> Optional[float]:
        """
        Executa uma operação binária com valores constantes.
        """
        try:
            if op == "+":
                return val1 + val2
            elif op == "-":
                return val1 - val2
            elif op == "*":
                return val1 * val2
            elif op == "/":
                if val2 == 0:
                    return None
                return val1 / val2
            elif op == "|":
                if val2 == 0:
                    return None
                return val1 / val2
            elif op == "%":
                if val2 == 0:
                    return None
                return float(int(val1) % int(val2))
            elif op == "^":
                return val1**val2
            elif op == ">":
                return 1.0 if val1 > val2 else 0.0
            elif op == "<":
                return 1.0 if val1 < val2 else 0.0
            elif op == ">=":
                return 1.0 if val1 >= val2 else 0.0
            elif op == "<=":
                return 1.0 if val1 <= val2 else 0.0
            elif op == "==":
                return 1.0 if val1 == val2 else 0.0
            elif op == "!=":
                return 1.0 if val1 != val2 else 0.0
            else:
                return None
        except (ValueError, ZeroDivisionError):
            return None

    def to_s_expression(self, tac: List[Dict[str, Any]]) -> str:
        """
        Converte TAC otimizado para sintaxe S-expression.
        """
        s_expressions = []

        for instr in tac:
            if instr["op"] == "assign":
                s_expr = f"( {instr['dest']} {instr['arg1']} assign )"
                s_expressions.append(s_expr)

            elif instr["op"] == "binop":
                arg1 = instr["arg1"]
                arg2 = instr["arg2"]
                op_symbol = instr["op_symbol"]
                dest = instr["dest"]

                s_expr = f"( {arg1} {arg2} {op_symbol} )"
                s_expr = f"( {dest} {s_expr} assign )"
                s_expressions.append(s_expr)

            elif instr["op"] == "mem_store":
                s_expr = f"( mem_store {instr['dest']} {instr['arg1']} )"
                s_expressions.append(s_expr)

            elif instr["op"] == "mem_load":
                s_expr = f"( {instr['dest']} ( mem_load {instr['arg1']} ) assign )"
                s_expressions.append(s_expr)

            elif instr["op"] == "print":
                s_expr = f"( print {instr['arg1']} )"
                s_expressions.append(s_expr)

            elif instr["op"] == "copy":
                s_expr = f"( {instr['dest']} {instr['arg1']} assign )"
                s_expressions.append(s_expr)

            elif instr["op"] == "label":
                s_expr = f"( label {instr['label']} )"
                s_expressions.append(s_expr)

            elif instr["op"] == "goto":
                s_expr = f"( goto {instr['label']} )"
                s_expressions.append(s_expr)

            elif instr["op"] == "ifFalse":
                s_expr = f"( ifFalse {instr['arg1']} {instr['label']} )"
                s_expressions.append(s_expr)

        return "\n".join(s_expressions)
