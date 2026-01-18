'''
DAY 2: Variables and lists

VARIABLES:
Since I already know Luau, I decided to do variables and lists in the same day
So
'''

name = "Mark"

'''
This is a variable, in particular a string, because it's a word, and it stores a word with the name we give to it
In this case we stored the word "Mark" in the "name" variable so if we print it:
'''

print(name)

'''
The output is "Mark".
But there are other types of variables: integers and floats
Integers are whole numbers and floats are decimal numbers, let's see some examples:
'''

age = 15
number = 7.65

print("My age is", age)

# Outputs "My age is 15", remember we can put "inside" a string in "print" command a variable

print("The lucky number is", number, "!")

# Outputs "The lucky number is 7.65 !"

# Here I had some difficulties as I was a lot used to Luau, even if Python is almost the same but something changes

#-----------------------------------------------------------------------------------------------------------------

'''
LISTS:
Now things get harder, as we know variables store things we need to remember, but if we have a lot of information we need to store there's a clean way to store all of that
Using lists, let's see here an example:
'''

players = ["Mark", "bro1", "bro2", "bro3"]

'''
Using "players" we can do a lot of stuff using list commands.
First command we can use in lists is .append(value), this adds an element at the end of the list:
'''

players.append("bro4")
print(players)

'''
Outputs ["Mark", "bro1", "bro2", "bro3", "bro4"]
Now second command: .insert(index, value), in this case we can choose the position (index, 0 for the first, n of values for the last) where the value is added:
'''

players.insert(1, "bro")
print(players)

'''
Outputs ["Mark", "bro", "bro1", "bro2", "bro3", "bro4"]
Third command: .extend(another_list), it attaches another list to the end of the first list (used for the command):
'''

onlinePlayers = ["stranger", "stranger1", "stranger2"]
players.extend(onlinePlayers)

print(players)

'''
Outputs ["Mark", "bro", "bro1", "bro2", "bro3", "bro4", "stranger", "stranger1", "stranger2"]
Now commands that deletes some or all values, starting from .remove(value), it removes the value we indicated:
'''

players.remove("bro4")

print(players)

# What if we wrote the value wrong and it gives an annoying error that stops everything? We'll see in the "Errors" chapter!

'''
Outputs ["Mark", "bro", "bro1", "bro2", "bro3", "stranger", "stranger1", "stranger2"]
now let's see .pop(index), it removes the value in the index we indicated:
'''

players.pop(4) # That's "bro3"

print(players)

'''
Outputs ["Mark", "bro", "bro1", "bro2", "stranger", "stranger1", "stranger2"]
You want to erase an entire list? just use .clear():
'''

example = ["example"]

example.clear() # tadà! "example" no longer exists

'''
There's a cooler way for .pop() (it lookes more advanced), del list_you_want[index]:
'''

del players[3] # That's going to be "bro2"

print(players)

'''
That's all for commands that deletes, now we'll see other commands such as .sort(), used to sort all variables in alphabetic order (variables) or/and in ascending order (for integers/floats):
'''

players.sort() 

print(players)

'''
Outputs ['Mark', 'bro', 'bro1', 'stranger', 'stranger1', 'stranger2']
>>>BEWARE: .sort() is case sensitive, so uppercases comes before lowercases

.reverse(), like .sort() but it sorts in reverse:
'''

players.reverse()

print(players)

'''
Outputs ['stranger2', 'stranger1', 'stranger', 'bro1', 'bro', 'Mark']
.copy(), it copies all the list, so we can do things like this:
'''

players2 = players.copy() # I stored a copy of "players" in another new list, "players2"

print(players2)

'''
Outputs ['stranger2', 'stranger1', 'stranger', 'bro1', 'bro', 'Mark'], just like "players"]
Now commands to get informations about lists, len(list), it outputs the length of the list:
'''

print(len(players)) # 6

'''
.count(value), counts how many times a value appears in the list:
'''

print(players.count("Mark")) # 1

'''
.index(value), it outputs the index of the indicated value:
'''

print(players.index("Mark")) # 5

'''
Last but not least, slicing (list[start:end:step])
With this command we can take just some of the values in a list, all of them, in reversed order and more in just one command:
'''

print(players[1:4]) # From the second to the fifth value, excluded (the end index is excluded) --Output: ['stranger1', 'stranger', 'bro1']

print(players[:4]) # From the start of the list to the fifth value, excluded --Output: ['stranger2', 'stranger1', 'stranger', 'bro1']

print(players[:]) # All the list --Output: ['stranger2', 'stranger1', 'stranger', 'bro1', 'bro', 'Mark']

print(players[::2]) # all the list with a step of 2 --Output: ['stranger2', 'stranger', 'bro']

print(players[-1]) # the last value --Output: Mark

print(players[-2]) # the second-last value --Output: bro

print(players[::-1]) # all the list in reverse --Output: ['Mark', 'bro', 'bro1', 'stranger', 'stranger1', 'stranger2']