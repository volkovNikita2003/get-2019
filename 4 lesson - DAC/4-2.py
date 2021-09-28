import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
t = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(bits)]

def dec2dac(n):
    signal = dec2bin(n)
    GPIO.output(dac, signal)
    return signal

try:
    while True:
        for i in range(256):
            signal = dec2dac(i)
            GPIO.output(dac, signal)
            time.sleep(t)
        for i in range(255, -1, -1):
            signal = dec2dac(i)
            GPIO.output(dac, signal)
            time.sleep(t)
except KeyboardInterrupt:
    print("Выход из цикла")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)