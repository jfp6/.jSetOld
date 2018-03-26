
import os
import sys


dirPath = os.getcwd()
sys.path.insert( 0, dirPath)
dirPathCase = dirPath + ''
if not os.path.exists(dirPathCase):
    os.makedirs(dirPathCase)


for file in os.listdir(dirPathCase):
    if file.endswith(".stl"):
        print(file)
        name = file[:-4]
        print(name)
        sourceFile = open(file,'r')
        target = file + "t" 
        targetFile = open(target,'w')
        first_row = True
        for row in sourceFile:
            if first_row:
                row = 'solid ' + name + '\n'
                first_row = False
            targetFile.write(row)
        sourceFile.close()
        targetFile.close()
        os.remove(file)
        os.rename(target,target[:-1])

