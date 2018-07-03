import json, urllib.request, pprint

with open('config.txt') as keyh:
    api_key = keyh.read().strip()


def get_response(movie_title: str='Titanic') -> dict:
    ''' 
    This function returns the response from tmdb for a 
    given movie title. 
    '''
    tmdb_url = 'https://api.themoviedb.org/3/search/movie?api_key='
    tmdb_query = '&query=' + '+'.join(movie_title.split())
    response = urllib.request.urlopen(tmdb_url+api_key+tmdb_query).read()
    return json.loads(response)

bad_title = 'www.TamilMV.vin - Aadhi (2018) - Malayalam - HDRip - 700MB - x264 - 1CD - MP3.mkv'.replace('.', ' ')
bad_title = bad_title.replace('(', ' ').replace(')', ' ')
bad_title = bad_title.replace('[', ' ').replace(']', ' ')
bad_title = bad_title.split()
print(bad_title)
for token in bad_title:
    if token.isdigit() and (int(token) > 1900 and int(token) < 2020):
        print(token)

#js_response = get_response()
#print (js_response['total_results'])
#pprint.pprint(js_response)
#for i in range(js_response['total_results']):
#    print (i, js_response['results'][i]['title'])
