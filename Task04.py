# Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между 
# ними в N-мерном пространстве.

def get_point_coordinates(n):
    point = []
    for i in range(n):
        point.append(int(input(f'{i + 1} = ')))
    return point
    
def distance(D, point1, point2):
    result = (point2[0] - point1[0])**2 
    for i in range(1,D):
        result += (point2[i] - point1[i])**2 
    return result**0.5
    
try:
    N = int(input('N = '))
    print(f'Введите {N} координат(ы) первой точки')
    X = get_point_coordinates(N)
    print(f'Введите {N} координат второй точки')
    Y = get_point_coordinates(N)
    my_distance = distance(N, X, Y)
    print(f'Расстояние между точками = {round(my_distance, 2)}')
except:
    print('Задайте координаты целыми числами > 0')

