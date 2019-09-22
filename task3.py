""" Excercise_3: Code to print all the words that don’t
 contain any of the given forbidden letters"""

myfile = open('words.txt')

def avoids(word,letter):
	for char in word:
		if char in letter:
			return False
	return True


letter = input('What letters to exclude? ')
count = 0
for line in myfile:
	word = line.strip()
	if avoids(word, letter):
		count += 1
		print(word)

print("count is :",count)
total_words = 0
myfile = open("words.txt")
for line in myfile:
	words = line.split()
	total_words += len(words)
print("Total number of words:", total_words)

percentage = (count / 113809.0) * 100

print(str(percentage) + "% of the words don't have " + letter + '.')
