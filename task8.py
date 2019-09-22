#Exercise8
def is_palindrome(num, start):
    numString = str(num)
    i = start
    j = len(numString) - 1
    count = 0
    while i <= j:
        if numString[i] == numString[j]:
             print(numString)
        else:
             return False
        i = i + 1
        j = j - 1

is_palindrome(5445, 5)
