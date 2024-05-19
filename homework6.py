my_list = ["Апельсин", "Виноград", "Дыня", "Груша", "Персик", "Слива", "Кокос"]
print('Список:', my_list)
print("Первый элемент :", my_list[0])
print("Последний элемент :", my_list[-1])
print("Подсписок:", my_list[2:5])
my_list[2] = "Яблоко"
print("Измененный список:", my_list)
print()
my_dict = {"Apple": "Яблоко", "Peach": "Персик", "Coconut": "Кокос", "Grape": "Виноград"}
print("Словарь:", my_dict)
print("Перевод:", my_dict.get("Grape"))
my_dict.update({"Apple": "Эпл", "Orange": "Апельсин"})
print("Измененный словарь:", my_dict)
