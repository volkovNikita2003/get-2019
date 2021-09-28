import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#настройки
leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

#настройка пинов на выход
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN, pull_up_down=GPIO.PUD_UP) # настройка на вход + подтяжка вверх

now = time.time()
period = 30

while (time.time() < now + period):
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))

time.sleep(2)

#гасим светодиоды
GPIO.output(leds, 0)
GPIO.cleanup()