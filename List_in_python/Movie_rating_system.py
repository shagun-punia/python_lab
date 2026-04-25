# Program 9: Movie Rating System

ratings = list(map(int, input("Enter movie ratings (1-5): ").split()))

print("\nOriginal Ratings:", ratings)

# Removing invalid ratings
valid_ratings = [r for r in ratings if 1 <= r <= 5]

print("Valid Ratings (1-5 only):", valid_ratings)

if len(valid_ratings) > 0:
    average = sum(valid_ratings) / len(valid_ratings)
    five_star = valid_ratings.count(5)

    valid_ratings.sort()

    print("\n----- Rating Summary -----")
    print("Sorted Ratings:", valid_ratings)
    print("Average Rating:", round(average, 2))
    print("Number of 5-Star Ratings:", five_star)
else:
    print("No valid ratings entered.")
    #OUTPUT
    """Enter movie ratings (1-5): 1 4 5

Original Ratings: [1, 4, 5]        
Valid Ratings (1-5 only): [1, 4, 5]

----- Rating Summary -----
Sorted Ratings: [1, 4, 5]
Average Rating: 3.33
Number of 5-Star Ratings: 1"""
