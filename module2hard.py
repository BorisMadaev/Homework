number = int(input('Введите число от 3 до 20 '))
if 2 < number < 21:
    result = ''
    list_1 = 0
    povtor = 0
    for i in range(1, 21):
        for j in range(1, 21):
            if (number % (i + j) == 0 or number == i + j) and i != j:
                if list_1 == 0:
                    list_1 = [[i, j]]
                else:
                    list_1 = list_1 + [[i, j]]
                for k in range(len(list_1)):
                    if int(list_1[k][0]) == j and int(list_1[k][1]) == i:
                        povtor = 1
                if povtor == 1:
                    list_1.remove([i, j])
                else:
                    result = result + str(i) + str(j)
                povtor = 0
    print(f'Пароль: {result}')
else:
    print("Вы ввели неправильное число!")
