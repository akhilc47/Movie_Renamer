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

bad_title = 'Molly\'s.Game.2017.1080p.BluRay.x264-[YTS.AM].mp4'.replace('.', ' ')
bad_title = bad_title.replace('(', ' ').replace(')', ' ')
bad_title = bad_title.replace('[', ' ').replace(']', ' ')
bad_title = bad_title.split()
print(bad_title)
year = 0
new_title_list = []
for token in bad_title:
    if token.isdigit() and (int(token) > 1900 and int(token) < 2020):
        print("year of release: ", token)
        year = int(token)
        break
    new_title_list.append(token)
if year:
    print(new_title_list)
    query_title = ""
    original_title = ""
    for token in reversed(new_title_list):
        query_title = token + " " + query_title
        print(query_title)
        js_response = get_response(query_title)
        #pprint.pprint(js_response)
        if js_response['total_results'] == 0:
            print ("Could not find correct title")
        elif js_response['total_results'] == 1:
            if int(js_response['results'][0]['release_date'][0:4]) == year:
                print ("Found the original title")
                original_title = js_response['results'][0]['title']
                break
        elif js_response['total_results'] > 20:
            continue
        else:
            for result in js_response['results']:
                if not result['release_date']:
                    continue
                elif year != int(result['release_date'][0:4]):
                    continue
                else:
                    print("Found matching year")
                    pprint.pprint(result)
                print (result['title'][-len(query_title):], query_title)
                if result['title'][-len(query_title):] == query_title.strip():
                    print("Found partially matching title")
                    if original_title == "":
                        original_title = result['title']
                    else:
                        print("Multiple matches, add more token to query")
                        break
                    print(original_title)
            if original_title:
                break
if original_title:
    print ("Found original title:", original_title)

