'''
Keep all helper functions needed for renamer.py here.
'''


def preproc_title(bad_title: str="Titanic")-> list:
    '''
    Cleans up the title and extract year if any.
    '''
    bad_title = bad_title.replace('.', ' ')
    bad_title = bad_title.replace('(', ' ').replace(')', ' ')
    bad_title = bad_title.replace('[', ' ').replace(']', ' ')
    bad_title = bad_title.split()
    year = 0
    title_and_year = []
    for token in bad_title:
        if token.isdigit() and (int(token) > 1900 and int(token) < 2020):
            year = int(token)
            break
        title_and_year.append(token)
    title_and_year.append(year)
    return title_and_year
