from typing import List, Dict, Any


class TACToAVRAssembly:

    def __init__(self):
        # Mapa variável -> endereço (low byte) na SRAM
        self.memory_map: Dict[str, int] = {}
        self.mem_address = 0x0100  # início da área de dados

        self.assembly_code: List[str] = []
        self.label_counter = 0

    # ------------------------------------------------------------------ #
    # Pipeline principal
    # ------------------------------------------------------------------ #

    def convert(self, tac: List[Dict[str, Any]]) -> str:
        """Converte uma lista de instruções TAC em um programa AVR completo."""
        self._allocate_memory(tac)
        self._generate_code(tac)
        return self._generate_full_program()

    def _allocate_memory(self, tac: List[Dict[str, Any]]) -> None:
        """Reserva 4 bytes na RAM para cada variável que aparece no TAC."""
        vars_found = set()
        for instr in tac:
            if instr.get("dest"):
                vars_found.add(instr["dest"])
            if instr.get("arg1") and not self._is_number(str(instr["arg1"])):
                vars_found.add(str(instr["arg1"]))
            if instr.get("arg2") and not self._is_number(str(instr["arg2"])):
                vars_found.add(str(instr["arg2"]))

        for var in sorted(vars_found):
            if var not in self.memory_map:
                self.memory_map[var] = self.mem_address
                self.mem_address += 4  # 32 bits

    def _ensure_var(self, var: str) -> int:
        """Garante que a variável tenha um endereço mapeado."""
        if var not in self.memory_map:
            self.memory_map[var] = self.mem_address
            self.mem_address += 4
        return self.memory_map[var]

    # ------------------------------------------------------------------ #
    # Helpers de memória 32 bits
    # ------------------------------------------------------------------ #

    def _load_var32(self, var: str, r0: int, r1: int, r2: int, r3: int) -> None:
        """
        Carrega variável 32 bits da RAM para registradores (little-endian).
        var -> r0 (low), r1, r2, r3 (high)
        Usa o ponteiro Z (r31:r30).
        """
        addr = self._ensure_var(var)
        low = addr & 0xFF
        high = (addr >> 8) & 0xFF

        # Z = addr
        self.assembly_code.append(f"ldi r30, {low}")
        self.assembly_code.append(f"ldi r31, {high}")
        # lê 4 bytes: [low, mid1, mid2, high]
        self.assembly_code.append(f"ld  r{r0}, Z+")
        self.assembly_code.append(f"ld  r{r1}, Z+")
        self.assembly_code.append(f"ld  r{r2}, Z+")
        self.assembly_code.append(f"ld  r{r3}, Z")

    def _store_var32(self, var: str, r0: int, r1: int, r2: int, r3: int) -> None:
        """
        Armazena registradores 32 bits em variável na RAM (little-endian).
        r0 (low), r1, r2, r3 (high) -> var
        Usa o ponteiro Z (r31:r30).
        """
        addr = self._ensure_var(var)
        low = addr & 0xFF
        high = (addr >> 8) & 0xFF

        # Z = addr
        self.assembly_code.append(f"ldi r30, {low}")
        self.assembly_code.append(f"ldi r31, {high}")
        # escreve 4 bytes: [low, mid1, mid2, high]
        self.assembly_code.append(f"st  Z+, r{r0}")
        self.assembly_code.append(f"st  Z+, r{r1}")
        self.assembly_code.append(f"st  Z+, r{r2}")
        self.assembly_code.append(f"st  Z,  r{r3}")

    def _load_const32(self, value: int, r0: int, r1: int, r2: int, r3: int) -> None:
        """Carrega constante 32 bits em registradores r0..r3 (little-endian)."""
        value &= 0xFFFFFFFF
        b0 = value & 0xFF
        b1 = (value >> 8) & 0xFF
        b2 = (value >> 16) & 0xFF
        b3 = (value >> 24) & 0xFF
        self.assembly_code.append(f"ldi r{r0}, {b0}")
        self.assembly_code.append(f"ldi r{r1}, {b1}")
        self.assembly_code.append(f"ldi r{r2}, {b2}")
        self.assembly_code.append(f"ldi r{r3}, {b3}")

    # ------------------------------------------------------------------ #
    # Geração de código por instrução TAC
    # ------------------------------------------------------------------ #

    def _generate_code(self, tac: List[Dict[str, Any]]) -> None:
        self.assembly_code.append("; TAC to AVR Assembly (32-bit scaled x100)")
        self.assembly_code.append("; ATmega328P (Arduino Uno)")
        self.assembly_code.append("; Generated from TAC")
        self.assembly_code.append("")

        for instr in tac:
            op = instr.get("op")
            if op == "label":
                self._gen_label(instr)
            elif op == "assign":
                self._gen_assign(instr)
            elif op == "binop":
                self._gen_binop(instr)
            elif op == "mem_store":
                self._gen_mem_store(instr)
            elif op == "mem_load":
                self._gen_mem_load(instr)
            elif op == "print":
                self._gen_print(instr)
            elif op == "goto":
                self._gen_goto(instr)
            elif op == "ifFalse":
                self._gen_iffalse(instr)

    def _gen_label(self, instr: Dict[str, Any]) -> None:
        self.assembly_code.append(f"{instr['label']}:")

    def _gen_assign(self, instr: Dict[str, Any]) -> None:
        """dest = arg1 (com escala x100)."""
        dest = instr["dest"]
        value = str(instr["arg1"])

        if self._is_number(value):
            num = int(float(value) * 100)  # escala x100
            self._load_const32(num, 18, 19, 20, 21)
        else:
            self._load_var32(value, 18, 19, 20, 21)

        self._store_var32(dest, 18, 19, 20, 21)

    def _gen_binop(self, instr: Dict[str, Any]) -> None:
        """
        dest = arg1 op arg2 (em 32 bits, escala x100).
        Usa:
        - arg1 em r18:r19:r20:r21
        - arg2 em r22:r23:r24:r25
        - resultado em r18:r19:r20:r21
        """
        dest = instr["dest"]
        arg1 = str(instr["arg1"])
        arg2 = str(instr["arg2"])
        op = instr["op_symbol"]

        # Carrega arg1 em r18..21
        if self._is_number(arg1):
            v1 = int(float(arg1) * 100)
            self._load_const32(v1, 18, 19, 20, 21)
        else:
            self._load_var32(arg1, 18, 19, 20, 21)

        # Carrega arg2 em r22..25
        if self._is_number(arg2):
            v2 = int(float(arg2) * 100)
            self._load_const32(v2, 22, 23, 24, 25)
        else:
            self._load_var32(arg2, 22, 23, 24, 25)

        if op == "+":
            self.assembly_code.append("add r18, r22")
            self.assembly_code.append("adc r19, r23")
            self.assembly_code.append("adc r20, r24")
            self.assembly_code.append("adc r21, r25")

        elif op == "-":
            self.assembly_code.append("sub r18, r22")
            self.assembly_code.append("sbc r19, r23")
            self.assembly_code.append("sbc r20, r24")
            self.assembly_code.append("sbc r21, r25")

        elif op == "*":
            # Multiplicação escalada: (a_s * b_s) / 100
            self.assembly_code.append("call mul_scaled32")

        elif op == "|":
            # Divisão real com 2 casas decimais:
            # s_c = floor(100 * s_a / s_b)
            self.assembly_code.append("call div_scaled32")

        elif op in ["<", ">", "<=", ">=", "==", "!="]:
            self.assembly_code.append("cp  r18, r22")
            self.assembly_code.append("cpc r19, r23")
            self._gen_cmp_result_16(op)

        else:
            raise NotImplementedError(
                f"Operador binário não suportado em 32 bits: {op}"
            )

        # Guarda resultado em dest
        self._store_var32(dest, 18, 19, 20, 21)

    def _gen_mem_store(self, instr: Dict[str, Any]) -> None:
        """MEM[dest] = arg1 (dest tratado como variável na RAM)."""
        dest = instr["dest"]
        value = str(instr["arg1"])

        if self._is_number(value):
            num = int(float(value) * 100)
            self._load_const32(num, 18, 19, 20, 21)
        else:
            self._load_var32(value, 18, 19, 20, 21)

        self._store_var32(dest, 18, 19, 20, 21)

    def _gen_mem_load(self, instr: Dict[str, Any]) -> None:
        """dest = MEM[arg1] (variáveis são todas em memória)."""
        dest = instr["dest"]
        src = str(instr["arg1"])

        self._load_var32(src, 18, 19, 20, 21)
        self._store_var32(dest, 18, 19, 20, 21)

    def _gen_print(self, instr: Dict[str, Any]) -> None:
        """print arg1 (usa escala x100 e função print_scaled_decimal32)."""
        value = str(instr["arg1"])

        if self._is_number(value):
            num = int(float(value) * 100)
            self._load_const32(num, 24, 25, 26, 27)
        else:
            self._load_var32(value, 24, 25, 26, 27)

        self.assembly_code.append("call print_scaled_decimal32")

    def _gen_goto(self, instr: Dict[str, Any]) -> None:
        self.assembly_code.append(f"rjmp {instr['label']}")

    def _gen_iffalse(self, instr: Dict[str, Any]) -> None:
        """
        ifFalse cond goto label
        cond é 32 bits: 0 => false, !=0 => true.
        """
        cond = str(instr["arg1"])
        label = instr["label"]

        # Carrega cond em r18..21
        if self._is_number(cond):
            num = int(float(cond) * 100)
            self._load_const32(num, 18, 19, 20, 21)
        else:
            self._load_var32(cond, 18, 19, 20, 21)

        # Testa zero: OR dos 4 bytes em r24 e checa Z
        self.assembly_code.append("mov r24, r18")
        self.assembly_code.append("or  r24, r19")
        self.assembly_code.append("or  r24, r20")
        self.assembly_code.append("or  r24, r21")

        skip_label = f"iffalse_skip{self.label_counter}"
        self.label_counter += 1

        self.assembly_code.append(f"brne {skip_label}")  # se !=0, não pula
        self.assembly_code.append(f"rjmp {label}")  # cond == 0 -> goto
        self.assembly_code.append(f"{skip_label}:")

    # ------------------------------------------------------------------ #
    # Comparação em 16 bits (para I, N, etc.)
    # ------------------------------------------------------------------ #

    def _gen_cmp_result_16(self, op: str) -> None:
        """
        Usa flags após CP/CPC (r18:r19 - r22:r23) para gerar:
        - false: r18:r19:r20:r21 = 0
        - true:  r18:r19:r20:r21 = 100 (1.00 escalado; bytes altos = 0)
        """
        true_label = f"cmp_t{self.label_counter}"
        end_label = f"cmp_e{self.label_counter}"
        self.label_counter += 1

        if op == "<":
            self.assembly_code.append(f"brlt {true_label}")
        elif op == ">":
            # A > B  <=> A >= B e A != B
            self.assembly_code.append(f"breq {end_label}")
            self.assembly_code.append(f"brge {true_label}")
        elif op == "<=":
            # A <= B  <=> A < B ou A == B
            self.assembly_code.append(f"brlt {true_label}")
            self.assembly_code.append(f"breq {true_label}")
        elif op == ">=":
            self.assembly_code.append(f"brge {true_label}")
        elif op == "==":
            self.assembly_code.append(f"breq {true_label}")
        elif op == "!=":
            self.assembly_code.append(f"brne {true_label}")

        # false
        self.assembly_code.append("ldi r18, 0")
        self.assembly_code.append("ldi r19, 0")
        self.assembly_code.append("ldi r20, 0")
        self.assembly_code.append("ldi r21, 0")
        self.assembly_code.append(f"rjmp {end_label}")

        # true
        self.assembly_code.append(f"{true_label}:")
        self.assembly_code.append("ldi r18, 100")  # 1.00 escalado
        self.assembly_code.append("ldi r19, 0")
        self.assembly_code.append("ldi r20, 0")
        self.assembly_code.append("ldi r21, 0")
        self.assembly_code.append(f"{end_label}:")

    # ------------------------------------------------------------------ #
    # Utilitários
    # ------------------------------------------------------------------ #

    def _is_number(self, value: str) -> bool:
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    # ------------------------------------------------------------------ #
    # Programa completo + funções auxiliares
    # ------------------------------------------------------------------ #

    def _generate_full_program(self) -> str:
        program: List[str] = []

        program.append(".global main")
        program.append(".section .text")
        program.append("")
        program.append("main:")
        program.append("clr r1")  # garante zero_reg
        program.append("ldi r16, 0x08")
        program.append("out 0x3E, r16")
        program.append("ldi r16, 0xFF")
        program.append("out 0x3D, r16")
        program.append("")
        program.append("ldi r16, 0x67")
        program.append("sts 0xC4, r16")
        program.append("ldi r16, 0x00")
        program.append("sts 0xC5, r16")
        program.append("ldi r16, 0x18")
        program.append("sts 0xC1, r16")
        program.append("ldi r16, 0x06")
        program.append("sts 0xC2, r16")
        program.append("")

        program.extend(self.assembly_code)
        program.append("")
        program.append("end_loop:")
        program.append("rjmp end_loop")
        program.append("")

        program.extend(self._uart_funcs())
        program.extend(self._math_funcs())

        return "\n".join(program)

    # ------------------------------------------------------------------ #
    # UART + impressão (32 bits escalado x100)
    # ------------------------------------------------------------------ #

    def _uart_funcs(self) -> List[str]:
        f: List[str] = []

        # Envio de um byte em r24 pela UART
        f.append("send_uart:")
        f.append("push r16")
        f.append("uart_ready:")
        f.append("lds  r16, 0xC0")
        f.append("sbrs r16, 5")
        f.append("rjmp uart_ready")
        f.append("sts  0xC6, r24")
        f.append("pop  r16")
        f.append("ret")
        f.append("")

        # Imprime inteiro 16 bits (0..65535) em r24:r25
        f.append("print_uint16_5:")
        f.append("push r18")
        f.append("push r19")
        f.append("push r20")
        f.append("push r21")
        f.append("push r22")
        f.append("push r23")
        f.append("")
        f.append("mov r18, r24")  # valor low")
        f.append("mov r19, r25")  # valor high")
        f.append("clr r21")  # contador de dígitos (0..5)")
        f.append("")
        # Se valor == 0, imprime '0' direto
        f.append("mov r20, r18")
        f.append("or  r20, r19")
        f.append("brne pu16_nonzero")
        f.append("ldi r24, 48")  # '0'")
        f.append("call send_uart")
        f.append("rjmp pu16_done")
        f.append("")
        f.append("pu16_nonzero:")
        f.append("; Loop principal: extrai dígitos (resto da divisão por 10)")
        f.append("pu16_div_loop:")
        f.append("mov r20, r18")
        f.append("or  r20, r19")
        f.append("breq pu16_print")  # se valor == 0, vai imprimir")
        f.append("")
        f.append("; Divide r19:r18 por 10 -> quociente em r22:r23, resto em r18")
        f.append("clr r22")  # quociente low")
        f.append("clr r23")  # quociente high")
        f.append("ldi r24, 10")
        f.append("clr r25")
        f.append("pu16_div10_loop:")
        f.append("cp  r18, r24")
        f.append("cpc r19, r25")
        f.append("brlo pu16_div10_done")
        f.append("sub r18, r24")
        f.append("sbc r19, r25")
        f.append("inc r22")
        f.append("brne pu16_div10_loop")
        f.append("inc r23")
        f.append("rjmp pu16_div10_loop")
        f.append("pu16_div10_done:")
        f.append("")
        f.append("; Agora r18 = resto (0..9), r22:r23 = quociente")
        f.append("ldi r24, 48")  # '0'")
        f.append("add r24, r18")  # '0' + resto")
        f.append("push r24")  # empilha dígito ASCII")
        f.append("inc r21")  # conta dígitos")
        f.append("mov r18, r22")  # valor = quociente")
        f.append("mov r19, r23")
        f.append("rjmp pu16_div_loop")
        f.append("")
        f.append("pu16_print:")
        f.append("; Desempilha e envia os dígitos (ordem correta)")
        f.append("pu16_print_loop:")
        f.append("cpi r21, 0")
        f.append("breq pu16_done")
        f.append("pop r24")
        f.append("call send_uart")
        f.append("dec r21")
        f.append("rjmp pu16_print_loop")
        f.append("")
        f.append("pu16_done:")
        f.append("pop r23")
        f.append("pop r22")
        f.append("pop r21")
        f.append("pop r20")
        f.append("pop r19")
        f.append("pop r18")
        f.append("ret")
        f.append("")

        # Imprime valor 32-bit escalado x100 em r24..r27 -> "<inteiro>.<duas casas>"
        f.append("print_scaled_decimal32:")
        f.append("push r18")
        f.append("push r19")
        f.append("push r20")
        f.append("push r21")
        f.append("push r22")
        f.append("push r23")
        f.append("")
        f.append("; valor escalado (x100) em r24:r25:r26:r27")
        f.append("mov r18, r24")  # low")
        f.append("mov r19, r25")
        f.append("mov r20, r26")
        f.append("mov r21, r27")  # high")
        f.append("")
        # divisão por 100 (inteiro) -> quociente em r22:r23 (16 bits), resto 0..99 em r18
        f.append("clr r22")  # quociente low")
        f.append("clr r23")  # quociente high")
        f.append("ldi r24, 100")
        f.append("clr r25")  # zero")
        f.append("psd32_div100_loop:")
        f.append("tst r21")
        f.append("brne psd32_can_sub")
        f.append("tst r20")
        f.append("brne psd32_can_sub")
        f.append("tst r19")
        f.append("brne psd32_can_sub")
        f.append("cp  r18, r24")
        f.append("brlo psd32_div100_done")
        f.append("psd32_can_sub:")
        f.append("sub r18, r24")
        f.append("sbc r19, r25")
        f.append("sbc r20, r25")
        f.append("sbc r21, r25")
        f.append("inc r22")
        f.append("brne psd32_div100_loop")
        f.append("inc r23")
        f.append("rjmp psd32_div100_loop")
        f.append("psd32_div100_done:")
        f.append("")
        f.append("; r18..r21 = resto (<100), r22:r23 = quociente")
        f.append("mov r20, r18")  # guarda resto 0..99 em r20")
        f.append("mov r24, r22")  # quociente low -> r24")
        f.append("mov r25, r23")  # quociente high -> r25")
        f.append("")
        f.append("; imprime parte inteira (16 bits) com print_uint16_5")
        f.append("call print_uint16_5")
        f.append("")
        f.append("; ponto decimal")
        f.append("ldi r24, 46")  # '.'")
        f.append("call send_uart")
        f.append("")
        f.append("; duas casas decimais a partir do resto (0..99)")
        f.append("mov r18, r20")  # copia resto")
        f.append("clr r21")  # dezenas")
        f.append("ldi r24, 10")
        f.append("psd32_frac_loop:")
        f.append("cp  r18, r24")
        f.append("brlo psd32_frac_done")
        f.append("sub r18, r24")
        f.append("inc r21")
        f.append("rjmp psd32_frac_loop")
        f.append("psd32_frac_done:")
        f.append("; r21 = dezenas, r18 = unidades")
        f.append("ldi r24, 48")
        f.append("add r24, r21")  # '0' + dezenas")
        f.append("call send_uart")
        f.append("ldi r24, 48")
        f.append("add r24, r18")  # '0' + unidades")
        f.append("call send_uart")
        f.append("")
        f.append("; newline")
        f.append("ldi r24, 10")
        f.append("call send_uart")
        f.append("")
        f.append("pop r23")
        f.append("pop r22")
        f.append("pop r21")
        f.append("pop r20")
        f.append("pop r19")
        f.append("pop r18")
        f.append("ret")
        f.append("")

        return f

    # ------------------------------------------------------------------ #
    # Funções matemáticas (mul_scaled32 + div_scaled32) – escala x100
    # ------------------------------------------------------------------ #

    def _math_funcs(self) -> List[str]:
        f: List[str] = []

        f.append("; Multiplicação 32 bits com escala x100")
        f.append("; Entrada: a_s  = r18:r19:r20:r21")
        f.append(";          b_s  = r22:r23:r24:r25")
        f.append("; Saída:   r18:r19:r20:r21 = (a_s * b_s) / 100 (escalado x100)")
        f.append("mul_scaled32:")
        f.append("push r26")
        f.append("push r27")
        f.append("push r28")
        f.append("push r29")
        f.append("push r16")
        f.append("")
        f.append("; copia a_s para r26..r29")
        f.append("mov r26, r18")
        f.append("mov r27, r19")
        f.append("mov r28, r20")
        f.append("mov r29, r21")
        f.append("")
        f.append("; resultado = 0 em r18..r21")
        f.append("clr r18")
        f.append("clr r19")
        f.append("clr r20")
        f.append("clr r21")
        f.append("")
        f.append("ldi r16, 32")
        f.append("ms32_loop:")
        f.append("sbrs r22, 0")
        f.append("rjmp ms32_no_add")
        f.append("add r18, r26")
        f.append("adc r19, r27")
        f.append("adc r20, r28")
        f.append("adc r21, r29")
        f.append("ms32_no_add:")
        f.append("lsl r26")
        f.append("rol r27")
        f.append("rol r28")
        f.append("rol r29")
        f.append("lsr r25")
        f.append("ror r24")
        f.append("ror r23")
        f.append("ror r22")
        f.append("dec r16")
        f.append("brne ms32_loop")
        f.append("")
        f.append("; agora produto em r18..r21 (mod 2^32)")
        f.append("; divide por 100 com subtrações sucessivas, quociente em r26..r29")
        f.append("clr r26")
        f.append("clr r27")
        f.append("clr r28")
        f.append("clr r29")
        f.append("ldi r22, 100")
        f.append("clr r23")
        f.append("ms32_div_loop:")
        f.append("tst r21")
        f.append("brne ms32_can_sub")
        f.append("tst r20")
        f.append("brne ms32_can_sub")
        f.append("tst r19")
        f.append("brne ms32_can_sub")
        f.append("cp  r18, r22")
        f.append("brlo ms32_div_done")
        f.append("ms32_can_sub:")
        f.append("sub r18, r22")
        f.append("sbc r19, r23")
        f.append("sbc r20, r23")
        f.append("sbc r21, r23")
        f.append("inc r26")
        f.append("brne ms32_div_loop")
        f.append("inc r27")
        f.append("brne ms32_div_loop")
        f.append("inc r28")
        f.append("brne ms32_div_loop")
        f.append("inc r29")
        f.append("rjmp ms32_div_loop")
        f.append("ms32_div_done:")
        f.append("mov r18, r26")
        f.append("mov r19, r27")
        f.append("mov r20, r28")
        f.append("mov r21, r29")
        f.append("")
        f.append("pop r16")
        f.append("pop r29")
        f.append("pop r28")
        f.append("pop r27")
        f.append("pop r26")
        f.append("ret")
        f.append("")

        # -------------------- NOVA FUNÇÃO: div_scaled32 -------------------- #
        f.append("; Divisão 32 bits com escala x100")
        f.append("; Entrada: s_a = r18:r19:r20:r21 (escala x100)")
        f.append(";          s_b = r22:r23:r24:r25 (escala x100, usa low16 r22:r23)")
        f.append(
            "; Saída:   r18:r19:r20:r21 = s_c = floor(100 * s_a / s_b) (escala x100)"
        )
        f.append("div_scaled32:")
        f.append("push r26")
        f.append("push r27")
        f.append("push r28")
        f.append("push r29")
        f.append("push r16")
        f.append("")
        f.append("; Calcula 100 * s_a em r26..r29 (4 + 32 + 64 = 100)")
        f.append("; r26..r29 = s_a")
        f.append("mov r26, r18")
        f.append("mov r27, r19")
        f.append("mov r28, r20")
        f.append("mov r29, r21")
        f.append("")
        f.append("; r26..r29 = 4 * s_a (2 shifts)")
        f.append("lsl r26")
        f.append("rol r27")
        f.append("rol r28")
        f.append("rol r29")
        f.append("lsl r26")
        f.append("rol r27")
        f.append("rol r28")
        f.append("rol r29")
        f.append("")
        f.append("; r18..r21 = 32 * s_a (5 shifts)")
        f.append("lsl r18")
        f.append("rol r19")
        f.append("rol r20")
        f.append("rol r21")
        f.append("lsl r18")
        f.append("rol r19")
        f.append("rol r20")
        f.append("rol r21")
        f.append("lsl r18")
        f.append("rol r19")
        f.append("rol r20")
        f.append("rol r21")
        f.append("lsl r18")
        f.append("rol r19")
        f.append("rol r20")
        f.append("rol r21")
        f.append("lsl r18")
        f.append("rol r19")
        f.append("rol r20")
        f.append("rol r21")
        f.append("")
        f.append("; soma 32*s_a em r26..r29 -> 36*s_a")
        f.append("add r26, r18")
        f.append("adc r27, r19")
        f.append("adc r28, r20")
        f.append("adc r29, r21")
        f.append("")
        f.append("; r18..r21 = 64 * s_a (mais 1 shift)")
        f.append("lsl r18")
        f.append("rol r19")
        f.append("rol r20")
        f.append("rol r21")
        f.append("")
        f.append("; soma 64*s_a -> 100*s_a")
        f.append("add r26, r18")
        f.append("adc r27, r19")
        f.append("adc r28, r20")
        f.append("adc r29, r21")
        f.append("")
        f.append("; quociente q = 0 em r24:r25")
        f.append("clr r24")
        f.append("clr r25")
        f.append("")
        f.append("; divisor usa low16 de s_b: r22:r23")
        f.append("clr r18")  # constante 0 para high bytes")
        f.append("")
        f.append("ds32_div_loop:")
        f.append("tst r29")
        f.append("brne ds32_can_sub")
        f.append("tst r28")
        f.append("brne ds32_can_sub")
        f.append("cp  r26, r22")
        f.append("cpc r27, r23")
        f.append("brlo ds32_div_done")
        f.append("ds32_can_sub:")
        f.append("sub r26, r22")
        f.append("sbc r27, r23")
        f.append("sbc r28, r18")
        f.append("sbc r29, r18")
        f.append("inc r24")
        f.append("brne ds32_div_loop")
        f.append("inc r25")
        f.append("rjmp ds32_div_loop")
        f.append("ds32_div_done:")
        f.append("")
        f.append("; q (r24:r25) = floor(100*s_a / s_b)")
        f.append("mov r18, r24")
        f.append("mov r19, r25")
        f.append("clr r20")
        f.append("clr r21")
        f.append("")
        f.append("pop r16")
        f.append("pop r29")
        f.append("pop r28")
        f.append("pop r27")
        f.append("pop r26")
        f.append("ret")
        f.append("")

        return f
