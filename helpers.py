from moviedb import get_response
import re

'''
Keep all helper functions needed for renamer.py here.
'''


def preproc_title(bad_title: str="Titanic")-> list:
    '''
    Cleans up the title and extract year if any.

    Returns list with tokens extracted plus year(=0 default).
    '''
    bad_title = re.sub((r'[\[|\]|,|.|\(|\)]'),' ',bad_title)
    year = 0
    title_and_year = []
    for token in bad_title.split():
        if token.isdigit() and (int(token) > 1900 and int(token) < 2020):
            year = int(token)
            break
        title_and_year.append(token)
    title_and_year.append(year)
    return title_and_year


def get_original_title(old_title: list=["Titanic"], year: int=1997):
    '''
    Algorithm for using the tokens with year to find the correct title.

    Returns an empty string if no match was found.
    '''
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
    return original_title
