import os

folder = os.path.abspath('some_data')
all_files = [item for item in os.scandir(folder) if os.path.isfile(os.path.join(folder, item))]
dict_stat = {10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0}
for file in all_files:
    for n in range(1, 6):
        size = 10 ** n
        if os.stat(os.path.join(folder, file)).st_size < size:
            dict_stat[size] += 1
            break
print(dict_stat)
