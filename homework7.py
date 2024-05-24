my_dict = {"Denis": 1995, "Svetlana": 2000, "Vladimir": 1990}
print("Словарь:", my_dict)
print("Вывод значения:", my_dict.get("Denis"))
print("Вывод отсутвующего значения:", my_dict.get("Irina"))
my_dict.update({"Sergei": 2005, "Tamara": 2010})
age = my_dict.pop("Vladimir")
print("Удаленное значение:", age)
print("Модифицированный словарь:", my_dict)
my_set = {1, 1, 2, 555, 4, 4, 1, 2, True, "Привет", "Hello!"}
print("Множество:", my_set)
my_set.update({100.01, 20})
my_set.remove(555)
print("Обновленное множество:", my_set)
