# Запросите у пользователя четыре числа (файл numbers.py). Отдельно сложите первые два и
# отдельно вторые два. Разделите первую сумму на вторую. Выведите результат на экран так,
# чтобы ответ содержал две цифры после запятой.

a = int(input("Enter the first number :"))
b = int(input("Enter the following number:"))
c = int(input("Enter the following number:"))
d = int(input("Enter the last number:"))
x =(a+b)/(c+d)
print("%.2f" % x)