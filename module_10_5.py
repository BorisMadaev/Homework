import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]


# Линейный вызов
time_start = datetime.datetime.now()
for i in range(len(filenames)):
    read_info(filenames[i])
time_end = datetime.datetime.now()
print(f'{time_end - time_start} (линейный)')

"""
# Многопроцессный
if __name__ == '__main__':
    time_start = datetime.datetime.now()
    with Pool(processes=4) as pool:
        process = pool.map(read_info, filenames)
    time_end = datetime.datetime.now()
    print(f'{time_end - time_start} (многопроцессорный)')
"""
