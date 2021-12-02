#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO
import time
import threading

sensorPuerta = 16
ledRojo=21

flag1 = 0


def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    GPIO.cleanup () # limpieza de los recursos GPIO antes de salir
    sys.exit(0)

def comportamintopuerta (canal):
    global flag1
    if flag1 == 0:
        pwm.ChangeDutyCycle(100)
        print("Puerta abierta!!!!!!!!")
        flag1 = 1
    else:
        pwm.ChangeDutyCycle(0)
        print("Puerta cerrada")
        flag1 = 0


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensorPuerta, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup (ledRojo, GPIO.OUT)

    pwm = GPIO.PWM(ledRojo,100)
    pwm.start (100)

    hilo1 = threading.Thread(target=GPIO.add_event_detect(sensorPuerta, GPIO.BOTH,
      callback=comportamintopuerta, bouncetime=200))
    hilo1.start()

    hilo1.join()
    signal.signal(signal.SIGINT, callbackSalir) # callback para CTRL+C que limpia todos los hilos anteriores
    signal.pause() # esperamos por hilo/callback CTRL+C antes de acabar para que no se acabe solo el principal