def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print("Функция с параметрами по умолчанию:")
print_params()
print_params(0)
print_params(1, 'два')
print_params(3, 'сто', False)
print_params(1, 1, 1)
print_params(b=25)
print_params(c=[1,2,3])
print()
print("Распаковка параметров:")
values_list = [1, False, "Вперед!"]
values_dict = {'a': 100, 'b': 'сто', 'c': 100.1001}
print_params(*values_list)
print_params(**values_dict)
print()
print("Распаковка + отдельные параметры:")
values_list_2 = [123.123123, 'новая строка']
print_params(*values_list_2, 42)
