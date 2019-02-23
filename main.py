# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()
# End of imports for django
# Site Specific Imports Start
from bottle import route, template, request
from django.http import JsonResponse
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
    return JsonResponse(box_office_movies, safe=False)


# Getting coming soon movies date
@route('/coming_soon_movies_dates', method="GET")
def coming_soon_movies_dates():
    coming_soon_movies_dates = get_coming_movies_dates()
    return JsonResponse(coming_soon_movies_dates, safe=False)


# Getting coming soon movies
@route('/coming_soon_movies', method="GET")
def coming_soon_movies():
    date_string = request.query.date_string
    coming_soon_movies = get_coming_soon_movies(date_string)
    return JsonResponse(coming_soon_movies, safe=False)


# Getting theatre movies
@route('/theatre_movies', method="GET")
def theatre_movies():
    theatre_movies = get_movies_in_theatre()
    return JsonResponse(theatre_movies, safe=False)


# Getting oscar winners
@route('/oscar_winners', method="GET")
def oscar_winners():
    oscar_winners = get_oscar_winners()
    return JsonResponse(oscar_winners, safe=False)

# Getting popular trailers
@route('/popular_trailers', method="GET")
def popular_trailers():
    popular_trailers = get_popular_trailers()
    return JsonResponse(popular_trailers, safe=False)

# Getting recent trailers
@route('/recent_trailers', method="GET")
def recent_trailers():
    recent_trailers = get_recent_trailers()
    return JsonResponse(recent_trailers, safe=False)

# Getting TV trailers
@route('/tv_trailers', method="GET")
def tv_trailers():
    tv_trailers = get_tv_trailers()
    return JsonResponse(tv_trailers, safe=False)


# Getting popular movies
@route('/popular_movies', method="GET")
def popular_movies():
    popular_movies = get_popular_movies()
    return JsonResponse(popular_movies, safe=False)


# Getting top rated indian movies
@route('/top_rated_movies', method="GET")
def top_rated_movies():
    top_rated_movies = get_top_rated_movies()
    return JsonResponse(top_rated_movies, safe=False)


# Getting top rated indian movies
@route('/top_rated_indians', method="GET")
def top_rated_indians():
    top_rated_indian_movies = get_top_rated_indian()
    return JsonResponse(top_rated_indian_movies, safe=False)


# Getting video trailer id
@route('/video_trailer_id', method="GET")
def video_trailer_id():
    url = request.query.url
    video_trailer_id = get_trailer_video_id(url)
    return JsonResponse(video_trailer_id, safe=False)


# Connecting to eel
import eel
eel.init("web")
web_app_options = {
    'mode': "chrome",
}
eel.start("main.html", options=web_app_options)
