from scipy.fftpack import fft, rfft, irfft, rfftfreq
import numpy as np
import math
import matplotlib.pyplot as plt
time=10
dt=0.1
t=np.arange(-time, time, dt)
a=10
b=20
c=30
#Моделирование сигнала из трёх синусоид
input=[a*math.sin(math.pi*i)+b*math.sin(math.pi*2*i)+c*math.sin(math.pi*3*i) for i in t]
#Вывод исходного сигнала
plt.plot(t, input, color='green')
plt.title('Исходный сигнал')
plt.xlabel('Частота, Hz')
plt.ylabel('Амплитуда, М')
plt.grid(True)
plt.show()
#Создание и вывод зашумленного сигнала
stray=np.random.uniform(-30, 30, np.size(t))
plt.plot(t, input + stray, color='red')
plt.title('Зашумленный сигнал')
plt.xlabel('Частота, Hz')
plt.ylabel('Амплитуда, М')
plt.grid(True)
plt.show()
#Вывод спектра зашумленного сигнала
spectr=rfft(input + stray)
plt.plot(rfftfreq(len(t)), abs(spectr),)
plt.title('Спектр зашумленного сигнала')
plt.xlabel('Частота, Hz')
plt.ylabel('Амплитуда, М')
plt.grid(True)
plt.show()
#Фильтрация шума по спектру и вывод спектра без шума
true_spectr = []
for i in range(0, len(spectr)):
    if abs(spectr[i]) > np.max(abs(spectr))/5:
        true_spectr.append(spectr[i])
    else:
        true_spectr.append(0)
plt.plot(rfftfreq(len(t)), np.abs(true_spectr))
plt.title('Спектр без шума')
plt.xlabel('Частота, Hz')
plt.ylabel('Амплитуда, М')
plt.show()
#Вывод нужного сигнала без шума
output=irfft(true_spectr)
plt.plot(t, output, color='green')
plt.title('Выходной сигнал без шума')
plt.xlabel('Частота, Hz')
plt.ylabel('Амплитуда, М')
plt.grid(True)
plt.show()
#Сравнение сигналов
plt.plot(t, input, color='Blue', label='Входной сигнал')
plt.plot(t,input + stray, color='red', label='Зашумленный сигнал')
plt.plot(t, output, color = 'green', label='Выходной сигнал')
plt.legend()
plt.grid(True)
plt.show()
