import random
import threading
import time
from queue import Queue


class Table:
    number = 0
    guest = ''

    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        num = random.randint(3, 10)
        time.sleep(num)


class Cafe:
    queue = Queue()

    def __init__(self, *args):
        self.tables = args

    def guest_arrival(self, *args):
        self.guests = args
        for i in range(len(self.guests)):
            count_free_table = 0
            for j in range(len(self.tables)):
                if self.tables[j].guest is None:
                    count_free_table += 1
                    self.tables[j].guest = self.guests[i].name
                    if j == 0:
                        self.thread1 = threading.Thread(target=Guest.run, args=(self.tables[j].guest,), daemon=True)
                        self.thread1.start()
                    if j == 1:
                        self.thread2 = threading.Thread(target=Guest.run, args=(self.tables[j].guest,), daemon=True)
                        self.thread2.start()
                    if j == 2:
                        self.thread3 = threading.Thread(target=Guest.run, args=(self.tables[j].guest,), daemon=True)
                        self.thread3.start()
                    if j == 3:
                        self.thread4 = threading.Thread(target=Guest.run, args=(self.tables[j].guest,), daemon=True)
                        self.thread4.start()
                    if j == 4:
                        self.thread5 = threading.Thread(target=Guest.run, args=(self.tables[j].guest,), daemon=True)
                        self.thread5.start()
                    print(f'{self.tables[j].guest} сел(-а) за стол номер {j+1}')
                    break
                elif j == len(self.tables)-1 and count_free_table == 0:
                    self.queue.put(self.guests[i].name)
                    print(f'{self.guests[i].name} в очереди')

    def discuss_guests(self):
        free_tables = 0
        while True:
            for i in (range(len(tables))):
                if self.tables[i].guest is not None:
                    if not self.thread1.is_alive() and i == 0:
                        free_tables += 1
                        print(f'{self.tables[i].guest} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {i+1} свободен')
                        self.tables[i].guest = None
                    elif not self.thread2.is_alive() and i == 1:
                        free_tables += 1
                        print(f'{self.tables[i].guest} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {i + 1} свободен')
                        self.tables[i].guest = None
                    elif not self.thread3.is_alive() and i == 2:
                        free_tables += 1
                        print(f'{self.tables[i].guest} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {i + 1} свободен')
                        self.tables[i].guest = None
                    elif not self.thread4.is_alive() and i == 3:
                        free_tables += 1
                        print(f'{self.tables[i].guest} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {i + 1} свободен')
                        self.tables[i].guest = None
                    elif not self.thread5.is_alive() and i == 4:
                        free_tables += 1
                        print(f'{self.tables[i].guest} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {i + 1} свободен')
                        self.tables[i].guest = None
                elif not self.queue.empty():
                    free_tables -= 1
                    self.tables[i].guest = self.queue.get()
                    print(f'{self.tables[i].guest} вышел(-ла) из очереди и сел(-а) за стол номер {i+1}')
                    if i == 0:
                        self.thread1 = threading.Thread(target=Guest.run, args=(self.tables[i].guest,), daemon=True)
                        self.thread1.start()
                    if i == 1:
                        self.thread2 = threading.Thread(target=Guest.run, args=(self.tables[i].guest,), daemon=True)
                        self.thread2.start()
                    if i == 2:
                        self.thread3 = threading.Thread(target=Guest.run, args=(self.tables[i].guest,), daemon=True)
                        self.thread3.start()
                    if i == 3:
                        self.thread4 = threading.Thread(target=Guest.run, args=(self.tables[i].guest,), daemon=True)
                        self.thread4.start()
                    if i == 4:
                        self.thread5 = threading.Thread(target=Guest.run, args=(self.tables[i].guest,), daemon=True)
                        self.thread5.start()
            if self.queue.empty() and free_tables == len(tables):
                break
        print(f'Завершение обслуживания')



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
