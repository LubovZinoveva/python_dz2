# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def get_multiplication(n):
    result = [1]
    count = 1
    for i in range(2, n+1):
        count *= i
        result.append(count)
    return result

try:
    number = int(input('N = '))
    if number > 0:
        my_list = get_multiplication(number)
        print(my_list)
    else:
        print("Число должно быть положительным")
except:
    print('Ошибка, введите целое число > 0')