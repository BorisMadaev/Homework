import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
time_1_start = time.time()
for i in range(len(filenames)):
    read_info(filenames[i])
time_1_end = time.time()
time_1 = time.strftime("%H:%M:%S", time.gmtime(time_1_end - time_1_start))
print(f'{time_1[1:]}{str(round(time_1_end - time_1_start - int(time_1_end - time_1_start), 6))[1:]} (линейный)')

"""
# Многопроцессный
if __name__ == '__main__':
    time_2_start = time.time()
    with Pool(processes=4) as pool:
        process = pool.map(read_info, filenames)
    time_2_end = time.time()
    time_2 = time.strftime("%H:%M:%S", time.gmtime(time_2_end - time_2_start))
    print(f'{time_2[1:]}{str(round(time_2_end - time_2_start - int(time_2_end - time_2_start), 6))[1:]} (многопроцессорный)')
"""
