
import RPi.GPIO as GPIO
import time
from my9221_RaspberryPi import MY9221
GPIO.setmode(GPIO.BOARD)
push = 11
GPIO.setup(push, GPIO.IN)
ledbar = MY9221(12,13)
cont = 0
estadoCero = 0
while True:
 leer_push = GPIO.input(push)
 if (not leer_push) != estadoCero:
 if (not leer_push) == 1:
 cont = cont + 1
 estadoCero = (not leer_push)
 if cont == 11:
 cont = 0
 ledbar.level(cont)