'''
DAY 11: Advanced Functions (with *args and **kwargs)
Today I Learned about functions that could have an infinite number of arguments using *args and **kwargs:
'''

# Function with *args to accept a variable number of arguments:
def sum_all(*args):
    total = sum(args)
    print(f"The sum of all arguments is: {total}")

sum_all(1, 2, 3, 4, 5) # Output: The sum of all arguments is: 15
sum_all(29, 14, 54, 21, 78, 99) # Output: The sum of all arguments is: 295


# Function with **kwargs to accept a variable number of keyword arguments:
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

display_info(name="Mark", level="36", rule="Admin") # Output: Name: Mark \n Level: 36 \n Rule: Admin


'''
Small Exercise, summarizing JSON with *args and **kwargs:
'''

import json

def save_contacts(file_name, **info):
    with open(file_name, 'w') as f:
        json.dump(info, f, indent=4)
    print(f"Contacts saved to {file_name}")

save_contacts("contacts.json", name="Mark", phone="1234567890", email="mark@example.com")

'''
That's it for today, I learned how to use *args and **kwargs to create flexible functions!
'''