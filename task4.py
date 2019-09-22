#Excercise_4

"""returns true if word is made only out of those given letters else it returns flase"""
def uses_only(word, string_of_letters):
	for letter in word:
		if letter in string_of_letters:
			return True
			print("letter is in the string")
		else:
			return False
	return True

uses_only('ace','a')

