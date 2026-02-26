'''
DAY 22: He Kaiming Initialization
Today I Learned that the way we initialize the weights of a neural network can have a huge impact on how it learns, sometimes for situations where 2 neurons are more than sufficient those could "die" even before training
Everything depends on how we initialize the weights, so it's important 
'''

import numpy as np

input_size = 2 # How many inputs
hidden_size = 4 # Number of neurons in hidden layers
output_size = 1 # Output neurons

W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2 / input_size) # Hidden layer neuron's weights
b1 = np.zeros((1, hidden_size)) # Hidden layer neuron's biases
W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2 / hidden_size) # Output neuron's weight
b2 = np.zeros((1, output_size)) # Output neuron's biases

'''
This is how most of the LLMs (Large Language Models) initialize their weights, it's one of the most accurate initializations (the level of math needed to understand how it works is unhuman, I'll keep my curiosity aside for now, maybe one day I'll understand it)!
'''