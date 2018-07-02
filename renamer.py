import json, urllib.request, pprint

tmdb_url = 'https://api.themoviedb.org/3/search/movie?api_key='
movie_title = 'wood job'
tmdb_query = '&query='+'+'.join(movie_title.split())
response = urllib.request.urlopen(tmdb_url+api_key+tmdb_query).read()
js_response = json.loads(response)

print (js_response['total_results'])
pprint.pprint(js_response)

#for i in range(js_response['total_results']):
#    print (i, js_response['results'][i]['title'])
