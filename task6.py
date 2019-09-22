#Exercise6: Code to print total number of abecedarian words in a given fileis_abecedarian('banana')
def is_abecedarian(word):
    index = 0
    while index < len(word) -1:
        if word[index] > word[index+1]:
            return False
        else:
            index +=1
    return True

is_abecedarian('banana')
is_abecedarian('ace')

myfile = open('words.txt')
count = 0
for line in myfile:
    word = line.strip()
    if is_abecedarian(word):
        count += 1
print('There number of abecedarian words in the given file are:', count)
