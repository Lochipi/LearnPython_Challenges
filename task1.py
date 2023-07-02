# # create a python function to check whether a number is or not

def check_number(num):
    if num < 2:
        print("Number is neither prime nor even")
    elif num % 2 == 0:
        print("Number is even")
    else: 
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                print("Number is not prime")
                return
        print("Number is prime")  

check_number(15) #Not prime
check_number(7) # prime number
check_number(10) # Even number

''' hint
We start a loop from 3 and continue until the square root of the number (checked with range(3, int(num ** 0.5) + 1)). We iterate through each number in this range and check if the number is divisible by any of them (checked with num).

, We print "Number is not prime" and return from the function.

the number is not divisible by any number in this range, it means the number is prime. We print "Number is prime".
'''