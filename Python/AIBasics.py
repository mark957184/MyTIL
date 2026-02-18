'''
DAY 20: AI basics
Today I Learned that there are a lot of AI-related tools that you could use in Raspberry Pi, but i'm not just going to use them, I want how they work
Learning how AI works is complicated and needs a lot of time and resources, i'm learning the basics for now:
'''

# So, AI can be defined as a structure of neurons, such as in our brains, that use some parameters to determine if something is true or false, bad or good, such as a child that is learning from the world...

import time
import numpy as np # This imports a library used for math and matrix calculations

# AI is trained to do tasks, repeating experiments, from which AI learns from it's errors, but how? How does a program (that uses 0's and 1's) learns from visual things or by prompts, or by words, or by anything else?

# Example of a basic Python AI (built with "neuron" class) that needs to understand how to do do the boolean operation AND
class neuron():
    def __init__(self):
        self.weights = np.random.rand(2) # This is the importance of a value and/or a value describing how correct it is, in this case in a range of values from 0 to 2
        self.bias = np.random.rand(1) # A value used to make the response more "flexible"

    # Returns what the AI thinks it is between 1 and 0
    def binary_value(self, x):
        return 1 if x > 1 else 0
    
    def predict(self, values):
        value = np.dot(values, self.weights) + self.bias
        return self.binary_value(value)

    # Trains the AI adjusting the parameters
    def train(self, values, expected_labels, num_of_training):
        for _ in range(num_of_training):
            for value, labels in zip(values, expected_labels):
                label = self.predict(value)
                error = labels - label
                print(error)
                self.weights += error*value*0.1
                self.bias += error

# Values to operate
values = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1])

ai = neuron()

# Starting the AI
print("Before training (1, 1): ", ai.predict([1, 1]))
print("Before training (0, 1): ", ai.predict([0, 1]))
print("Before training (1, 0): ", ai.predict([1, 0]))
print("Before training (0, 0): ", ai.predict([0, 0]))

# Trains the AI
ai.train(values, labels, 15) # Discovered that 15 is a good number of trainings for this AI

# Now the answers should be more correct
print("After training (1, 1): ", ai.predict([1, 1]))
print("After training (0, 1): ", ai.predict([0, 1]))
print("After training (1, 0): ", ai.predict([1, 0]))
print("After training (0, 0): ", ai.predict([0, 0]))

# It's all about math, geometry (with more complicated AI) and statistics

'''
These are the very basics things about AI, but deeper than that there are a lot of things to learn and this could probably be a challenge for the end of the Python month!
'''