#Ввод значения
s = input("Enter the number:")
s = s.strip()

#Проверка корректоности ввода
if not (1 <= len(s) <= 2):
    print("Invalid input")
    exit(0)

#Множество всех допустимых чисел
digits = "0123456789ABCDF"

if s [0] not in digits:
    print("Invalid input")
    exit(1)

if len(s) >= 2 and s[1] not in digits:
    print("Invalid input")
    exit(2)

#Преобразование в число
n = int(s)

#Проверка корректности диапазона
if not(0 <= n <= 99):
     print("Invalid input")
     exit(3)

#Перевод числа в пропись
answer = ""

if n // 10 == 2:
         answer += "Двадцать "
elif n // 10==3:
         answer += "Тридцать "
elif n // 10==4:
         answer += "Сорок "
elif n // 10==5:
         answer += "Пятьдесят "
elif n // 10==6:
         answer += "Шестьдесят "
elif n // 10==7:
         answer += "Семьдесят "
elif n // 10==8:
         answer += "Восемьдесят "
elif n // 10==9:
         answer += "Девяносто "


if n == 0:
             answer += "Ноль"
if n % 10 == 1:
             answer += "один"
elif n % 10 == 2:
             answer += "два"
elif n % 10 == 3:
             answer += "три"
elif n % 10 == 4:
             answer += "четыре"
elif n % 10 == 5:
             answer += "пять"
elif n % 10 == 6:
             answer += "шесть"
elif n % 10 == 7:
             answer += "семь"
elif n % 10 == 8:
             answer += "восемь"
elif n % 10 == 9:
             answer += "девять"

if n == 10:
             answer = "Десять"
elif n == 11:
             answer = "Одиннадцать"
elif n == 12:
             answer = "Двенадцать"
elif n == 13:
             answer = "Тринадцать"
elif n == 14:
            answer = "Четырнадцать"
elif n == 15:
             answer = "Пятнадцать"
elif n == 16:
             answer = "Шестнадцать "
elif n == 17:
             answer = "Семнадцать"
elif n == 18:
             answer = "Восемьнадцать"
elif n == 19:
             answer = "Девятнадцать"

#Вывод
print(f"Result: {answer}")

