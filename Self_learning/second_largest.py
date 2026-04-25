# Program to find second largest element (without using sort)

# Take list input in one line
lst = list(map(int, input("Enter elements separated by space: ").split()))

# Check if list has enough elements
if len(lst) < 2:
    print("Need at least 2 elements")
else:
    largest = second = -999999999  # small initial values

    # Loop through list
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    # Print result
    if second == -999999999:
        print("No second largest element")
    else:
        print("Second largest element is:", second)
        #output
        """Enter elements separated by space: 56 78 234 79
Second largest element is: 79"""