import os
import shutil

source = 'C:/Users/Owner/Desktop/Jayna WhiteHat/The-temper-game-main/'
destination = 'C:/Users/Owner/Desktop/Jayna WhiteHat/Project 99/'
files = os.listdir(source)
for i in files:
    shutil.copy(source + i, destination)

