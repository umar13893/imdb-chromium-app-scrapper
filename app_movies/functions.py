from bs4 import BeautifulSoup
import requests

# Cool functions here

# Getting box office movies
def get_movies_box_office():


    """
    Getting box office movies
    :return: List of box office movies
    """
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/chart/boxoffice/"
    top_movies_list = []
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        table_rows = soup.find_all("tr")
        for row in table_rows:
            context_data = {}
            table_data_poster = row.find_all("td", {"class": "posterColumn"})

            if table_data_poster:
                for poster in table_data_poster:
                    post_image_list = poster.find_all("img")
                    if post_image_list:
                        poster_image = post_image_list[0].get("src")
                        context_data["movie_poster"] = poster_image

            table_data_title = row.find_all("td", {"class": "titleColumn"})
            if table_data_title:
                for title_col in table_data_title:
                    # Mobile Title List
                    title_list = title_col.find_all("a")
                    if title_list:
                        title = title_list[0].text
                        context_data["movie_title"] = title
                    # Movie Link List
                    url_link_list = title_col.find_all("a")
                    if url_link_list:
                        url_link = url_link_list[0].get("href")
                        context_data["movie_link"] = base_url + url_link

            table_data_weekend = row.find_all("td", {"class": "ratingColumn"})
            if table_data_weekend:
                context_data["weekend"] = str(table_data_weekend[0].text).strip()


            table_data_gross = row.find_all("span", {"class": "secondaryInfo"})
            if table_data_gross:
                context_data["gross"] = str(table_data_gross[0].text).strip()


            # Appending context data top movie
            top_movies_list.append(context_data)

        top_movies_list = [x for x in top_movies_list if x != {}]
        return {
            "status": True,
            "top_movies_list": list(top_movies_list),
            "table_headings": ["Poster", "Title", "Weekend", "Gross", ""],
        }
    else:
        return {
            "status": False,
            "message": "Not able to get the data."
        }


# Getting coming soon movies date
def get_coming_movies_dates():

    """
    Getting soon movies dates
    :return: List of coming soon movies dates
    """

    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/movies-coming-soon"
    list_sort_options = []
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        sort_field = soup.find_all("select", {"class": "sort_field"})
        if sort_field:
            sort_field_select = sort_field[0]
            sort_options = sort_field_select.find_all("option")
            if sort_options:
                for sort_option in sort_options:
                    context_sort = {}
                    option_text = str(sort_option.text).strip()
                    option_value = str(sort_option.get("value")).strip()
                    context_sort["option_text"] = option_text
                    context_sort["option_value"] = option_value
                    list_sort_options.append(context_sort)

            list_sort_options = [x for x in list_sort_options if x != {}]
        return {
            "status": True,
            "sort_options": list(list_sort_options)
        }
    else:

        return {
            "status": False,
            "message": "Not able to get the data."
        }

# Getting coming soon movies
def get_coming_soon_movies(date_url_string):

    """
    Getting coming soon movies
    :return: List of coming soon movies
    """
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com" + date_url_string
    movies_list = []
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        item_lists = soup.find_all("div", {"class": "list_item"})
        for item in item_lists:
            movie_context = {}

            # getting poster image
            poster_image_list = item.find_all("img", {"class": "poster"})
            if poster_image_list:
                poster_image = poster_image_list[0].get("src")
                movie_context["poster_image"] = str(poster_image).strip()

            # Getting movie heading
            movie_heading_list = item.find_all("h4")
            if movie_heading_list:
                movie_heading = str(movie_heading_list[0].text).strip()
                movie_context["movie_heading"] = str(movie_heading).strip()

            # Getting movie link
            movie_link_list = item.find_all("a")
            if movie_link_list:
                movie_href = movie_link_list[0].get("href")
                movie_href = str(base_url + movie_href)
                movie_context["movie_href"] = str(movie_href).strip()


            # Movie time
            movie_time_list = item.find_all("time")
            if movie_time_list:
                time = movie_time_list[0].text
                movie_context["movie_time"] = str(time).strip()


            # Getting movie types
            movie_type_list = item.find_all("p", {"class": "cert-runtime-genre"})
            if movie_type_list:
                for movie_type in movie_type_list:
                    movie_spans = movie_type.find_all("span")
                    list_of_text = [x.text for x in movie_spans]
                    types_movie = " ".join(list_of_text)
                    movie_context["movie_types"] = str(types_movie).strip()


            # Getting movie description
            movie_desc_list = item.find_all("div", {"class": "outline"})
            if movie_desc_list:
                description = str(movie_desc_list[0].text).strip()
                movie_context["description"] = str(description).strip()

            movies_list.append(movie_context)


        movie_list = [x for x in movies_list if x != {}]
        return {
            "status": True,
            "movie_list": list(movie_list),
            "table_headings": ["Poster", "Name", "Time", "Types", "Description", ""]
        }
    else:
        return {
            "status": False,
            "message": "Oops! something went wrong. try again later!"
        }


# Getting movies in theatre
def get_movies_in_theatre():

    """
    Getting movies in theatre
    :return: List of movies in theatre
    """
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/movies-in-theaters/"
    movies_list = []
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        item_lists = soup.find_all("div", {"class": "list_item"})
        for item in item_lists:
            movie_context = {}

            # getting poster image
            poster_image_list = item.find_all("img", {"class": "poster"})
            if poster_image_list:
                poster_image = poster_image_list[0].get("src")
                movie_context["poster_image"] = poster_image

            # Getting movie heading
            movie_heading_list = item.find_all("h4")
            if movie_heading_list:
                movie_heading = str(movie_heading_list[0].text).strip()
                movie_context["movie_heading"] = movie_heading

            # Getting movie link
            movie_link_list = item.find_all("a")
            if movie_link_list:
                movie_href = movie_link_list[0].get("href")
                movie_href = str(base_url + movie_href)
                movie_context["movie_href"] = movie_href

            # Movie time
            movie_time_list = item.find_all("time")
            if movie_time_list:
                time = movie_time_list[0].text
                movie_context["movie_time"] = time

            # Getting movie types
            movie_type_list = item.find_all("p", {"class": "cert-runtime-genre"})
            if movie_type_list:
                for movie_type in movie_type_list:
                    movie_spans = movie_type.find_all("span")
                    list_of_text = [x.text for x in movie_spans]
                    types_movie = " ".join(list_of_text)
                    movie_context["movie_types"] = types_movie

            # Getting movie description
            movie_desc_list = item.find_all("div", {"class": "outline"})
            if movie_desc_list:
                description = str(movie_desc_list[0].text).strip()
                movie_context["description"] = description

            movies_list.append(movie_context)

        movie_list = [x for x in movies_list if x != {}]
        return {
            "status": True,
            "movie_list": list(movie_list),
            "table_headings": ["Poster", "Name", "Time", "Types", "Description", ""]
        }
    else:
        return {
            "status": False,
            "message": "Oops! something went wrong. try again later!"
        }


# Get oscar winners
def get_oscar_winners():

    """
    Getting list of oscars winner
    :return: List of oscar winners
    """
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/search/title?count=200&groups=oscar_best_picture_winners&sort=year,desc&ref_=nv_ch_osc"
    movies_list = []
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        lister_items = soup.find_all("div", {"class": "mode-advanced"})
        for lister_item in lister_items:
            movies_context = {}
            list_item_images = lister_item.find_all("div", {"class": "lister-item-image"})
            for list_item_image in list_item_images:
                link_list = list_item_image.find_all("a")
                link_image_list = list_item_image.find_all("img", {"class": "loadlate"})
                if link_list:
                    link = link_list[0].get("href")
                    movie_link = base_url + link
                    movies_context["movie_link"] = movie_link
                if link_image_list:
                    link_image = link_image_list[0].get("loadlate")
                    movies_context["link_image"] = link_image


            list_item_contents = lister_item.find_all("div", {"class": "lister-item-content"})
            for list_item_content in list_item_contents:
                title_list = list_item_content.find_all("h3")
                if title_list:
                    for title in title_list:
                        movie_title_list = title.find_all("a")
                        if movie_title_list:
                            movie_title = str(movie_title_list[0].text).strip()
                            movies_context["movie_title"] = movie_title

                        movie_year_list = title.find_all("span", {"class": "lister-item-year"})
                        if movie_year_list:
                            movie_year = str(movie_year_list[0].text).strip()
                            movies_context["movie_year"] = movie_year

                rating_bar_list = list_item_content.find_all("div", {"class": "ratings-bar"})
                if rating_bar_list:
                    for rating_bar in rating_bar_list:
                        rating_list = rating_bar.find_all("div", {"class": "ratings-imdb-rating"})
                        if rating_list:
                            rating_value = rating_list[0].get("data-value")
                            movies_context["rating_value"] = rating_value


                description_list = list_item_content.find_all("p", {"class": "text-muted"})
                if description_list:
                    for description in description_list[1:]:
                        desc_text = str(description.text).strip()
                        movies_context["desc_text"] = desc_text

            movies_list.append(movies_context)

        movies_list = [x for x in movies_list if x != {}]
        return {
            "status": True,
            "movies_list": list(movies_list),
            "table_headings": ["Poster", "Title", "Year", "Rating", "Description"]
        }
    else:

        return {
            "status": False,
            "message": "Not able to get the data."
        }


# Trailers Functions
def get_popular_trailers():

    """
    Getting popular trailers
    :return: List of popular trailers
    """
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/trailers/"
    popular_trailers = []
    request = requests.get(url)
    # popTab
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        # Data required: name, video id, image, link

        popular_trailer_div = soup.find_all("div", {"id": "popTab"})
        if popular_trailer_div:
            for popular_trailer in popular_trailer_div:
                trailer_items = popular_trailer.find_all("div", {"class": "gridlist-item"})
                if trailer_items:
                    for link_item in trailer_items:
                        trailers_context = {}
                        # Getting the video id
                        trailer_video_id = link_item.get("data-videoid")
                        trailers_context["trailer_video_id"] = trailer_video_id

                        # Getting caption name
                        trailer_captions = link_item.find_all("div", {"class": "trailer-caption"})
                        if trailer_captions:
                            for title_cap in trailer_captions:
                                title_cap_list = title_cap.find_all("a")
                                if title_cap_list:
                                    caption = title_cap_list[0].text
                                    trailers_context["caption_title"] = str(caption).strip()

                        # Getting link from trailer item
                        link_list = link_item.find_all("a")
                        if link_list:
                            trailer_link = base_url + link_list[0].get("href")
                            trailers_context["trailer_link"] = trailer_link

                        # Getting trailer images
                        trailer_images_list = link_item.find_all("img", {"class": "pri_image"})
                        if trailer_images_list:
                            for trailer_image in trailer_images_list:
                                trailer_image_src = trailer_image.get("data-src-x2")
                                trailer_description = trailer_image.get("title")
                                trailers_context["trailer_description"] = str(trailer_description).strip()
                                trailers_context["trailer_image_src"] = trailer_image_src


                        popular_trailers.append(trailers_context)

        trailers = [x for x in popular_trailers if x != {}]
        return {
            "status": True,
            "popular_trailers": list(trailers)
        }

    else:
        return {
            "status": False,
            "message": "Not able to get the data."
        }


def get_recent_trailers():

    """
    Getting list of recent trailers
    :return: List recent trailers
    """
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/trailers/"
    popular_trailers = []
    request = requests.get(url)
    # popTab
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        # Data required: name, video id, image, link

        popular_trailer_div = soup.find_all("div", {"id": "recAddTab"})
        if popular_trailer_div:
            for popular_trailer in popular_trailer_div:
                trailer_items = popular_trailer.find_all("div", {"class": "gridlist-item"})
                if trailer_items:
                    for link_item in trailer_items:
                        trailers_context = {}
                        # Getting the video id
                        trailer_video_id = link_item.get("data-videoid")
                        trailers_context["trailer_video_id"] = trailer_video_id

                        # Getting caption name
                        trailer_captions = link_item.find_all("div", {"class": "trailer-caption"})
                        if trailer_captions:
                            for title_cap in trailer_captions:
                                title_cap_list = title_cap.find_all("a")
                                if title_cap_list:
                                    caption = title_cap_list[0].text
                                    trailers_context["caption_title"] = str(caption).strip()

                        # Getting link from trailer item
                        link_list = link_item.find_all("a")
                        if link_list:
                            trailer_link = base_url + link_list[0].get("href")
                            trailers_context["trailer_link"] = trailer_link

                        # Getting trailer images
                        trailer_images_list = link_item.find_all("img", {"class": "pri_image"})
                        if trailer_images_list:
                            for trailer_image in trailer_images_list:
                                trailer_image_src = trailer_image.get("data-src-x2")
                                trailer_description = trailer_image.get("title")
                                trailers_context["trailer_description"] = str(trailer_description).strip()
                                trailers_context["trailer_image_src"] = trailer_image_src

                        popular_trailers.append(trailers_context)

        trailers = [x for x in popular_trailers if x != {}]
        return {
            "status": True,
            "popular_trailers": list(trailers)
        }
    else:
        return {
            "status": False,
            "message": "Not able to get the data."
        }


def get_tv_trailers():

    """
    Getting list of tv trailers
    :return: list tc trailers
    """
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/trailers/"
    popular_trailers = []
    request = requests.get(url)
    # popTab
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        # Data required: name, video id, image, link

        popular_trailer_div = soup.find_all("div", {"id": "tvTab"})
        if popular_trailer_div:
            for popular_trailer in popular_trailer_div:
                trailer_items = popular_trailer.find_all("div", {"class": "gridlist-item"})
                if trailer_items:
                    for link_item in trailer_items:
                        trailers_context = {}
                        # Getting the video id
                        trailer_video_id = link_item.get("data-videoid")
                        trailers_context["trailer_video_id"] = trailer_video_id

                        # Getting caption name
                        trailer_captions = link_item.find_all("div", {"class": "trailer-caption"})
                        if trailer_captions:
                            for title_cap in trailer_captions:
                                title_cap_list = title_cap.find_all("a")
                                if title_cap_list:
                                    caption = title_cap_list[0].text
                                    trailers_context["caption_title"] = str(caption).strip()

                        # Getting link from trailer item
                        link_list = link_item.find_all("a")
                        if link_list:
                            trailer_link = base_url + link_list[0].get("href")
                            trailers_context["trailer_link"] = trailer_link

                        # Getting trailer images
                        trailer_images_list = link_item.find_all("img", {"class": "pri_image"})
                        if trailer_images_list:
                            for trailer_image in trailer_images_list:
                                trailer_image_src = trailer_image.get("data-src-x2")
                                trailer_description = trailer_image.get("title")
                                trailers_context["trailer_description"] = str(trailer_description).strip()
                                trailers_context["trailer_image_src"] = trailer_image_src

                        popular_trailers.append(trailers_context)

        trailers = [x for x in popular_trailers if x != {}]
        return {
            "status": True,
            "popular_trailers": list(trailers)
        }
    else:
        return {
            "status": False,
            "message": "Not able to get the data."
        }

# Movies Functions
def get_top_rated_movies():

    """
    This function return the top movies list
    :return: List of top rated movies
    """
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/chart/top"
    top_movies_list = []
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        table_rows = soup.find_all("tr")
        for row in table_rows:
            context_data = {}
            table_data_poster = row.find_all("td", {"class": "posterColumn"})

            if table_data_poster:
                for poster in table_data_poster:
                    post_image_list = poster.find_all("img")
                    if post_image_list:
                        poster_image = post_image_list[0].get("src")
                        context_data["movie_poster"] = poster_image


            table_data_title = row.find_all("td", {"class": "titleColumn"})
            if table_data_title:
                for title_col in table_data_title:
                    # Mobile Title List
                    title_list = title_col.find_all("a")
                    if title_list:
                        title = title_list[0].text
                        context_data["movie_title"] = title
                    # Movie Link List
                    url_link_list = title_col.find_all("a")
                    if url_link_list:
                        url_link = url_link_list[0].get("href")
                        context_data["movie_link"] = base_url + url_link

            table_data_rating = row.find_all("td", {"class": "imdbRating"})
            if table_data_rating:
                for rating_data in table_data_rating:
                    rating_list = rating_data.find_all("strong")
                    if rating_list:
                        rating = rating_list[0].text
                        context_data["movie_rating"] = rating

            # Appending context data top movie
            top_movies_list.append(context_data)

        top_movies_list = [x for x in top_movies_list if x != {}]
        return {
            "status": True,
            "top_movies_list": list(top_movies_list),
            "table_headings": ["Poster", "Title", "Rating", ""],
        }
    else:
        return {
            "status": False,
            "message": "Not able to get the data."
        }


# Getting top rated indian movies
def get_top_rated_indian():

    """
    Getting the top rated indian movies
    :return: List of top rated indian movies
    """
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/india/top-rated-indian-movies/"
    top_movies_list = []
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        table_rows = soup.find_all("tr")
        for row in table_rows:
            context_data = {}
            table_data_poster = row.find_all("td", {"class": "posterColumn"})

            if table_data_poster:
                for poster in table_data_poster:
                    post_image_list = poster.find_all("img")
                    if post_image_list:
                        poster_image = post_image_list[0].get("src")
                        context_data["movie_poster"] = poster_image


            table_data_title = row.find_all("td", {"class": "titleColumn"})
            if table_data_title:
                for title_col in table_data_title:
                    # Mobile Title List
                    title_list = title_col.find_all("a")
                    if title_list:
                        title = title_list[0].text
                        context_data["movie_title"] = title
                    # Movie Link List
                    url_link_list = title_col.find_all("a")
                    if url_link_list:
                        url_link = url_link_list[0].get("href")
                        context_data["movie_link"] = base_url + url_link

            table_data_rating = row.find_all("td", {"class": "imdbRating"})
            if table_data_rating:
                for rating_data in table_data_rating:
                    rating_list = rating_data.find_all("strong")
                    if rating_list:
                        rating = rating_list[0].text
                        context_data["movie_rating"] = rating

            # Appending context data top movie
            top_movies_list.append(context_data)

        top_movies_list = [x for x in top_movies_list if x != {}]
        return {
            "status": True,
            "top_movies_list": list(top_movies_list),
            "table_headings": ["Poster", "Title", "Rating", ""],
        }
    else:
        return {
            "status": False,
            "message": "Not able to get the data."
        }


# Get popular movies
def get_popular_movies():

    """
    Getting most popular movies
    :return: List of most popular movies
    """
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/chart/moviemeter"
    top_movies_list = []
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, features="html5lib")
        table_rows = soup.find_all("tr")
        for row in table_rows:
            context_data = {}
            table_data_poster = row.find_all("td", {"class": "posterColumn"})
            if table_data_poster:
                for poster in table_data_poster:
                    poster_image_list = poster.find_all("img")
                    if poster_image_list:
                        poster_image = poster_image_list[0].get("src")
                        context_data["movie_poster"] = poster_image

            table_data_title = row.find_all("td", {"class": "titleColumn"})
            if table_data_title:
                for title_col in table_data_title:

                    # Mobile Title List
                    title_list =title_col.find_all("a")
                    if title_list:
                        title = title_list[0].text
                        context_data["movie_title"] = title

                    # Movie Link List
                    url_link_list = title_col.find_all("a")
                    if url_link_list:
                        url_link = url_link_list[0].get("href")
                        context_data["movie_link"] = base_url + url_link

            table_data_rating = row.find_all("td", {"class": "imdbRating"})
            if table_data_rating:
                for rating_data in table_data_rating:
                    rating_list = rating_data.find_all("strong")
                    if rating_list:
                        rating = rating_list[0].text
                        context_data["movie_rating"] = rating

            # Appending context data top movie
            top_movies_list.append(context_data)

        top_movies_list = [x for x in top_movies_list if x != {}]
        return {
            "status": True,
            "top_movies_list": list(top_movies_list),
            "table_headings": ["Poster", "Title", "Rating", ""],
        }
    else:
        return {
            "status": False,
            "message": "Not able to get the data."
        }

# Getting trailer by video id
def get_trailer_video_id(url):

    """
    This function get the video id from
    specified url
    :param url: URL of top rated movie
    :return: ID of video trailer
    """
    req = requests.get(url)
    if req.status_code == 200:
        soup = BeautifulSoup(req.content, features="html5lib")
        video_id = None
        video_container = soup.find_all("div", {"class": "slate_wrapper"})
        for video_data in video_container:
            video_id = video_data.find_all("a", {"class": "slate_button"})[0].get("data-video")
            video_id = video_id

        return {
            "status": True,
            "video_id": video_id
        }
    else:
        return {
            "status": False,
            "message": "Oops! Could not get the video trailer id."
        }