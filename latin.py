pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
	print original
	word=original.lower()  #converts to lowercase
	first=word[0]    			#Holds the First letter
	if first=='a' or first=='e' or  first=='i' or  first=='o' or first=='u':
		print "vowel"
		new_word=word+pyg
		print new_word
	else:
		new_word=word[1:len(original)]+word[0]+pyg
		print "consonant"
else:
	print 'empty'
