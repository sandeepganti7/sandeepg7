""" Excercise_2: Code to print all the words that doesn't have
letter 'e' """

myfile = open('words.txt')
def has_no_e(word):
    for char in word:
        if char == 'e' or char == 'E':
            return False
    return True  
count = 0
for line in myfile:
	word = line.strip()
	if has_no_e(word):
		count = count + 1
		print(word)
print("Number of words withouit letter 'e':")
print(count)
total_words = 0
myfile = open("words.txt")
for line in myfile:
	words = line.split()
	total_words += len(words)
print("Number of words:", total_words)
percentage = (count / total_words) * 100
print(str(percentage) + "% of the words don't have an 'e'.")
