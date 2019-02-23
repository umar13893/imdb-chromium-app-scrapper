# Site Specific Imports Start
from bottle import route, request, response
from json import dumps
from app_movies.functions import (
    get_movies_box_office,
    get_coming_movies_dates,
    get_coming_soon_movies,
    get_movies_in_theatre,
    get_oscar_winners,
    get_popular_trailers,
    get_recent_trailers,
    get_tv_trailers,
    get_top_rated_movies,
    get_top_rated_indian,
    get_popular_movies,
    get_trailer_video_id,
)
# End Site Specific Imports

# Getting box office movies
@route('/box_office_movies', method="GET")
def box_office_movies():
    box_office_movies = get_movies_box_office()
    response.content_type = 'application/json'
    return dumps(box_office_movies)


# Getting coming soon movies date
@route('/coming_soon_movies_dates', method="GET")
def coming_soon_movies_dates():
    coming_soon_movies_dates = get_coming_movies_dates()
    response.content_type = 'application/json'
    return dumps(coming_soon_movies_dates)


# Getting coming soon movies
@route('/coming_soon_movies', method="GET")
def coming_soon_movies():
    date_string = request.query.date_string
    coming_soon_movies = get_coming_soon_movies(date_string)
    response.content_type = 'application/json'
    return dumps(coming_soon_movies)


# Getting theatre movies
@route('/theatre_movies', method="GET")
def theatre_movies():
    theatre_movies = get_movies_in_theatre()
    response.content_type = 'application/json'
    return dumps(theatre_movies)


# Getting oscar winners
@route('/oscar_winners', method="GET")
def oscar_winners():
    oscar_winners = get_oscar_winners()
    response.content_type = 'application/json'
    return dumps(oscar_winners)

# Getting popular trailers
@route('/popular_trailers', method="GET")
def popular_trailers():
    popular_trailers = get_popular_trailers()
    response.content_type = 'application/json'
    return dumps(popular_trailers)

# Getting recent trailers
@route('/recent_trailers', method="GET")
def recent_trailers():
    recent_trailers = get_recent_trailers()
    response.content_type = 'application/json'
    return dumps(recent_trailers)

# Getting TV trailers
@route('/tv_trailers', method="GET")
def tv_trailers():
    tv_trailers = get_tv_trailers()
    response.content_type = 'application/json'
    return dumps(tv_trailers)


# Getting popular movies
@route('/popular_movies', method="GET")
def popular_movies():
    popular_movies = get_popular_movies()
    response.content_type = 'application/json'
    return dumps(popular_movies)


# Getting top rated indian movies
@route('/top_rated_movies', method="GET")
def top_rated_movies():
    top_rated_movies = get_top_rated_movies()
    response.content_type = 'application/json'
    return dumps(top_rated_movies)


# Getting top rated indian movies
@route('/top_rated_indians', method="GET")
def top_rated_indians():
    top_rated_indian_movies = get_top_rated_indian()
    response.content_type = 'application/json'
    return dumps(top_rated_indian_movies)


# Getting video trailer id
@route('/video_trailer_id', method="GET")
def video_trailer_id():
    url = request.query.url
    video_trailer_id = get_trailer_video_id(url)
    response.content_type = 'application/json'
    return dumps(video_trailer_id)


# Connecting to eel
import eel
eel.init("web")
web_app_options = {
    'mode': "chrome",
}
eel.start("main.html", options=web_app_options)
