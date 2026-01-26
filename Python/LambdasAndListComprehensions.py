'''
DAY 9: Lambdas and list comprehensions
Today I learned some faster ways to do cycles and functions with Lambda (like a smaller function) and list comprehension (a cycle like for but written in one line of code)
Those are small things but very useful to make things faster and easier, like in here:
'''

# Don't use this:
costs = [20, 50, 55, 80, 45, 75, 10]

for x in costs:
    if x >= 50:
        x * 0.9
        print(x) # Prints 45.0, 49.5, 72.0, 67.5


# Use this instead:
costs = [20, 50, 55, 80, 45, 75, 10]
sales = [x * 0.9 for x in costs if x > 50] # A lot cleanier!

print(sales)

'''--------------------------------------------------------------------------------------------------------------------'''

duplicate = lambda x: x * 2 # In just 1 line of code
print(duplicate(5))

'''
That's all, i'll check around for something else to learn!
'''