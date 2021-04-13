# Animated Banner Program
# By Barbara Salas


#allows us to clear the console screen.
import os
import time

#***** Variables *****

#the printed banner version of the message
#this is a 7-line display, stored as 7 strings
#initially, these are empty.
printedMessage = [ "","","","","","","" ]
WIDTH = 79 #79 was replaced by 5 to answer question 5.
characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "A" : [ "  *  ",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ],


               "B" : [ "**** ",
                       "*   *",
                       "*   *",
                       "**** ",
                       "*   *",
                       "*   *",
                       "**** "],

               "C" : [ " *** ",
                       "*   *",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*   *",
                       " *** "],

               "D" : [ "**** ",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "**** "],


               "E" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    ",
                       "*****" ],

               "F" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    ",
                       "*    " ],

               "G" : [ " *** ",
                       "*   *",
                       "*    ",
                       "* +* ",
                       "*   *",
                       "*   *",
                       " *** "],

               "H" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ],

               "I" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "*****" ],

               "J" : [ "*****",
                       "    *",
                       "    *",
                       "    *",
                       "    *",
                       "*   *",
                       " *** " ],

               "K" : [ "*   *",
                       "*  * ",
                       "* *  ",
                       "**   ",
                       "* *  ",
                       "*  * ",
                       "*   *" ],

               "L" : [ "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],

               "M" : [ "*   *",
                       "** **",
                       "* * *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *" ],

               "N" : [ "*   *",
                       "**  *",
                       "* * *",
                       "*  **",
                       "*   *",
                       "*   *",
                       "*   *" ],

               "O" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],

               "P" : [ "**** ",
                       "*   *",
                       "*   *",
                       "**** ",
                       "*    ",
                       "*    ",
                       "*    " ],

               "Q" : [ " *** ",
                       "*   *",
                       "*   *",
                       "*   *",
                       "* * *",
                       " *** ",
                       "    *" ],

               "R" : [ "**** ",
                       "*   *",
                       "*   *",
                       "**** ",
                       "*   *",
                       "*   *",
                       "*   *" ],

               "S" : [ " *** ",
                       "*    ",
                       "*    ",
                       " *** ",
                       "    *",
                       "    *",
                       " *** " ],

               "T" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  " ],

               "U" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       " *** " ],

               "V" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       " * * ",
                       "  *  " ],

               "W" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "* * *",
                       "** **",
                       "*   *" ],

               "X" : [ "*   *",
                       " * * ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       " * * ",
                       "*   *" ],

               "Y" : [ "*   *",
                       " * * ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  " ],

               "Z" : [ "*****",
                       "    *",
                       "   * ",
                       "  *  ",
                       " *   ",
                       "*    ",
                       "*****" ],

               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ]

               }
			   
def savemessage (printedMessage):
	try:		
		file = open("C:\\Users\\Admin\\Desktop\\message.txt", "a") # create the file
		for row in range(7):
			file.write(printedMessage[row] + '\n') #This line adds the seven rows one by one until the last row 
		file.write('\n')	#a line break is added to display a more ordered outcome text	
		file.close() #this text file is closed
		return (0) #this line returns 0 as true, this part was executed
	except:
		print('Error: File cannot be created or opened') #For any error, a message will be shown
		return (1) #this line will return 1 as false due to the error

def display(message): 
	#build up the printed banner. To do this, the 1st row of the display is created for each 
	#character in the message, followed by the second line, third line and so on until the seventh line
	for row in range(7): #means that the index ‘row’ will go over from index 0 to 6, this is 7-1 as maximum limit of this range
		for char in message: #it goes through the range ‘message’ with the index ‘char’
			try:
			#save in printmessage, line by line of each character from the map of letters
				printedMessage[row] += (str(characters[char][row]) + "  ")
			except: 
				print ('ERROR: Invalid character: ', char) #This means that if it is not defined, then it will fail
				return(1) #return(1) means that an error has occured
				
	if (savemessage(printedMessage)== 0): #This line put a condition and calls the function
	
		offset = WIDTH
		while True:
			os.system("cls") #this command clears the screen
			for row in range(7): #print each line of the message, including the offset.
				print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset]) #This prints a part of the string according to indexes in a range of 79
			
			offset -=1 #move the message a little to the left.
			#if the entire message has moved 'through' the display then
			#start again from the right hand side.
			if offset <= ((len(message)+2)*6) * -1:
				offset = WIDTH
				
			time.sleep(0.05) #take out or change this line to speed up / slow down the display				
		
message = input("Enter a phrase: ") #the message we want to print

if (message.strip() == ''): #strip will delete all spaces before or after the message. If spaces o nothing is entered, this will delivery an error message
	print ('A data must be entered') #if user enters nothing, then this message will be displayed.
else:
	display(message.upper())#'display' function is called with 'message' as argument,This message is converted into uppercase
