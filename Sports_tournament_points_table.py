# Program 10: Sports Tournament Points Table

points = list(map(int, input("Enter team points sperated by space: ").split()))

print("\nOriginal Points:", points)

# Replacing negative points with 0
points = [p if p >= 0 else 0 for p in points]

print("After Replacing Negative Points with 0:", points)

# Sorting leaderboard
points.sort(reverse=True)

print("\n----- Leaderboard -----")
print("Winner Points:", points[0])
if len(points) > 1:
    print("Runner-Up Points:", points[1])
print("Final Sorted Leaderboard:", points)
#OUTPUT
"""Enter team points sperated by space: 3 4 7

Original Points: [3, 4, 7]
After Replacing Negative Points with 0: [3, 4, 7]

----- Leaderboard -----
Winner Points: 7
Runner-Up Points: 4
Final Sorted Leaderboard: [7, 4, 3]"""