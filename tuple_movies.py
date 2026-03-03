# Now that you've seen how tuples can be used to store and manage book information, let's create an application to manage a movie collection. This task will help you practice using tuples to store fixed collections of data. Follow the instructions below:

# Initialize a List of Movies
movie_collection = [
    ("The Terminator", "James Cameron", 1984),
    ("I, Robot", "Alex Proyas", 2004),
]


# Function to add movies
def add_movie(title, director, year):
    new_movie = (title, director, year)
    movie_collection.append(new_movie)
    print(f"{title} added to list")


# Function to remove a movie by title
def remove_movie(title):
    found_movies = search_by_title(title)
    if len(found_movies) > 0:
        for movie in found_movies:
            movie_collection.remove(movie)
            print(f" {movie[0]} removed from list")
    else:
        print(f" {title} not found")


# Function to update movie
def update_movie(title, new_director, new_year):
    updated_movie = (title, new_director, new_year)
    found_movies = search_by_title(title)
    if len(found_movies) > 0:
        for movie in found_movies:
            movie_collection.remove(movie)
        movie_collection.append(updated_movie)
        print(f"{title} updated with Director: {new_director} and Year: {new_year}")
    else:
        print(f"{title} not found")


# Display All Movies
def display_movies():
    print("All Movies:")
    for title, director, year in movie_collection:
        print(f"- Title: {title}, Director: {director}, Year: {year}")


# Function to search for Director
def search_by_director(director):
    found_movies = []
    for movie in movie_collection:
        if movie[1] == director:
            found_movies.append(movie)
    return found_movies


# Function to search by Title
def search_by_title(title):
    found_movies = []
    for movie in movie_collection:
        if movie[0] == title:
            found_movies.append(movie)
    return found_movies


# Function to sort movies by year
def sort_movies_by_year():
    return sorted(movie_collection, key=lambda movie: movie[2])


# Add Movies
add_movie("The Matrix", "Wachowski's", 1999)
add_movie("Terminator 2", "James Cameroon", 1991)

# List Movies
display_movies()

# Search for Movies by James Cameron and Display
cameron_movies = search_by_director("James Cameron")
print("James Cameron Movies:")
for title, director, year in cameron_movies:
    print(f"- Title: {title}, Director: {director}, Year: {year}")

# Remove Movies
remove_movie("The Terminator")
display_movies()

# Update Movie
update_movie("Terminator 2", "James Cameron", 1991)
display_movies()

# Sort Movies by year and Display
sorted_movies = sort_movies_by_year()
print("Movies by year:")
for title, director, year in sorted_movies:
    print(f"- Title: {title}, Director: {director}, Year: {year}")
