immutable_var = (1, True, "Привет!")
print(immutable_var)
# immutable_var [0] = 3
# Ошибка!
# отдельный элемент кортежа менять нельзя, надо перезаменять весь кортеж целиком.
# Пример,
# immutable_var = (3, True, "Привет!")
# print(immutable_var)
# Исключение - если в кортеж входит список, внутренние отдельные элементы списка можно спокойно менять.
# Пример:
# immutable_var = ([1,1], True, "Привет!")
# print(immutable_var)
# immutable_var [0][0] = 3
# print(immutable_var)
mutable_list = [1, 15, "Апельсин"]
mutable_list[1] = True
print(mutable_list)
