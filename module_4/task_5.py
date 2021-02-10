from functools import reduce

def my_func(el, next_el):
    yield el * next_el

new_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(my_func, new_list))
#ошибки нет, но и результат не выдаёт, почему?