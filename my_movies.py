# Initialize an Empty List: Create an empty list named favorite_movies.
favorite_movies = []


# Add Movies to the List: Write a function add_movie(movie) that adds a movie to the list and prints a message indicating the movie was added.
def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added.")


# Remove Movies from the List: Write a function remove_movie(movie) that removes a movie from the list if it exists, and prints a message indicating the movie was removed or a message if the movie was not found.
def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed")
    else:
        print(f"Movie '{movie}' not found")


# Display the List: Write a function display_movies() that prints all the movies in the list.
def display_movies():
    print("Favorite Movies:")
    for movie in favorite_movies:
        print(f"- {movie}")


# Count Movies in the List: Write a function count_movies() that prints the number of movies in the list.
def count_movies():
    print(f" {len(favorite_movies)} favorite movies saved")


# Find a Movie: Write a function find_movie(movie) that checks if a movie is in the list and prints a message indicating whether the movie was found or not.
def find_movie(movie):
    if movie in favorite_movies:
        print(f" {movie} exists")
    else:
        print(f" {movie} not found")


# Clear the List: Write a function clear_movies(et that removes all movies from the list and prints a message indicating the list has been cleared.
def clear_movies():
    favorite_movies.clear()
    print("Movie list cleared")


# Adding Movies
add_movie("Terminator")
add_movie("iRobot")
add_movie("Event Horizon")
add_movie("Tremors")

# Display Movies
display_movies()

# Remove Movies
remove_movie("Terminator")

# Count Movies
count_movies()

# Find Movie
find_movie("T2")

# Clear Movies
clear_movies()

# Count Movies
count_movies()
