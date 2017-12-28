# this return all of the print() funtions
'''
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument. /0')
        
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
'''

# this return up to the Error.
def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))

except ZeroDivisionError:
    print('Error:  Invalid argument. /0')
