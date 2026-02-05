'''
DAY 12: Generators and Yield
Today I Learned about generators in Python and how to use the 'yield' statement to create them. Generators are a type of iterable but they generate values on the fly and do not store them in memory
This makes them more memory efficient for large datasets or infinite sequences. The 'yield' statement is used in a function to produce a series of values over time, pausing the function's state between each yield:
'''

def count_up_to(max):
    count = -1
    while count < max:
        count += 1
        print(count)

count_up_to(5000)