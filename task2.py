# create a python function that when you input a number to the function you have created checks whether the number belongs to the Fibonnaci sequence or not.
'''
fibonacci  sequence is a series of numbers which each number is the sum of the two preceding ones.
It starts with 0 and 1, and the subsequent numbers are obtained by adding the previous two numbers in the sequence.
for example : 0,1,1,2,3,5,8,13 and so on

'''

def check_fibonacci(num):
    fib1, fib2 = 0, 1

    while fib2 < num:
        fib1, fib2 = fib2, fib1 + fib2 

    if fib2 == num:
        return True
    else:
        return False

number = int(input("Please enter a number: "))

if check_fibonacci(number):
    print(number, "belongs to the Fibonacci sequence.")
else:
    print(number, "does not belong to the Fibonacci sequence.")
