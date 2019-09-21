""" Excercise_1: Code to print all the words having
more than 20 characters """

myfile = open('words.txt')
for line in myfile:
	word = line.strip()
	if len(word) > 20:
		print (word)
