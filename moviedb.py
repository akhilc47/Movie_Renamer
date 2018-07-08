import configparser
import json
import urllib.request
import urllib.parse

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['REMOTE']['api_key']


def get_response(movie_title: str='Titanic', page_num: int=1) -> dict:
    '''
    This function returns the response from tmdb for a given movie title.

    Input must be a string type movie title.

    If more than 20 results, page number can be used to access next pages.

    Output is a dictionary with the result(s).
    '''
    tmdb_url = config['REMOTE']['tmdb_url'] 
    movie_title = urllib.parse.quote(movie_title) # Escape non-ascii titles
    tmdb_query = '&query=' + '+'.join(movie_title.split())
    page = '&page='+str(page_num)
    response = urllib.request.urlopen(tmdb_url+api_key+tmdb_query+page).read()
    return json.loads(response)
