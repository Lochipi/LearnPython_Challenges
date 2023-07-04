'''question
Reverse an integer '''

def reverse_num(num):
    str_num = str(num)

    if str_num[0] == '-':   #If the number is negative, reverse the string from index 1
        reversed_str = '-' + str_num[:0:-1]
    else:
        reversed_str = str_num[::-1]

    #converting back a string to a number 
    reversed_str_num = int(reversed_str)

    return reversed_str_num



# test
num1 = 12345
reversed_num1 = reverse_num(num1)
print("Reversed integer:", reversed_num1)  #expected 54321

num2 = -6789
reversed_num2 = reverse_num(-6789)
print("Reversed integer:", reversed_num2)  #expected -9876
