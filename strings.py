def reverseAllChars (inputString) :
	newString = ''
	for i in range(len(inputString)-1, -1, -1) :
		newString += inputString[i]
	return newString

print reverseAllChars("hello this is my home")

def reverseCharsInWords (inputString) :
	strlist = inputString.split(' ')
	strlist = [reverseAllChars(item) for item in strlist]
	return ' '.join(strlist)

print reverseCharsInWords("no this is my home")

def reverseWordsInString (inputString) :
	strlist = inputString.split(' ')
	return ' '.join(strlist[::-1])

print reverseWordsInString("This is both our homes.")

def reverseOddWords (inputString) :
	strlist = inputString.split(' ')
	for i in range(0, len(strlist), 2) :
		strlist[i] = reverseAllChars(strlist[i])
	return ' '.join(strlist)

print reverseOddWords("This is all our homes")

def addWordNum (inputString) :
	strlist = inputString.split(' ')
	for i in range(len(strlist)) :
		strlist[i] += str(i+1)
	return ' '.join(strlist)

print addWordNum("Who cares whose home it is")