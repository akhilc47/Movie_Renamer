import json
import urllib.request
import urllib.parse

with open('config.txt') as keyh:
    api_key = keyh.read().strip()


def get_response(movie_title: str='Titanic') -> dict:
    '''
    This function returns the response from tmdb for a given movie title.

    Input must be a string type movie title.

    Output is a dictionary with the result(s).
    '''
    tmdb_url = 'https://api.themoviedb.org/3/search/movie?api_key='
    movie_title = urllib.parse.quote(movie_title) # Escape non-ascii titles
    tmdb_query = '&query=' + '+'.join(movie_title.split())
    response = urllib.request.urlopen(tmdb_url+api_key+tmdb_query).read()
    return json.loads(response)
