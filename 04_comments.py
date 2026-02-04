# subject of this python script:
# authored by : sana
# where to contact: github profile link or email (gmail) google colab link


# step-1: why to use single qutation
print('sana') # when we are writting a string

# step-2: when to use "" qutation marks?
print("sana")
print("what's up") # when wrotting string  and making use of other qutation marks


# step-3: when to use triple qutation marks?
print('''
     sehar's
      sana ''')# to write multiple strings and also make use ""or''qutation marks inside


# assignment: when to use comments in python mention 10 study cases?
# Calculate the factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1  # base case: 0! = 1
    else:
        return n * factorial(n-1)  # recursive case: n! = n * (n-1)!