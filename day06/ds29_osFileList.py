# date : 2024-02-19
# desc : 윈도우 파일 리스트

import os

fnameAry = []
folderName = 'C:\Sources\ds-and-algorithm/day06'

for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)

print(fnameAry)   
print(len(fnameAry))

fnameAry.sort(reverse = True) # 역순 정렬
print(fnameAry)