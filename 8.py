import numpy as np
import matplotlib.pyplot as ptl

with open("/home/b01-109/Desktop/Scripts/Denisova Ekaterina B01-109/settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("/home/b01-109/Desktop/Scripts/Denisova Ekaterina B01-109/data.txt")
set_array  = np.loadtxt("/home/b01-109/Desktop/Scripts/Denisova Ekaterina B01-109/settings.txt")

fig, ax = ptl.subplots(figsize = (14, 10), dpi = 300)


data_array = data_array * set_array[1]
y = data_array
x = [1] * 898

for i in range(898):
    x[i] = i * set_array[0]

t_charge = np.argmax(data_array)
t_charge = t_charge * set_array[0]
t_down = (899 - np.argmax(data_array)) * set_array[0]

ptl.title("Зарядка и разрядка конденсатора в RC-цепи", color = 'brown') # header

ax.grid(color = 'purple',    #  lines colour
        linewidth = 0.40,    #  width
        linestyle = 'dashed')

ax.minorticks_on()
ax.grid(which='minor',
        color = 'purple',
        linewidth = 0.20,
        linestyle = 'dashed')

ptl.plot(x, y, '-b', label='Зависимость', markevery = 70, marker = "s")

ptl.legend()
ax.set_xlabel('Время t(с)')
ax.set_ylabel('Напряжение U(В)')
ptl.text(6.3, 1.5, 'время зарядки %f' % t_charge, fontsize = 8)
ptl.text(6, 2, 'время разрядки %f' % t_down, fontsize = 8)

print(t_charge)
print(t_down)
ptl.xlim (0, 10)
ptl.ylim (0, 3.5)

ptl.text(0, 8, 'время зарядки %f' % t_charge, fontsize = 500)


fig.savefig("png.svg")
ptl.show()
