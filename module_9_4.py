import random


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        random_word = random.choice(self.words)
        return random_word


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for i in range(len(data_set)):
                file.write(f'{str(data_set[i])}\n')
#        with open(file_name, 'r', encoding='utf-8') as file:
#            for line in file:
#                print(line[:-1])
    return write_everything


# 1
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

# 2
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# 3
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
