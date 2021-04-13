# String Processing #
# by Barbara Salas #

def Mywords(n): #defining a function that counts words from a sentence or paragraph
	for char in '*"():;!/?-.,\n':   #Those characteres different to words
		n=n.replace(char,' ')       #are replaced by a space
	words = n.split() #spliting the sentence or paragraph in words delimited by any length of space between them
	return len(words) #delivering the total number of words
	
def CountSpace(n): #defining a function that counts spaces from a sentence or paragraph
	spaces=0       #counter of spaces starts in zero
	for i in range(len(n)):  #this for loop goes over the input until the last character
		if (n[i]==' '):      #if a character from the input is equal to space 
			spaces=spaces+1  #then it must be counted  
	return (spaces)          #and return the number of spaces
	
def Countervowels(n): #defining a function that counts the number of vowels in a sentence or paragraph
	vowels=0          #counter of vowels starts in zero
	n=n.lower()       #to consider upper and lowercase vowels all letters are converted into a lowercase
	for i in range (len(n)):   #this for loop goes over the input until the last character
		if (n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u'): #if a character from 
			vowels=vowels+1            #the input is equal to any vowel, then it must be counted
	return (vowels)       #and return the number of spaces
	
#begin
phrase=input('Please enter a word, sentence or paragraph: ') #a user enter a senquence or paragraph
print('How many words are in your text?')
print (Mywords(phrase))   #Mywords function is called to count the number of words in that input
print('How many spaces are in your text?')
print(CountSpace(phrase))  #CountSpace function is called to count the number of spaces in that input
print('How many vowels are in your text?')
print(Countervowels(phrase)) #Countervowels function is called to count the number of vowels in that input