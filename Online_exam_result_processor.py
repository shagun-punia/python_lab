#  Online Exam Result Processor

scores = list(map(int, input("Enter scores: ").split()))

if len(scores) <= 2:
    print("Not enough scores to remove lowest 2.")
else:
    scores.sort()
    scores = scores[2:]   # Remove lowest 2

    for i in range(len(scores)):
        if 30 <= scores[i] <= 35:
            scores[i] += 5   # Grace marks

    passed = len([s for s in scores if s >= 40])

    print("Updated Scores:", scores)
    print("Number of Students Passed:", passed)