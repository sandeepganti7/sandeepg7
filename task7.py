#Exercise7
def three_consec(word):
	index = 0
	count = 0
	while index < len(word) - 1:
		if word[index] == word[index + 1]:
			count += 1
			index += 2
			if count == 3:
				return ("Found !!!!")
			else:
				count = 0
				index += 1
	return ("Not Found !!!", count)
three_consec('blaaap')

