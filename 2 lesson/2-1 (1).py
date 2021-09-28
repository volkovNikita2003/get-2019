import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#настройки
period = 5
pattern_0 = [0, 0, 0, 0, 0, 0, 0, 0]
pattern_1 = [1, 0, 1, 0, 0, 0, 1, 0]
pattern_2 = [1, 0, 1, 0, 1, 0, 1, 0]
pattern_3 = [1, 1, 1, 1, 0, 0, 0, 0]
leds = [21, 20, 16, 12, 7, 8, 25, 24]


#настройка пинов на выход
GPIO.setup(leds, GPIO.OUT)

def lightPattern(pattern, period):
    # светодиоды
    GPIO.output(leds, pattern)
    time.sleep(period)
    #гасим светодиоды
    GPIO.output(leds, pattern_0)

#вызываем функции с разными шаблонами
lightPattern(pattern_1, period)
time.sleep(2)
lightPattern(pattern_2, period)
time.sleep(2)
lightPattern(pattern_3, period)


#гасим светодиоды
GPIO.output(leds, 0)
GPIO.cleanup()