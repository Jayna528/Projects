import shutil
import os

path = 'C:/Users/Owner/Desktop/Jayna WhiteHat/Project 99'
files = os.listdir(path)

for i in files:
    name, ext = os.path.splitext(i)
    ext = ext[1:]

    if ext == '':
        continue

    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + i, path + '/' + ext + '/' + i)
    
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + i, path + '/' + ext + '/' + i)
