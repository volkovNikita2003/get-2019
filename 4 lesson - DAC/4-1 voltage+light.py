import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

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
        print()
        str = input("Введите число от 0 до 255 (для завершения программы введите q)")
        if str.isdigit():
            value = int(str)

            if 0 <= value <= 255:
                signal = dec2dac(int(str))
                voltage = value / levels * maxVoltage
                print("Выведен сигнал {:^3} -> {}. Выходное напряжение {:.2f}".format(value, signal, voltage))
            
            else:
                print("Введено некорректное число")
        
        elif str == 'q':
            print("Завершение программы")
            break

        else:
            print("Введена некорректная строка")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)