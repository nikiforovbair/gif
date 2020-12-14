import pickle
from PIL import Image, ImageDraw
import numpy as np
import time
import os


print("Укажите путь к файлам (например: C:\ct-pickle-dumps\\" + "1\\")
_path = input()

start_time = time.time()

SPECTR_UINT = 4096 / 255
DIFF = 1024 / SPECTR_UINT

list_files = os.listdir(path=_path)


list_sort_files = list()

for i, item in enumerate(list_files):
    if(item.isdigit()):
        list_sort_files.append(int(item))

list_sort_files.sort()


frames = []

for file in list_sort_files:
    with open(_path + '\\' + str(file), 'rb') as f:
        data_ct = pickle.load(f)

    data_ct = data_ct / SPECTR_UINT
    data_ct = data_ct + DIFF
    f.close()
    image = Image.fromarray(np.uint8(data_ct), 'L')
    frames.append(image)
    print(file)

frames[0].save('gif_result.gif', format = 'GIF',
               append_images = frames[1:],
               save_all = True,
               duration = 300, Loop = 0)

print("Save file: gif_result.gif " + "End time: " +"--- %s seconds ---" % (time.time() - start_time))
print(input())
