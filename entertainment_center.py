import media
import fresh_tomatoes

# Provide the movie data
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://www.imdb.com/title/tt0114709/?ref_=nv_sr_1",
                        "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.imdb.com/title/tt0499549/?ref_=nv_sr_1",
                     "http://cafmp.com/wp-content/uploads/2012/11/avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology.",  # noqa
                        "http://www.imdb.com/title/tt1375666/?ref_=nv_sr_1",
                        "http://resizing.flixster.com/q3gSXJc8aDKWJuAiok9ckWvKcQ4=/800x1200/v1.bTsxMTE2NjcyNTtqOzE2OTc5OzIwNDg7ODAwOzEyMDA",  # noqa
                        "https://www.youtube.com/watch?v=JEv8W3pWqH0")
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn.",
                             "http://www.imdb.com/title/tt0332379/?ref_=nv_sr_2",  # noqa
                             "http://image.tmdb.org/t/p//original/uXqiiMwGraI72DhRAUq8P8gz2ip.jpg",  # noqa
                             "https://www.youtube.com/watch?v=5afGGGsxvEA")
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://www.imdb.com/title/tt0382932/?ref_=fn_al_tt_1",  # noqa
                          "http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg",  # noqa
                          "https://www.youtube.com/watch?v=wlCAq45TcxU")
hunger_games = media.Movie("Hunger Games",
                           "A really real reality show.",
                           "http://www.imdb.com/title/tt1392170/?ref_=nv_sr_2",
                           "http://www.hungergamesdwtc.net/wp-content/uploads/2014/02/The-Hunger-Games-Poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# Store the movies in a list
movies = [toy_story, avatar, inception, school_of_rock, ratatouille, hunger_games]  # noqa

# Run open_movies_page function from fresh_tomatoes.py with the movies specified above # noqa
fresh_tomatoes.open_movies_page(movies)

# Print the Class Variables of Movie
# Custom Class Variable
print media.Movie.VALID_RATINGS

# Automatically generated Class Variables
print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__
