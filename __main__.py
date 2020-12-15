import pickle
from PIL import Image, ImageDraw
import numpy as np
import time
import os



def check_int_and_sort(list_files):
    list_sort_files = list()

    for item in list_files:
        if(item.isdigit()):
            list_sort_files.append(int(item))

    list_sort_files.sort()
    return list_sort_files

def create_images_is_binary_files_ct(_path, list_files, color_module):
    SPECTR_UINT = 4096 / 255
    DIFF = 1024 / SPECTR_UINT
    
    frames = []
    for file in list_files:
        with open(_path + '\\' + str(file), 'rb') as f:
            data_ct = pickle.load(f)
        f.close()

        data_ct = data_ct / SPECTR_UINT
        data_ct = data_ct + DIFF
        
        image = Image.fromarray(np.uint8(data_ct), 'L').convert(color_module)
        frames.append(image)
        print(file)
    return frames


def main():
    print("Укажите путь к папке (например: C:\ct-pickle-dumps\\) **ОСТОРОЖНО РЕКУРСИЯ!**")
    _path = input()
    print("Укажите цветовой модуль (например: RGB, RGBA, L - grayscale)")
    color_module = input()

    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(_path):
        list_files = filenames
        list_sort_files = check_int_and_sort(list_files)
        
        if (len(list_sort_files) == 0):
            continue

        frames = create_images_is_binary_files_ct(dirpath, list_sort_files, color_module)

        frames[0].save(str(os.path.basename(dirpath)) + "_result_" + ("%s_sec" % round((time.time() - start_time), 5)) + ".gif", format = 'GIF',
            append_images = frames[1:],
            save_all = True, Loop = 0)
    

    print("Save files in " + str(os.path.abspath(".")) + " End time: " + "--- %s seconds ---" % (time.time() - start_time))
    input()

if __name__ == "__main__":
    main()
    pass


