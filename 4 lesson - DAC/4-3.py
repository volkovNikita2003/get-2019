import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000) 
p.start(0)
try:
    while True:
        print()
        str = input("Введите число от 0 до 100 (для завершения программы введите q)")
        if str.isdigit():
            value = int(str)

            if 0 <= value <= 100:
                p.ChangeDutyCycle(value)
                time.sleep(0.1)
            
            else:
                print("Введено некорректное число")
        
        elif str == 'q':
            print("Завершение программы")
            break

        else:
            print("Введена некорректная строка")

except KeyboardInterrupt:
    print("Выход из цикла")
finally:
    p.stop()
    GPIO.cleanup(22)