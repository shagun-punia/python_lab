#  Sports Tournament Points Table

points = list(map(int, input("Enter team points: ").split()))

points = [p if p >= 0 else 0 for p in points]

if len(points) < 2:
    print("Not enough teams.")
else:
    points.sort(reverse=True)
    print("Winner:", points[0])
    print("Runner-up:", points[1])
    print("Leaderboard:", points)