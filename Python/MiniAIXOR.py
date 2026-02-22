'''
DAY 21: Mini AI XOR
Today I Learned that neurons alone can't do much, but a network of neurons can do more complicated stuff, as mathematically a neuron creates just a line, where the objective is to divide some elements (let's call those blue) from other elements (red)
When blue and red elements are "mixed" (can't be divided by just one line), we use more neurons divided in layers, the layers in the middle are called hidden layers
In this case I'll use 5 neurons to make a AI XOR port, that outputs 1 when only one of the inputs is 1:
'''

import numpy as np

# FUNCTIONS
def relu(x):
    return np.where(x > 0, x, x * 0.1)

def relu_derivative(x):
    return np.where(x > 0, 1, 0.1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# DATA 
## Inputs and labels:
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

## Weights and biases:
W1 = np.random.randn(2, 4) * 0.01  # 4 hidden neurons
b1 = np.zeros((1, 4)) # Bias
W2 = np.random.randn(4, 1) * 0.01  # 1 output neuron
b2 = np.zeros((1, 1))

## Learning rate:
learning_rate = 0.1

# Training
for epoch in range(20000):
    # Forward pass
    z1 = np.dot(X, W1) + b1 
    a1 = relu(z1) # 4 hidden neurons output
    z2 = np.dot(a1, W2) + b2
    output = sigmoid(z2) # Final output

    # Error
    loss = np.mean(np.square(y - output))

    # Backpropagation
    d_output = (y - output) * sigmoid_derivative(output)
    
    # Hidden layer's error
    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * relu_derivative(a1)

    # Update values
    W2 += a1.T.dot(d_output) * learning_rate
    b2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    W1 += X.T.dot(d_hidden) * learning_rate
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate
    if epoch % 500 == 0:
        #print(a1) # Just debug
        print(f"Epoch: {epoch}, Error: {loss:.4f}")

print("\nAFTER TRAINING")
for i in range(len(X)):
    pred = sigmoid(np.dot(relu(np.dot(X[i], W1) + b1), W2) + b2)
    print(f"Input: {X[i]}, Target: {y[i]}, Output: {pred[0][0]:.4f}")

'''
That's a lot for today, I'll pause watching some docs and learning with lighter stuff, first time doing even a small neural network is exausting
'''
