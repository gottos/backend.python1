import numpy as np
from numpy.random import default_rng
import collections


def cart2pol(x, y):
    """
  Функция по преобразованию координат из декартовой системы координат в полярную
  """
    rho = np.sqrt(x ** 2 + y ** 2)
    phi = np.arctan2(y, x)  # * 180 / np.pi  # получаем угол в градусах
    return rho, phi


def pol2cart(rho, phi):
    """
  Функция по преобразованию координат из полярной системы координат в декартовую
  """
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y


# Генерируем n точек на координатной плоскости
rng = default_rng()
n = input("Введите количество координат: ")
n = int(n)
x_y_array = rng.integers(low=-100, high=100, size=(n, 2))

# Переведем точки в полярную систему координат
# и формируем два словаря, ключами в которых будут положительные и отрицательные значения угла

positive_angle_radius_dict = {}  # I и II координатные четверти
negative_angle_radius_dict = {}  # III и IV координатные четверти

for x_y in x_y_array:
    (rho, phi) = cart2pol(x_y[0], x_y[1])
    if phi < 0:
        negative_angle_radius_dict[phi] = rho
    else:
        positive_angle_radius_dict[phi] = rho

# Получаем точки, отсортированные в порядке возрастания угла
# При этом точки с отрицательным углом располагаются в порядке убывания модуля значения
# (т.к. большой отрицательный угол находится в III квадранте,
# а обход по условию задачи должен быть против часовой стрелки, т.е. I -> II -> III -> IV)


positive_angle_radius_dict_sorted = collections.OrderedDict(sorted(positive_angle_radius_dict.items()))

negative_angle_radius_dict_sorted = collections.OrderedDict(sorted(negative_angle_radius_dict.items()))

# Формируем итоговый список из точек расположенных в нужном порядке и переведенных в декартовые координаты

result_list_cartesian = []
result_list_polar = []

for angle, radius in positive_angle_radius_dict_sorted.items():
    result_list_polar.append((angle, radius))
    result_list_cartesian.append(pol2cart(radius, angle))

for angle, radius in negative_angle_radius_dict_sorted.items():
    result_list_polar.append((angle, radius))
    result_list_cartesian.append(pol2cart(radius, angle))

print("result cartesian list {}".format(result_list_cartesian))
print("result polar list {}".format(result_list_polar))

# Находим расстояние между началом координат и точками массива
distances = np.sqrt(x_y_array[:, 0] * x_y_array[:, 0] + x_y_array[:, 1] * x_y_array[:, 1])

# Находим среднее, минимальное и максимальное расстояния
dist_mean = np.mean(distances)
dist_max = np.max(distances)
dist_min = np.min(distances)
print("Минимальное расстояние: ", dist_min)
print("Максимальное расстояние: ", dist_max)
print("Среднее расстояние: ", dist_mean)