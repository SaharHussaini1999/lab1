def is_high_score(movie):
    return movie["imdb"] > 5.5


def high_score_movies(movie_list):
    return [movie for movie in movie_list if movie["imdb"] > 5.5]


def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"].lower() == category.lower()]


def average_score(movie_list):
    if not movie_list:
        return 0
    total_score = sum(movie["imdb"] for movie in movie_list)
    return total_score / len(movie_list)


def average_score_by_category(movie_list, category):
    filtered = movies_by_category(movie_list, category)
    return average_score(filtered)


print(is_high_score(movies[0]))
print(high_score_movies(movies))
print(movies_by_category(movies, "Romance"))
print(average_score(movies))
print(average_score_by_category(movies, "Romance"))
