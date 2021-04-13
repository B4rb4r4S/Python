# Sequence Generator #
# by Barbara Salas #

def MySequence(n): #defining a function that generates a numeric sequence 
	result=0       #result starts in zero
	if n%3!=0:     #if the numeric variable n is not divisible by 3
		result=n**2  # n will be squared and stored in result
	else:
		result = int(n/3) #otherwise, n will be divided by 3
	return (result)       #and result will be returned
	
try:  #if an error is found, execution is stopped and transferred down to except block
	query=int(input('Please enter the number of terms you want to print: ')) #input must be integers 
	if query>=0:
		print('The first',query,'terms of the sequence are: ')
		for i in range(query): #this for loop goes over from zero to the number of terms entered in query
			print(MySequence(i)) #MySequence function is called to calculate the terms of the sequence
	else:
		print ('Must be a positive integer number') #if a negative integer is entered, an error will appear
except:
	print ('Must be a positive integer number') #if the entered character is different to a positive integer, then this error message will appear
