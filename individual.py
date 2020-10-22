# Вариант 1
# Даны два числа. Найти среднее арифметическое и среднее геометрическое их модулей.

import math
a = abs(float(input("Enter the first number:")))
b = abs(float(input("Enter the second number:")))
x = (a+b)/2
y = math.sqrt(a*b)
print(f"the arithmetic mean {x}")
print(f"the geometric mean {y}")
