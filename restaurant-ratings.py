# your code goes here


def print_alpha_restaurant_ratings(filename):
    """prints restaurants and ratings in alphabetical order."""

    ratings_file = open(filename)

    restaurant_ratings = {}

    for line in ratings_file:
        restaurant_info = line.rstrip().split(":")
        restaurant_name = restaurant_info[0]
        restaurant_rating = restaurant_info[1]

        restaurant_ratings[restaurant_name] = restaurant_rating

    sorted_restaurants = sorted(restaurant_ratings)

    for restaurant in sorted_restaurants:
        restaurant_rating = restaurant_ratings[restaurant]
        print "{} is rated at {}.".format(restaurant, restaurant_rating)


    ratings_file.close()

print_alpha_restaurant_ratings("scores.txt")