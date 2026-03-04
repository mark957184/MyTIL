'''
DAY 23: Logic thinking
Today I Realised I was going to fast recently, without understanding really what I was coding, so yeah
I also saw those hackathons on the internet and I thought, why not? Instead of training in something they asked in those competitions, I'm going to improve my problem solving skills and learn to code (at least) in Python on my own, without guides, small corrections or such things
Let's start from exercises to train my logic thinking:
'''

# Basic perceptron
target = 10
lr = 0.1
w = 1
x = 5

for _ in range(50): # Epochs
    y = w * x
    print(y)
    e = (y - target)**2 # Error
    print(e)
    w -= lr * 2 * x * (y - target) # weight change
    print(w)

print(f"final result is: {y}")


# More input network
targets = [2.1, 4.2, 5.3] # targets
x = [1, 2, 3] # Values

for _ in range(50): # Epochs
    m_slope = 0 # Average slope for the values 
    for x_input, trgs in zip(x, targets): # calculating every slope
        y = w * x_input
        m_slope += 2*x_input*(y-trgs)
        e = (y-trgs)**2 # Error
        print(e)
    w -= lr * (m_slope/3) # Final weight change


# Final complete simple perceptron
targets = [5.1, 6.9, 9.2, 11.0]
x = [0, 1, 2, 3]
bias = 0

for _ in range(50): # Epochs
    m_bias = 0 # Average bias
    m_slope = 0 # Average slope for the values
    for x_input, trgs in zip(x, targets): # Calculating every slope and bias
        y = w * x_input + bias
        m_bias += 2*(y-trgs)
        m_slope += 2*x_input*(y-trgs)
        e = (y-trgs)**2 # Error
        print(f"Error: {e}")
        print(f"Result: {y}")
    bias -= lr * (m_bias/4) # Final weight change
    w -= lr * (m_slope/4) # Final bias change


# Zipping problems
'''
Here we need to know when in a string there are repetitions so we can compress all of it's data in a smaller and lighter version of it
To do that, we check 3 words at the time, for example in MOON we'll do MOO and OON, but in words like BANANA there's a repetition in the same letters, how do we resolve this? Let's see
'''

string_to_compress = "BANANA"
l = len(string_to_compress) # length of the string
bits_of_string = {} # Bits of the string
repetitions = {} # Repetitions
i = 0

for i in range(l): # Divides the string in bits
    if i+3 <= l:
        bits_of_string[i] = string_to_compress[i:i+3]
    else:
        break

for index, bit in bits_of_string.items():
    bits_of_string1 = bits_of_string.copy()
    bits_of_string1.pop(index)
    '''
    if bit in bits_of_string1.values():    This way the repetition is registered even if it is with the same letters, we need at least 3 indexes of difference
        l1 = len(repetitions.keys())
        repetitions.update({l1: bit})
    else:
        repetitions.clear()
    '''
    
    for indexes, bits in bits_of_string1.items(): # Control the difference of indexes, if less than 3 it doesn't count it as a repetition
        if bit == bits:
                dif = abs(indexes-index)
                if dif > 2:
                    l1 = len(repetitions.keys())
                    repetitions.update({l1: bit})
                else:
                    repetitions.clear()
    
    print(repetitions) # 0 repetitions, as it should be


'''
That's enough for today, I'll continue like this for the next days!
'''