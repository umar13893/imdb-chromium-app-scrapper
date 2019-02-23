Vue.use(VueTabs);
Vue.prototype.$http = axios;

function stoperror() {
   return true;
}
window.onerror = stoperror;

new Vue({
    el:"#app",
    data: {
        movies_type: "coming_soon",
        trailer_type: "popular",
        dates_movies_arr: [],
        date_movie: null,
        is_global_loading: true,
        is_loading_movies: false,
        is_loading_trailers: false,
        is_loading_oscars: false,
        is_show_date: true,
        is_show_movies_select: true,
        is_show_trailer_select: true,
        table_results: [],
        table_headings: [],
        grid_data_response: [],
    },
    created() {
        this.getComingMoviesDates();
        this.is_global_loading = true;
    },
    mounted() {
    },
    methods: {
        getComingMoviesDates() {
            const baseURI = 'http://localhost:8000/coming_soon_movies_dates';
            this.$http.get(baseURI)
            .then((response) => {
                if(response.data.status) {
                    for(i=0; i < response.data.sort_options.length; i++)
                    {
                        obj_movies_dates = {
                            "value": response.data.sort_options[i].option_value,
                            "text": response.data.sort_options[i].option_text,
                        };
                        this.dates_movies_arr.push(obj_movies_dates);
                    }
                    this.date_movie = this.dates_movies_arr[0];
                }
                else {
                    alert("Something went wrong. Please try again later!");
                }
            })
            .then((response) => {
                let date_string_value = this.date_movie.value;
                const baseURI = "http://localhost:8000/coming_soon_movies";
                this.$http.get(baseURI, {
                    params: {
                        date_string: date_string_value,
                    },
                })
                .then((response) => {
                    if(response.data.status)
                    {
                        this.table_results = response.data.movie_list;
                        this.table_headings = response.data.table_headings;
                        this.is_global_loading = false;
                        this.is_show_movies_select = true;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    this.is_global_loading = false;
                    this.is_show_movies_select = true;
                })
            })
            .catch(function (error) {
                alert("Something went wrong. Please try again later!");
                this.is_global_loading = false;
                this.is_show_movies_select = true;
            })
        },

        handleTabChange(tabIndex, newTab, oldTab){
            if(tabIndex === 0)
            {
                this.is_show_movies_select = false;
                this.movies_type = "coming_soon";
                this.is_show_date = false;
                this.is_loading_movies = true;
                let self = this;
                const baseURI = 'http://localhost:8000/coming_soon_movies_dates';
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status) {
                        for(i=0; i < response.data.sort_options.length; i++)
                        {
                            obj_movies_dates = {
                                "value": response.data.sort_options[i].option_value,
                                "text": response.data.sort_options[i].option_text,
                            };
                            this.dates_movies_arr.push(obj_movies_dates);
                        }
                        this.date_movie = this.dates_movies_arr[0];
                    }
                    else {
                        alert("Something went wrong. Please try again later!");
                    }
                })
                .then((response) => {
                    let date_string_value = this.date_movie.value;
                    const baseURI = "http://localhost:8000/coming_soon_movies";
                    this.$http.get(baseURI, {
                        params: {
                            date_string: date_string_value,
                        },
                    })
                    .then((response) => {
                        if(response.data.status)
                        {
                            self.table_results = response.data.movie_list;
                            self.table_headings = response.data.table_headings;
                            self.is_loading_movies = false;
                            self.is_show_date = true;
                            self.is_show_movies_select = true;
                        }
                    })
                    .catch(function(error) {
                        alert("Something went wrong. Please try again later!");
                        self.is_loading_movies = false;
                        self.is_show_date = true;
                        self.is_show_movies_select = true;
                    })
                })
                .catch(function (error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                    self.is_show_date = true;
                    self.is_show_movies_select = true;
                })
            }
            else if(tabIndex === 1)
            {
                this.is_show_trailer_select = false;
                this.trailer_type = "popular";
                this.is_show_date = false;
                this.is_loading_movies = true;
                let self = this;
                const baseURI = "http://localhost:8000/popular_trailers";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.grid_data_response = response.data.popular_trailers;
                        self.is_loading_movies = false;
                        self.is_show_trailer_select = true;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                    self.is_show_trailer_select = true;
                })
            }
            else if(tabIndex === 2)
            {
                this.is_show_movies_select = false;
                this.is_show_date = false;
                this.is_loading_movies = true;
                let self = this;
                const baseURI = "http://localhost:8000/oscar_winners";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.table_results = response.data.movies_list;
                        self.table_headings = response.data.table_headings;
                        self.is_loading_movies = false;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                })
            }
            else
            {
                // Default is Movies
                this.is_show_movies_select = false;
                this.movies_type = "coming_soon";
                this.is_show_date = false;
                this.is_loading_movies = true;
                let self = this;
                const baseURI = 'http://localhost:8000/coming_soon_movies_dates';
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status) {
                        for(i=0; i < response.data.sort_options.length; i++)
                        {
                            obj_movies_dates = {
                                "value": response.data.sort_options[i].option_value,
                                "text": response.data.sort_options[i].option_text,
                            };
                            this.dates_movies_arr.push(obj_movies_dates);
                        }
                        this.date_movie = this.dates_movies_arr[0];
                    }
                    else {
                        alert("Something went wrong. Please try again later!");
                    }
                })
                .then((response) => {
                    let date_string_value = this.date_movie.value;
                    const baseURI = "http://localhost:8000/coming_soon_movies";
                    this.$http.get(baseURI, {
                        params: {
                            date_string: date_string_value,
                        },
                    })
                    .then((response) => {
                        if(response.data.status)
                        {
                            self.table_results = response.data.movie_list;
                            self.table_headings = response.data.table_headings;
                            self.is_loading_movies = false;
                            self.is_show_date = true;
                            self.is_show_movies_select = true;
                        }
                    })
                    .catch(function(error) {
                        alert("Something went wrong. Please try again later!");
                        self.is_loading_movies = false;
                        self.is_show_date = true;
                        self.is_show_movies_select = true;
                    })
                })
                .catch(function (error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                    self.is_show_date = true;
                    self.is_show_movies_select = true;
                })
            }
        },
        onMoviesTypeChange() {
            let movie_type = this.movies_type;
            this.is_show_date = false;
            this.is_loading_movies = true;
            var self = this;
            if(movie_type === "coming_soon")
            {
                const baseURI = 'http://localhost:8000/coming_soon_movies_dates';
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status) {
                        for(i=0; i < response.data.sort_options.length; i++)
                        {
                            obj_movies_dates = {
                                "value": response.data.sort_options[i].option_value,
                                "text": response.data.sort_options[i].option_text,
                            };
                            this.dates_movies_arr.push(obj_movies_dates);
                        }
                        this.date_movie = this.dates_movies_arr[0];
                    }
                    else {
                        alert("Something went wrong. Please try again later!");
                    }
                })
                .then((response) => {
                    let date_string_value = this.date_movie.value;
                    const baseURI = "http://localhost:8000/coming_soon_movies";
                    this.$http.get(baseURI, {
                        params: {
                            date_string: date_string_value,
                        },
                    })
                    .then((response) => {
                        if(response.data.status)
                        {
                            self.table_results = response.data.movie_list;
                            self.table_headings = response.data.table_headings;
                            self.is_loading_movies = false;
                            self.is_show_date = true;
                        }
                    })
                    .catch(function(error) {
                        alert("Something went wrong. Please try again later!");
                        self.is_loading_movies = false;
                        self.is_show_date = true;
                    })
                })
                .catch(function (error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                    self.is_show_date = true;
                })
            }
            else if(movie_type === "popular") {
                const baseURI = "http://localhost:8000/popular_movies";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.table_results = response.data.top_movies_list;
                        self.table_headings = response.data.table_headings;
                        self.is_loading_movies = false;
                        self.is_show_date = false;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                    self.is_show_date = false;
                })
            }
            else if(movie_type === "top_rated")
            {
                const baseURI = "http://localhost:8000/top_rated_movies";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.table_results = response.data.top_movies_list;
                        self.table_headings = response.data.table_headings;
                        self.is_loading_movies = false;
                        self.is_show_date = false;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                    self.is_show_date = false;
                })
            }
            else if(movie_type === "top_rated_indians")
            {
                const baseURI = "http://localhost:8000/top_rated_indians";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.table_results = response.data.top_movies_list;
                        self.table_headings = response.data.table_headings;
                        self.is_loading_movies = false;
                        self.is_show_date = false;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                    self.is_show_date = false;
                })
            }
            else if(movie_type === "in_theatre")
            {
                const baseURI = "http://localhost:8000/theatre_movies";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.table_results = response.data.movie_list;
                        self.table_headings = response.data.table_headings;
                        self.is_loading_movies = false;
                        self.is_show_date = false;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                    self.is_show_date = false;
                })
            }
            else if(movie_type === "box_office")
            {
                const baseURI = "http://localhost:8000/box_office_movies";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.table_results = response.data.top_movies_list;
                        self.table_headings = response.data.table_headings;
                        self.is_loading_movies = false;
                        self.is_show_date = false;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                    self.is_show_date = false;
                })
            }
            else
            {
                const baseURI = 'http://localhost:8000/coming_soon_movies_dates';
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status) {
                        for(i=0; i < response.data.sort_options.length; i++)
                        {
                            obj_movies_dates = {
                                "value": response.data.sort_options[i].option_value,
                                "text": response.data.sort_options[i].option_text,
                            };
                            this.dates_movies_arr.push(obj_movies_dates);
                        }
                        this.date_movie = this.dates_movies_arr[0];
                    }
                    else {
                        alert("Something went wrong. Please try again later!");
                    }
                })
                .then((response) => {
                    let date_string_value = this.date_movie.value;
                    const baseURI = "http://localhost:8000/coming_soon_movies";
                    this.$http.get(baseURI, {
                        params: {
                            date_string: date_string_value,
                        },
                    })
                    .then((response) => {
                        if(response.data.status)
                        {
                            self.table_results = response.data.movie_list;
                            self.table_headings = response.data.table_headings;
                            self.is_loading_movies = false;
                            self.is_show_date = true;
                        }
                    })
                    .catch(function(error) {
                        alert("Something went wrong. Please try again later!");
                        self.is_loading_movies = false;
                        self.is_show_date = true;
                    })
                })
                .catch(function (error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                    self.is_show_date = true;
                })
            }
        },
        onMoviesDateChange() {
            this.is_loading_movies = true;
            let date_string_value = this.date_movie.value;
            // alert(date_string_value);
            const baseURI = "http://localhost:8000/coming_soon_movies";
            this.$http.get(baseURI, {
                params: {
                    date_string: date_string_value,
                },
            })
            .then((response) => {
                if(response.data.status)
                {
                    this.table_headings = [];
                    this.table_results = response.data.movie_list;
                    this.table_headings = response.data.table_headings;
                    this.is_loading_movies = false;
                }
            })
            .catch(function(error) {
                alert("Something went wrong. Please try again later!");
                this.is_loading_movies = false;
            })
        },
        getMovieUrl(movie_url) {

            $.magnificPopup.open(
            {
                closeOnBgClick: true,
                closeBtnInside: true,
                enableEscapeKey: true,
                type: 'ajax',
                items: {
                    src: 'http://localhost:8000/video_trailer_id?url=' + movie_url,
                },
                callbacks:
                {
                    parseAjax: function(response) {

                        if(response.data.status)
                        {
                            if(response.data.video_id === null)
                            {
                                $.magnificPopup.close();
                                alert("No video found!");
                            }
                            else
                            {
                                $.magnificPopup.close();
                                $.magnificPopup.open({
                                    items: {
                                        src: 'http://www.imdb.com/video/imdb/'+response.data.video_id+'/imdb/embed?autoplay=true;width=870',
                                    },
                                    type: 'iframe',
                                });
                            }
                        }
                    },
                    ajaxContentAdded: function(e) {
                        console.log("Event!");
                    },
                    open: function() {
                        $(".mfp-preloader").text("");
                    },
                },
                ajax: {
                    settings: {
                        contentType: "application/json",
                        dataType: 'json',
                        type: 'GET'
                   }
               }
            });



        },
        playDirectVideo(video_id) {
            if(video_id)
            {
                $.magnificPopup.open({
                    items: {
                    src: 'http://www.imdb.com/video/imdb/'+video_id+'/imdb/embed?autoplay=true;width=870',
                    },
                    type: 'iframe',
                });
            }
            else
            {
                alert("No video found!");
            }
        },
        onTrailerTypeChange() {
            let trailer_type = this.trailer_type;
            if(trailer_type === "popular")
            {
                this.is_loading_movies = true;
                let self = this;
                const baseURI = "http://localhost:8000/popular_trailers";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.grid_data_response = response.data.popular_trailers;
                        self.is_loading_movies = false;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                })
            }
            else if(trailer_type === "most_recent")
            {
                this.is_loading_movies = true;
                let self = this;
                const baseURI = "http://localhost:8000/recent_trailers";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.grid_data_response = response.data.popular_trailers;
                        self.is_loading_movies = false;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                })
            }
            else if(trailer_type === "tv_tonight")
            {
                this.is_loading_movies = true;
                let self = this;
                const baseURI = "http://localhost:8000/tv_trailers";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.grid_data_response = response.data.popular_trailers;
                        self.is_loading_movies = false;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                })
            }
            else
            {
                this.is_loading_movies = true;
                let self = this;
                const baseURI = "http://localhost:8000/popular_trailers";
                this.$http.get(baseURI)
                .then((response) => {
                    if(response.data.status)
                    {
                        self.grid_data_response = response.data.popular_trailers;
                        self.is_loading_movies = false;
                    }
                })
                .catch(function(error) {
                    alert("Something went wrong. Please try again later!");
                    self.is_loading_movies = false;
                })
            }
        },
    },


});