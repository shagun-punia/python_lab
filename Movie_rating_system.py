#  Movie Rating System

ratings = list(map(int, input("Enter ratings (1-5): ").split()))

ratings = [r for r in ratings if 1 <= r <= 5]

if len(ratings) == 0:
    print("No valid ratings.")
else:
    average = sum(ratings) / len(ratings)
    five_star = ratings.count(5)

    ratings.sort()

    print("Valid Ratings:", ratings)
    print("Average Rating:", average)
    print("5-Star Ratings:", five_star)