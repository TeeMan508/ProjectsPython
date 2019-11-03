import math
#Сумма всех чисел от 1 до 2^25
print(sum(range(1, 2**25+1)))

#Вывод развернутой строки в консоль
print(input("String Input: ")[::-1])

#Факториал 1000
print(str(math.factorial(1000)))

#Вывод всех клеточек поля для игры в морской бой
print([n + str(i) for i in range(1,11) for n in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']])

#Удвоение всех нечетных числе списка
print([k*2 if k % 2 == 1 else k for k in [1, 2, 3, 4, 5, 6, 7, 8, 9]])