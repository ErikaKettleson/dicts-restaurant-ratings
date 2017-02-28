# your code goes here


def print_alpha_restaurant_ratings(filename):
    """prints restaurants and ratings in alphabetical order."""

    ratings_file = open(filename)

    for line in ratings_file:
        restaurant_info = line.rstrip().split(":")


    ratings_file.close()

print_alpha_restaurant_ratings("scores.txt")