#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pratica6_rfid_led.py
#  
#  Copyright 2023  <sel@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from mfrc522 import SimpleMFRC522
from time import sleep 
import RPi.GPIO as rpio

rpio.setwarnings(False)

led1_pin = 27			#LED acionado por botão
led2_pin = 22	#LED acionado com contagem

#Configuração dos pinos no pacote RPi.GPIO
rpio.setmode(rpio.BCM)
rpio.setwarnings(False)
rpio.setup(led1_pin, rpio.OUT)	#LED 2 como saída
rpio.setup(led2_pin, rpio.OUT)	#LED 3 como saída

#Inicializa os LEDs 2 e 3 apagados
rpio.output(led1_pin, False)	
rpio.output(led2_pin, False)

leitor = SimpleMFRC522()
ID_tag= 497386497680 # ID da tag utilizada

print("Posicione a tag do leitor para leitura:")
while True:
	
	leitura = leitor.read()
	print("ID:{}\nTexto: {}".format(leitura[0],leitura[1]))
	sleep(3) 
	
	if leitura[0]==ID_tag:
		rpio.output(led1_pin, True)
		rpio.output(led2_pin, False)
		print("Acesso Liberado")
	else:
		rpio.output(led2_pin, True)
		rpio.output(led1_pin, False)
		print("Acesso Negado")

