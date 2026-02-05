'''
DAY 13: Decorators
Today I Learned that decorators are a powerful feature in Python that allow you to modify the behavior of functions:
'''

def my_decorator(func):
    def wrapper():
        print("Before the function is called")
        func()
        print("After the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

'''
I sincerely didn't understand decorators, so I tried some other examples:
'''

def scream_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper() + "!!!"
        return modified_result
    return wrapper

@scream_decorator
def greet():
    return "hello there"

print(greet())  # Output: "HELLO THERE!!!"

'''----------------------------------------------------------------------------------------------------------'''

import random

def sixth_sense(func):
    def wrapper():
        original_f = func()
        modified_f = f"hmm... something is about to happen. I feel it\n{original_f}"
        return modified_f
    return wrapper

@sixth_sense
def make_something_happen():
    something = ["KABOOM!", "SPLASH!", "BOOM!", "PEW PEW!", "KABLAM!"]
    x = random.choice(something)
    return x

print(make_something_happen())

'''
That's all about decorators I think, tomorrow I'll do more practice with things I didn't understand well in those 2 weeks
'''