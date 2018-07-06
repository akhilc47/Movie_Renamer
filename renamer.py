import pprint
import os
from moviedb import get_response
from helpers import preproc_title

path = "E:/Downloads/malayalam"
fout = open('output.csv', 'w')
for item in os.listdir(path):
    title_with_year = preproc_title(item)
    old_title = title_with_year[:-1]
    year = title_with_year[-1]
    original_title = ""
    for i in range(len(old_title)):
        query_title = ' '.join(old_title[i:])
        web_response = get_response(query_title)
        if web_response['total_results'] == 0:
            print(query_title, "0 results")
            continue
        print(query_title, "Looping through results")
        for movie in web_response['results']:
            if not (year and movie['release_date']):
                continue
            elif year != int(movie['release_date'][0:4]):
                continue
            print("YEAR MATCHED,", "query:", year, "response:",
                  movie['release_date'])
            if movie['title'] == query_title.strip():
                print("TITLE MATCHED,", "query:", query_title,
                      "response:", movie['title'])
                original_title = movie['title']
                break
        if original_title:
            break
        if web_response['total_results'] > 20:
            print("Too many results and nothing matches on first page")
    if original_title:
        fout.write(item+","+original_title+"\n")
    else:
        fout.write(item+", couldn't find original title"+"\n")
    print("*"*30)
fout.close()
