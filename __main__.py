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

def create_images_is_binary_files_ct(_path, list_files):
    SPECTR_UINT = 4096 / 255
    DIFF = 1024 / SPECTR_UINT
    
    frames = []
    for file in list_files:
        with open(_path + '\\' + str(file), 'rb') as f:
            data_ct = pickle.load(f)
        f.close()

        data_ct = data_ct / SPECTR_UINT
        data_ct = data_ct + DIFF
        
        image = Image.fromarray(np.uint8(data_ct), 'L')
        frames.append(image)
        print(file)
    return frames


def main(): 
    print("Укажите путь к файлам (например: C:\ct-pickle-dumps\\" + "1\\")
    _path = input()

    start_time = time.time()


    list_files = os.listdir(path=_path)
    list_sort_files = check_int_and_sort(list_files)

    frames = create_images_is_binary_files_ct(_path, list_sort_files)

    frames[0].save('gif_result.gif', format = 'GIF',
                   append_images = frames[1:],
                   save_all = True, Loop = 0)

    print("Save file: gif_result.gif " + "End time: " +"--- %s seconds ---" % (time.time() - start_time))
    print(input())

if __name__ == "__main__":
    main()

