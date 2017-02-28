# your code goes here

# def get_user_restaurant_data():
#     """prompts user for restaurant and rating and checks for int."""

#     user_restaurant = raw_input(
#         "We're rating restaurants! Give me a restaurant to rate!\n" +
#         "> ")

    
#     while True:
#         user_rating = raw_input("How would you rate your restaurant " +
#                             "on a scale of 1-5?\n" + 
#                             "> ")
#         if int(user_rating) > 5 or int(user_rating) < 0:
#             continue

#         try int(user_rating):
#             break
#         except ValueError:
#             continue






def print_alpha_restaurant_ratings(filename):
    """prints restaurants and ratings in alphabetical order."""

    ratings_file = open(filename)

    restaurant_ratings = {}

    for line in ratings_file:
        restaurant_name, restaurant_rating = line.rstrip().split(":")

        restaurant_ratings[restaurant_name] = restaurant_rating

    sorted_restaurants = sorted(restaurant_ratings)

    for restaurant in sorted_restaurants:
        restaurant_rating = restaurant_ratings[restaurant]
        print "{} is rated at {}.".format(restaurant, restaurant_rating)


    ratings_file.close()

get_user_restaurant_data()
print_alpha_restaurant_ratings("scores.txt")