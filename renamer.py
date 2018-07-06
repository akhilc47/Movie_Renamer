import pprint
import os
from helpers import preproc_title, get_original_title

path = "E:/Downloads/malayalam"
fout = open('output.csv', 'w')
for item in os.listdir(path):
    title_with_year = preproc_title(item)
    old_title = title_with_year[:-1]
    year = title_with_year[-1]
    original_title = get_original_title(old_title, year)
    if original_title:
        fout.write(item+","+original_title+"\n")
    else:
        fout.write(item+", couldn't find original title"+"\n")
fout.close()
