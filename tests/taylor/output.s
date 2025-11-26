.global main
.section .text

main:
clr r1
ldi r16, 0x08
out 0x3E, r16
ldi r16, 0xFF
out 0x3D, r16

ldi r16, 0x67
sts 0xC4, r16
ldi r16, 0x00
sts 0xC5, r16
ldi r16, 0x18
sts 0xC1, r16
ldi r16, 0x06
sts 0xC2, r16

; TAC to AVR Assembly (32-bit scaled x100)
; ATmega328P (Arduino Uno)
; Generated from TAC

ldi r18, 100
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 60
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 50
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 64
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 25
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 48
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 200
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 36
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 100
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 24
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 100
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 0
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
L0:
ldi r30, 24
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 232
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 36
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 236
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 232
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 236
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
cp  r18, r22
cpc r19, r23
brlt cmp_t0
breq cmp_t0
ldi r18, 0
ldi r19, 0
ldi r20, 0
ldi r21, 0
rjmp cmp_e0
cmp_t0:
ldi r18, 100
ldi r19, 0
ldi r20, 0
ldi r21, 0
cmp_e0:
ldi r30, 68
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 68
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
mov r24, r18
or  r24, r19
or  r24, r20
or  r24, r21
brne iffalse_skip1
rjmp L1
iffalse_skip1:
ldi r30, 0
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 72
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 24
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 76
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 72
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 76
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
call mul_scaled32
ldi r30, 80
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 80
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 0
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 24
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 84
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 84
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r22, 100
ldi r23, 0
ldi r24, 0
ldi r25, 0
add r18, r22
adc r19, r23
adc r20, r24
adc r21, r25
ldi r30, 88
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 88
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 24
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
rjmp L0
L1:
ldi r30, 48
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 92
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 0
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 96
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 92
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 96
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
call div_scaled32
ldi r30, 100
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 100
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 12
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 60
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 104
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 12
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 108
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 104
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 108
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
sub r18, r22
sbc r19, r23
sbc r20, r24
sbc r21, r25
ldi r30, 112
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 112
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 60
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 6
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 52
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 144
ldi r19, 1
ldi r20, 0
ldi r21, 0
ldi r30, 40
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 100
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 28
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 100
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 4
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
L2:
ldi r30, 28
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 116
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 40
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 120
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 116
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 120
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
cp  r18, r22
cpc r19, r23
brlt cmp_t2
breq cmp_t2
ldi r18, 0
ldi r19, 0
ldi r20, 0
ldi r21, 0
rjmp cmp_e2
cmp_t2:
ldi r18, 100
ldi r19, 0
ldi r20, 0
ldi r21, 0
cmp_e2:
ldi r30, 124
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 124
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
mov r24, r18
or  r24, r19
or  r24, r20
or  r24, r21
brne iffalse_skip3
rjmp L3
iffalse_skip3:
ldi r30, 4
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 128
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 28
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 132
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 128
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 132
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
call mul_scaled32
ldi r30, 136
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 136
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 4
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 28
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 140
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 140
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r22, 100
ldi r23, 0
ldi r24, 0
ldi r25, 0
add r18, r22
adc r19, r23
adc r20, r24
adc r21, r25
ldi r30, 144
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 144
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 28
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
rjmp L2
L3:
ldi r30, 52
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 148
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 4
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 152
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 148
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 152
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
call div_scaled32
ldi r30, 156
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 156
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 16
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 60
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 160
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 16
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 164
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 160
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 164
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
add r18, r22
adc r19, r23
adc r20, r24
adc r21, r25
ldi r30, 168
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 168
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 60
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 1
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 56
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 88
ldi r19, 2
ldi r20, 0
ldi r21, 0
ldi r30, 44
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 100
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 32
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r18, 100
ldi r19, 0
ldi r20, 0
ldi r21, 0
ldi r30, 8
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
L4:
ldi r30, 32
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 172
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 44
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 176
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 172
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 176
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
cp  r18, r22
cpc r19, r23
brlt cmp_t4
breq cmp_t4
ldi r18, 0
ldi r19, 0
ldi r20, 0
ldi r21, 0
rjmp cmp_e4
cmp_t4:
ldi r18, 100
ldi r19, 0
ldi r20, 0
ldi r21, 0
cmp_e4:
ldi r30, 180
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 180
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
mov r24, r18
or  r24, r19
or  r24, r20
or  r24, r21
brne iffalse_skip5
rjmp L5
iffalse_skip5:
ldi r30, 8
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 184
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 32
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 188
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 184
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 188
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
call mul_scaled32
ldi r30, 192
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 192
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 8
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 32
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 196
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 196
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r22, 100
ldi r23, 0
ldi r24, 0
ldi r25, 0
add r18, r22
adc r19, r23
adc r20, r24
adc r21, r25
ldi r30, 200
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 200
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 32
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
rjmp L4
L5:
ldi r30, 52
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 204
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 8
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 208
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 204
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 208
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
call div_scaled32
ldi r30, 212
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 212
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 20
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 60
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 216
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 16
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 220
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 216
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 220
ldi r31, 1
ld  r22, Z+
ld  r23, Z+
ld  r24, Z+
ld  r25, Z
sub r18, r22
sbc r19, r23
sbc r20, r24
sbc r21, r25
ldi r30, 224
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 224
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 60
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 60
ldi r31, 1
ld  r18, Z+
ld  r19, Z+
ld  r20, Z+
ld  r21, Z
ldi r30, 228
ldi r31, 1
st  Z+, r18
st  Z+, r19
st  Z+, r20
st  Z,  r21
ldi r30, 228
ldi r31, 1
ld  r24, Z+
ld  r25, Z+
ld  r26, Z+
ld  r27, Z
call print_scaled_decimal32

end_loop:
rjmp end_loop

send_uart:
push r16
uart_ready:
lds  r16, 0xC0
sbrs r16, 5
rjmp uart_ready
sts  0xC6, r24
pop  r16
ret

print_uint16_5:
push r18
push r19
push r20
push r21
push r22
push r23

mov r18, r24
mov r19, r25
clr r21

mov r20, r18
or  r20, r19
brne pu16_nonzero
ldi r24, 48
call send_uart
rjmp pu16_done

pu16_nonzero:
; Loop principal: extrai dígitos (resto da divisão por 10)
pu16_div_loop:
mov r20, r18
or  r20, r19
breq pu16_print

; Divide r19:r18 por 10 -> quociente em r22:r23, resto em r18
clr r22
clr r23
ldi r24, 10
clr r25
pu16_div10_loop:
cp  r18, r24
cpc r19, r25
brlo pu16_div10_done
sub r18, r24
sbc r19, r25
inc r22
brne pu16_div10_loop
inc r23
rjmp pu16_div10_loop
pu16_div10_done:

; Agora r18 = resto (0..9), r22:r23 = quociente
ldi r24, 48
add r24, r18
push r24
inc r21
mov r18, r22
mov r19, r23
rjmp pu16_div_loop

pu16_print:
; Desempilha e envia os dígitos (ordem correta)
pu16_print_loop:
cpi r21, 0
breq pu16_done
pop r24
call send_uart
dec r21
rjmp pu16_print_loop

pu16_done:
pop r23
pop r22
pop r21
pop r20
pop r19
pop r18
ret

print_scaled_decimal32:
push r18
push r19
push r20
push r21
push r22
push r23

; valor escalado (x100) em r24:r25:r26:r27
mov r18, r24
mov r19, r25
mov r20, r26
mov r21, r27

clr r22
clr r23
ldi r24, 100
clr r25
psd32_div100_loop:
tst r21
brne psd32_can_sub
tst r20
brne psd32_can_sub
tst r19
brne psd32_can_sub
cp  r18, r24
brlo psd32_div100_done
psd32_can_sub:
sub r18, r24
sbc r19, r25
sbc r20, r25
sbc r21, r25
inc r22
brne psd32_div100_loop
inc r23
rjmp psd32_div100_loop
psd32_div100_done:

; r18..r21 = resto (<100), r22:r23 = quociente
mov r20, r18
mov r24, r22
mov r25, r23

; imprime parte inteira (16 bits) com print_uint16_5
call print_uint16_5

; ponto decimal
ldi r24, 46
call send_uart

; duas casas decimais a partir do resto (0..99)
mov r18, r20
clr r21
ldi r24, 10
psd32_frac_loop:
cp  r18, r24
brlo psd32_frac_done
sub r18, r24
inc r21
rjmp psd32_frac_loop
psd32_frac_done:
; r21 = dezenas, r18 = unidades
ldi r24, 48
add r24, r21
call send_uart
ldi r24, 48
add r24, r18
call send_uart

; newline
ldi r24, 10
call send_uart

pop r23
pop r22
pop r21
pop r20
pop r19
pop r18
ret

; Multiplicação 32 bits com escala x100
; Entrada: a_s  = r18:r19:r20:r21
;          b_s  = r22:r23:r24:r25
; Saída:   r18:r19:r20:r21 = (a_s * b_s) / 100 (escalado x100)
mul_scaled32:
push r26
push r27
push r28
push r29
push r16

; copia a_s para r26..r29
mov r26, r18
mov r27, r19
mov r28, r20
mov r29, r21

; resultado = 0 em r18..r21
clr r18
clr r19
clr r20
clr r21

ldi r16, 32
ms32_loop:
sbrs r22, 0
rjmp ms32_no_add
add r18, r26
adc r19, r27
adc r20, r28
adc r21, r29
ms32_no_add:
lsl r26
rol r27
rol r28
rol r29
lsr r25
ror r24
ror r23
ror r22
dec r16
brne ms32_loop

; agora produto em r18..r21 (mod 2^32)
; divide por 100 com subtrações sucessivas, quociente em r26..r29
clr r26
clr r27
clr r28
clr r29
ldi r22, 100
clr r23
ms32_div_loop:
tst r21
brne ms32_can_sub
tst r20
brne ms32_can_sub
tst r19
brne ms32_can_sub
cp  r18, r22
brlo ms32_div_done
ms32_can_sub:
sub r18, r22
sbc r19, r23
sbc r20, r23
sbc r21, r23
inc r26
brne ms32_div_loop
inc r27
brne ms32_div_loop
inc r28
brne ms32_div_loop
inc r29
rjmp ms32_div_loop
ms32_div_done:
mov r18, r26
mov r19, r27
mov r20, r28
mov r21, r29

pop r16
pop r29
pop r28
pop r27
pop r26
ret

; Divisão 32 bits com escala x100
; Entrada: s_a = r18:r19:r20:r21 (escala x100)
;          s_b = r22:r23:r24:r25 (escala x100, usa low16 r22:r23)
; Saída:   r18:r19:r20:r21 = s_c = floor(100 * s_a / s_b) (escala x100)
div_scaled32:
push r26
push r27
push r28
push r29
push r16

; Calcula 100 * s_a em r26..r29 (4 + 32 + 64 = 100)
; r26..r29 = s_a
mov r26, r18
mov r27, r19
mov r28, r20
mov r29, r21

; r26..r29 = 4 * s_a (2 shifts)
lsl r26
rol r27
rol r28
rol r29
lsl r26
rol r27
rol r28
rol r29

; r18..r21 = 32 * s_a (5 shifts)
lsl r18
rol r19
rol r20
rol r21
lsl r18
rol r19
rol r20
rol r21
lsl r18
rol r19
rol r20
rol r21
lsl r18
rol r19
rol r20
rol r21
lsl r18
rol r19
rol r20
rol r21

; soma 32*s_a em r26..r29 -> 36*s_a
add r26, r18
adc r27, r19
adc r28, r20
adc r29, r21

; r18..r21 = 64 * s_a (mais 1 shift)
lsl r18
rol r19
rol r20
rol r21

; soma 64*s_a -> 100*s_a
add r26, r18
adc r27, r19
adc r28, r20
adc r29, r21

; quociente q = 0 em r24:r25
clr r24
clr r25

; divisor usa low16 de s_b: r22:r23
clr r18

ds32_div_loop:
tst r29
brne ds32_can_sub
tst r28
brne ds32_can_sub
cp  r26, r22
cpc r27, r23
brlo ds32_div_done
ds32_can_sub:
sub r26, r22
sbc r27, r23
sbc r28, r18
sbc r29, r18
inc r24
brne ds32_div_loop
inc r25
rjmp ds32_div_loop
ds32_div_done:

; q (r24:r25) = floor(100*s_a / s_b)
mov r18, r24
mov r19, r25
clr r20
clr r21

pop r16
pop r29
pop r28
pop r27
pop r26
ret
