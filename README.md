# README

## About
This is the 1st project from the Udacity Full Stack Web Developer Nanodegree Program.
The programm automatically generates and launches an HTML Document displaying a specified list of movies, including the movie title, storyline, imdb details, poster image and trailer from youtube.

## Included Files
movies/
	- entertainment_center.py
	- fresh_tomatoes.py
	- media.py
	
## How to use
Before running any python programms please check if you have Python installed on you're machine!
You can check this by running the command `python --version` from the terminal.

1. Open the file "enterainment_center.py" (for example in Python IDLE) and provide some movie data. It should follow this syntax:
movie_name = media.Movie("Movie Name", 
                        "The movie storyline in one or two sentences.", 
                        "URL to the IMDB site of the movie",
                        "URL to a poster image (upright orientation preferred)", 
                        "URL to the youtube trailer")

                        
2. Collect all movies in a list like this:
movies = [movie_a, movie_b, movie_c]

3. Run the application by typing `python entertainment_center.py` from the terminal. If you are using Python IDLE, open "entertainment_center.py" and choose "Run Module" from the "Run" menu. 
This will run the main function `fresh_tomatoes.open_movies_page(movies)`

Make sure "entertainment_center.py", "media.py" and "fresh_tomatoes.py" are located in the same directory. The directory must be read-write, so the "open_movie_page" function can generate a HTML file.

## More Info / Contact
If you have any questions feel free to contact me: info@tmerz.com


## Author
Created by Tobias Merz (tobi238)