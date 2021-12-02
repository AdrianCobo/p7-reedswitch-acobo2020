# P7-ReedSwitch


## (CC-BY-NC-SA) Adrián Cobo Merino

El objetivo de este esta práctica es tener la primera toma de contacto con un interruptor de lengüeta.

### Funcionamiento del Programa.

Este programa encenderá un led cuando el iman se separe del interruptor indicando que la puerta está abierta, y lo apagará cuando este pegado el iman al interruptor, indicando que la puerta se ha
cerrado.

```python
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
```

**El esquema de conexión se puede intuir de**

```python
   
   #GPIO Mode (BOARD / BCM)
   GPIO.setmode(GPIO.BCM)

   #set GPIO Pins
   sensorPuerta = 16
   ledRojo=21
```

Si quieres ver un video de demostracion del programa, pulsa [aqui](https://drive.google.com/file/d/1cDLSdudxqsnL4s5az-hANzkDzSYxUYtO/view?usp=sharing).

Para cualquier duda: <a.cobo.2020@alumos.urjc.es>
