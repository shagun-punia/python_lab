# Check prime using function

def is_prime(num):  # define function
    if num <= 1:  # check small numbers
        return False
    for i in range(2, num):  # check divisibility
        if num % i == 0:  # not prime
            return False
    return True  # prime

num = int(input("Enter a number: "))  # input

print("\n----- Output -----")
if is_prime(num):  # call function
    print(num, "is Prime")
else:
    print(num, "is not Prime")
    #OUTPUT
    """
    
    Enter a number: 5

----- Output -----
5 is Prime 
"""