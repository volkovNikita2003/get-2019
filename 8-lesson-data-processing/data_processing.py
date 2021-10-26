import numpy as np
import matplotlib.pyplot as plt

#чтение данных из data.txt и setting.txt
data_array = np.loadtxt("data.txt", dtype=int)
setting_array = np.loadtxt("settings.txt", dtype=float) # 0 - шаг времени (период измерений); 1 - шаг по напряжению
Nt = data_array.size #количество измерений

# Перевод показаний АЦП в Вольты, номеров отсчётов в секунды;
data_voltage_array = data_array * setting_array[1]
time_array = np.arange(0.0, Nt*setting_array[0], setting_array[0])

#рассчет времени зарядки и разрядки
index_max_voltage = np.argmax(data_array)
time_up = round(index_max_voltage * setting_array[0], 2)
time_down = round((Nt - index_max_voltage) * setting_array[0], 2)
print(time_up, time_down)

#построение графика
count_markers = 50
w = 16
h = 10
dpi = 400
fig, ax = plt.subplots(figsize=(w,h), dpi=dpi)
ax.plot(time_array, data_voltage_array, 
        linestyle = '-', linewidth = 0.3, color = 'blue',
        marker = 'o', markersize = 5, markevery=[i for i in range(0, Nt, Nt//count_markers)],
        label = "V(t)"
        )

ax.legend() # легенда
ax_x_min = 0
ax_x_max = setting_array[0]*Nt*(1+0.05)
ax_y_min = 0
ax_y_max = setting_array[1]*255*(1+0.05)
ax.axis( [ax_x_min, ax_x_max, ax_y_min, ax_y_max] ) # макс и мин занчения по осям
#  Добавляем подписи к осям:
ax.set_xlabel('Время (с)')
ax.set_ylabel('Напряжение (В)')
#заголовок
ax.set_title("Процесс заряда и разряда кондесатора в RC-цепочке", loc = "center", wrap=True)

# сетка
#  Прежде чем рисовать вспомогательные линии необходимо включить второстепенные деления осей:
ax.minorticks_on()
#  Определяем внешний вид линий основной сетки:
ax.grid(which='major',
        color = 'gray',  #  цвет линий
        linewidth = 1, #  толщина
        linestyle = '-'
        )
#  Определяем внешний вид линий вспомогательной сетки:
ax.grid(which='minor',
        color = 'gray',  #  цвет линий
        linewidth = 0.5, #  толщина
        linestyle = '--'
        )

#добавление текста
x1 = (ax_x_max - ax_x_min)/100*60
y1 = (ax_y_max - ax_y_min)/100*50
ax.text(x1, y1, "Время заряда = " + str(time_up) + " c",
        color = 'black',    #  цвет шрифта
        fontsize = 14)

x2 = (ax_x_max - ax_x_min)/100*60
y2 = y1 - (ax_y_max - ax_y_min)/100*10
ax.text(x2, y2, "Время разряда = " + str(time_down) + " c",
        color = 'black',    #  цвет шрифта
        fontsize = 14)

#сохранение графика
fig.savefig("graph.svg")
#plt.show()