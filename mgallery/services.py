import requests
from MovieWebsite import settings


def get_movie_data(movie_title):
    r = requests.get('https://api.themoviedb.org/3/search/movie?api_key=' +
                     settings.MOVIE_DB_API_KEY +
                     '&query=' + movie_title)
    json = r.json()

    if json is not None:
        movie_data = json['results'][0]
        movie_data['youtube_key'] = get_video(str(movie_data['id']))
    else:
        movie_data = {}

    return movie_data


def get_video(movie_id):
    r = requests.get('https://api.themoviedb.org/3/movie/' +
                     movie_id +
                     '?api_key=' +
                     settings.MOVIE_DB_API_KEY +
                     '&append_to_response=videos')

    json = r.json()

    if json is not None:
        youtube_key = json['videos']['results'][0]['key']
    else:
        youtube_key = ''

    return youtube_key
