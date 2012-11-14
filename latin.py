#English to PygLatin converter
#If the word user entered is starting with a vowel then 'ay' is added to the end of the word
#if the word doesn't have a vowel infront of it then the first letter + 'ay' is added to the last




pyg = 'ay'              #pyg is used add ay at the end of the string

original = raw_input('Enter a word:')            #getting an input from the user

if len(original) > 0 and original.isalpha():     #checking if the string is valid
	print original
	word=original.lower()                    #converts to lowercase
	first=word[0]    			 #Holds the First letter
	if first=='a' or first=='e' or  first=='i' or  first=='o' or first=='u':  #checking if the first letter is vowel
		print "vowel"
		new_word=word+pyg
		print new_word
	else:
		new_word=word[1:len(original)]+word[0]+pyg  
		print "consonant"
else:
	print 'empty'
