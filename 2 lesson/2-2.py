import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#настройки
cyclesNumber = 3
period = 1
pattern_0 = [0, 0, 0, 0, 0, 0, 0, 0]
pattern_1 = [1, 0, 1, 0, 0, 0, 1, 0]
pattern_2 = [1, 0, 1, 0, 1, 0, 1, 0]
pattern_3 = [1, 1, 1, 1, 0, 0, 0, 0]
dac = [26, 19, 13, 6, 5, 11, 9, 10]


#настройка пинов на выход
GPIO.setup(dac, GPIO.OUT)

def runningLight(cyclesNumber, period):
    for i in range(cyclesNumber):
        for j in range(8):
            GPIO.output(dac[j], 1)
            time.sleep(period)
            GPIO.output(dac[j], 0)

#вызываем функцию
runningLight(cyclesNumber, period)

#гасим светодиоды
GPIO.output(dac, 0)
GPIO.cleanup()