import os
from PIL import Image
from multiprocessing import Pool

SIZE = (75,75)
SAVE_DIRECTORY = r'C:\Users\lenovo\Desktop\p\1'

def get_image_paths(folder):
    return (os.path.join(folder, f) for f in os.listdir(folder) if 'jpg' in f)

def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE)
    base, fname = os.path.split(filename)
    save_path = os.path.join(SAVE_DIRECTORY, fname)
    im.save(save_path)
    print('Finsh %s'%save_path)

folder = r'C:\Users\lenovo\Desktop\SB'

images = get_image_paths(folder)
pool = Pool()
pool.map(create_thumbnail, images)
pool.close()
pool.join()
