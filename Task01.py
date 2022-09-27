# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать. *Пример:*
# 6782 -> 23
# 0,56 -> 11

def sum_numbers(num):
    sum = 0
    bite_num = int(num)
    while bite_num > 0:
        sum +=  bite_num % 10
        bite_num //= 10

    while num % 1 != 0:
        num = round(num * 10, 8)
        sum += int(num % 10)
    return sum

try:
    number = float(input('Число = '))
    total = sum_numbers(number)
    print(total)
except:
    print('Введите целое или вещественное число')
