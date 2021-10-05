import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
comparator = 4
troykaModule = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comparator, GPIO.IN)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)

def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(bits)]

def dec2dac(n):
    signal = dec2bin(n)
    GPIO.output(dac, signal)
    return signal

try:
    while True:
        for value in range(256):
            signal = dec2dac(value)
            time.sleep(0.001)
            voltage = value / levels * maxVoltage
            compValue = GPIO.input(comparator)
            if compValue == 0:
                print("ADC value = {:^3} -> {}, input voltave = {:.2f}V".format(value, signal, voltage))
                break
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)