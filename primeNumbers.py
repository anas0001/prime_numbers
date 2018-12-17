#Function Definitions

def primeCheck(a):
    """inputs an integer, checks if the number is prime, returns Boolean True for prime and False for not prime"""
    if a == 1:
        return False
    if a == 2 or a == 3 or a == 5:
        return True
    if a%2 == 0:
        return False
    for x in range(3,a,2):
        if a%x == 0:
            return False
        if a/2 <= x:
            return True

def primeGenerate(x):
    """inputs an integer, finds all the prime numbers within 0 and that range, returns a list of all the prime numbers within the range"""
    primeNum = []
    for y in range(x+1):
       if primeCheck(y):
           primeNum.append(y)
    return primeNum

#Program and Function Calls

number = int(input('Please enter a number to see it is prime or not?\n'))
answer = 'prime' if primeCheck(number) == True else 'not prime'
print('the number is ', answer)

span = int(input('Please enter the range to find prime numbers\n'))
print('the prime numbers in the range', span ,'are ', end='')
print(*primeGenerate(span), sep=', ')