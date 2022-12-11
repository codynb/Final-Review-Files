#Cody Brown: Final Exam Review: Files

#File vs Variable?
    #Files live in permanent stroaged on computer's hard drive, where a variable
    #disappears after a program is closed, variable is internal, file can be
    #used by more than one code

#File Characteristics
    #Has a name: example.txt
    #Has a directory name: /Users/Cody
    #Has full path name: /Users/Cody/example.txt
    #Can be moved from one directory to another
    #Name can be changed
    #Can be copied
    #Can be VERY BIG

#READING AN EXISTING FILE
    # first, creating a folder on my desktop manaully, calld "FilesRv"
    # second, creating a python  folder, manually in that folder called "filex1.py"
    # third, creating .txt file with lines a song lyric in that folder called "lyric.txt"
# # Reading the file line by line
# -----------
op = open('lyric.txt')
    #opening the file
op1 = op.readline()
print(op1)
    #this printed only the FIRST line of the lyric.txt file
op2 = op.readline()
print(op2)

op3 = op.readline()
print(op3)
    #All .readline() together read the first 3 lines of the lyric.txt file
 ## Reading a file in it's entirety
 #need a for loop:
op = open('lyric.txt')
    # remember to always open the file!
for line in op:
    print(line)
# ----------
#
#  REMOVING TABS AND SPACES
#  using premade "tabs.txt", we are going to remove the bad tabs
# ------------
tabs = open('tabs.txt')
tabsr = tabs.readline()
print(tabsr)
    #This printed the first line
print(len(tabsr))
    #The length is 24
tabs2 = tabsr.strip()
print(tabs2)
    #This printed the first line again
print(len(tabs2))
    #This printed 22
# -------------
# in summary, .strip() removes the whitespace from a string
#
#  WRITING IN FILES THAT ALREADY EXIST AND CREATING NEW FILES
# This empty file is called 'writing.txt', it has some random words throughout
# -------------
writ = open("writing.txt")
#printing what it is in it currently
for line in writ:
    print(line)
    #this prints every line
#in order to write in a file, it needs to have the mode 'w' as a second paramter
writ2 = open("writing.txt",'w')
# --------------
# This command CLEARS what was written in the text file completely, it is now empty
# If this command is used, and the file indicated doesn't exist, it will create a
# new file named/and the type of whatever is in the first parameter!
# --------
createnote = open('note3.txt', 'w')
createpy = open('pyex.py','w')
# ---------
#     Now, the folder where this python document is located has two new files!
#     note3.txt and pyex.py!
#
#  WRITING IN FILES
# Adding text into a text file
# ---------
story = open("myStory.txt", 'w')
    #Recall that this either deletes all information in myStory.txt file if it exists,
    #or if it does not exist, will create a new file called myStory.txt
firstline = "Dear reader, this is a story about... \n"
story.write(firstline)
# ---------
#     This .write() added the firstline into the myStory.txt!
# Adding code into a python file
# ---------
code = open('pyex.py','w')
code1 = 'for i in range(4):\n'
code.write(code1)
    #this added the line 'for i in range(4)'
code2 = '   print(i)'
code.write(code2)
    #now, pyex.py has the following:
        #for i in range(4):
        #   print(i)
code.close()
# ---------
#
#  FORMAT OPERATOR
# Arguments for the .write() command have to be strings. But sometimes we want to put
# values in a file, what is the easiest way to convert them to strings?
#     Could use str
#     OR the format operator, %
# % applied to integers: it is the modulus operator, gives remainder of a division
# % applied to strings: becomes the formato
# Format Sequences:
#     %d : the second operand should be formatted as an integer
#     %f : the second operand should be formatted as an float
#     %s : the second operand should be formatted as a string
#     %first.secondf : the second operand should be formatted as a float,
#         here, "first" fives the number of decimal places to look at for a number
#         "second" gives the number of decimal points
# examples of %first.secondf
# ---------
m = 2.51525354
s = "%4.1f" %m
s
# prints ' 2.5'
len(s)
# prints 4
t = "%10.3f" %m
len(t)
prints 10
# ----------
# Multiple Format Operators
#     we use a tuple when using multiplle format operators in a sentence
# for example:
# --------
gender = 'female'
age = 19
height = 5.10
first_line = 'A %d years old, %s student, who is %f tall' %(age, gender, height)
first_line
# ------
# prints 'A 19 years old, female student, who is 5.100000 tall'
