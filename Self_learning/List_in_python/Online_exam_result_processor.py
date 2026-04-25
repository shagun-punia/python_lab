# Program 5: Online Exam Result Processor

scores = list(map(int, input("Enter student scores separated by space: ").split()))

print("\n----- Original Scores -----")
print(scores)

# Removing lowest 2 scores
scores.sort()
removed = scores[:2]
scores = scores[2:]

print("Removed Lowest 2 Scores:", removed)

# Adding grace marks (5 marks for 30-35)
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Counting passed students
passed = len([s for s in scores if s >= 40])

print("\n----- Final Result -----")
print("Updated Scores:", scores)
print("Number of Students Passed (>=40):", passed)
#OUTPUT
"""Enter student scores separated by space: 78 90 78 65 
09

----- Original Scores -----
[78, 90, 78, 65, 9]
Removed Lowest 2 Scores: [9, 65]

----- Final Result -----
Updated Scores: [78, 78, 90]
Number of Students Passed (>=40): 3"""