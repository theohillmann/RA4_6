#!/usr/bin/env bash

set -e  # se der erro em qualquer comando, o script para

# Se quiser garantir que está no diretório certo:
# cd "$(dirname "$0")"

#echo "=== 1) Gerando TAC e Assembly com Python ==="
#python main.py

echo
echo "=== 2) Compilando Assembly com avr-gcc ==="
avr-gcc -mmcu=atmega328p -Os -o main.elf output.s

echo
echo "=== 3) Gerando main.hex com avr-objcopy ==="
avr-objcopy -O ihex -R .eeprom main.elf main.hex

echo
echo "=== 4) Subindo para o Arduino com avrdude ==="
avrdude -p m328p -c arduino -P /dev/tty.usbmodem11101 -b 115200 -U flash:w:main.hex

echo
echo "=== Concluído! ==="