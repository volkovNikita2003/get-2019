import matplotlib.pyplot as plt
import time
import RPi.GPIO as GPIO

# первоначальные настройки
leds = [24, 25, 8, 7, 12, 16, 20, 21]
leds.reverse()
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
comparator = 4
troykaModule = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comparator, GPIO.IN)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.LOW)

#функции для считывания сигнала с компоратора
def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(bits)]

def dec2dac(n):
    signal = dec2bin(n)
    GPIO.output(dac, signal)
    return signal

def adc(i, value):
    if i == -1:
        return value
    dec2dac(value + 2**i)
    time.sleep(0.001)
    compValue = GPIO.input(comparator)
    if compValue == 0:
        return adc(i-1, value)
    else:
        return adc(i-1, value+2**i)

data = [] #значения считанного сигнала

try:
    GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH) #подача напряжения на 17 пин
    time_start = time.time() #начало эксперемента
    print("Начало эксперемента")
    print("Началась зарядка конденсатора")
    flag = False #False - зарядка конденсатора. True - разрядка конденсатора 
    while True:
        value = adc(bits-1, 0) #запуск функции
        data.append(value) #добавление значения в массив

        # вывод сигнала в область leds
        GPIO.output(leds, dec2bin(value))

        # проверка уровня заряда конденсатора, при значении близком к максимуму начинается разрядка конденсатора
        if value > 245 and not(flag):
            GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.LOW) #подача напряжения на 17 пин прекращена
            print("Началась разрядка конденсатора")
            flag = True
        # проверка уровня заряда конденсатора, при значении = 0 эксперемент заканчивается
        if value == 0 and flag:
            time_end = time.time() #конец эксперемента
            print("Конец эксперемента")
            break
    
    experiment_time = time_end - time_start #время эксперемента
    T = experiment_time / (len(data) - 1) #период измерений *(len(data) - 1) т.к. промежутков времени на 1 меньше, чем отсчетов
    sampling_rate = (len(data) - 1) / experiment_time #частота дискретезации
    voltage_1 = maxVoltage / levels #шаг по напряжению
    print()
    print("Длительность эксперимента = {} с, период измерений = {:.5f} с, часота дискретизации = {:.5f} Гц, шаг по напряжению = {:.5f} В".format(experiment_time, T, sampling_rate, voltage_1))

    #построение графика
    plt.plot(data)
    plt.show()

    #запись данных в файл data.txt
    with open('data.txt', 'w') as f:
        data_str = [str(item) for item in data] #перевод int в str
        f.write("\n".join(data_str)) #запись данных
        print()
        print("Измерения записаны в файл data.txt")
    #запись настроек в файл settings.txt
    with open('settings.txt', 'w') as f:
        f.write("Период измерений: {} с\n".format(T))
        f.write("Единица напряжения: {:.3f} В".format(voltage_1))
        print("Настройки записаны в setting.txt")
    
finally:
    #сброс настроек
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup(leds)