'''
DAY 5: Functions and classes
Today I Learned that in Python, we use functions to do multiple things in one line of code, multiple times, whenever we want
Functions are also used to do operations with the data you give to it in that line of code you use to call a function (that's possible with the 'return' command, inside the function):
'''

def check_grade(name, grade):
    if grade >= 60:
        print(f"Good job, {name}! You've passed the test") # If grade is greater than 60, you've passed the test...
    elif grade < 60:
        print(f"Maybe you need to study more, {name} :(") # if not you'll be told to study more

students = ["Mark", "John", "Pork"] # List of students
grades = [100, 48, 63] # Their relative grades

def all_students(): # Make the function for every student (function of a function)
    n = 0 # First student
    for student in students:
        check_grade(student, grades[n]) # Executes the function, with all student and their relative grades
        n += 1 # It executes 3 times, so at the end I'm changing the student (by changing the index for the students list)


all_students() # Makes everything work

'''
This is one of the most complex code I probably did with a new language (for me) such as Python, but there is still something to try
Caling 'return' in a function! We can use it for like math problems or things like this, that require an answer:
'''

def subtracting_and_adding(n, m): # A math function that makes a list of both the addition and the subtraction of 2 numbers
    ans = n - m
    ans1 = n + m
    return ans, ans1

subadd = subtracting_and_adding(7, 3) # List of the results, took thanks to the 'return' statement
subadd1 = f"{subadd[0]} and {subadd[1]}" # Converting the list in a string
print(f"The results for the addition and subtraction of 7 and 3 are: {subadd1}") # Printing the final result

'''
Now the biggest thing I learned in Python so far, classes
Those are like a library of functions (a function squared), with multiple possible inputs by calling the class with a name
Here a code I made:
'''

class BotConfig:
    def __init__(self, name, version, creator): # def __init__ it's like a section to store data in subvariables of 'self', all data got from the line where you call the class
        self.name = name
        self.version = version
        self.creator = creator

    def get_info(self): # A function that prints the given info, here remember to just put 'self' in the arguments, It took a lot to me to fix that
        print("---------BOT INFO---------")
        print(f"Name: {self.name}")
        print(f"Version: {self.version}")
        print(f"Creator: {self.creator}")
        print("--------------------------")

bot = BotConfig("PyBot", "1.2.4", "Mark")

bot.get_info()

'''
I got all the basics for Python now, I'll spend the next days starting to analyze some code like in discord.py (maybe easier files or some Python exercise online)
So I can find new things to learn and I'll try to comprehend the code, line by line!
'''
