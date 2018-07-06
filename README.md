# Movie_Renamer
Find correct title of media files from open online databases.

## renamer.py
Execute this file to loop through all the files/folders in the path. Correct the names of files/folders.

## moviedb.py
get_response() returns result from TMDB API for a given title(string).

## helpers.py
- preproc_title() cleans the title directly obtained from file/folder.
- get_original_title() runs algorithm to find correct title for a given list of tokens.
