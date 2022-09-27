# Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами, 
# выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!

import random

def get_list(list_len):
    result = []
    for i in range(list_len):
        result.append(random.randint(0, 50))
    return result

def mix_list(array):
    result = []
    for i in range(len(array)):
        element = random.choice(array)
        result.append(element)
        array.remove(element)
    return result

try:
    n = int(input("Размерность списка: "))
    if n > 0:
        my_list = get_list(n)
        print(my_list)
        my_list = mix_list(my_list)
        print(my_list)
    else: 
        print('Введите число > 0')
except:
    print('Введите целое число')
