'''
DAY 24: Boolean logics
Today I Learned that all the logic behind computers were first thought in the nineteeth century, especially by George Boole, an important mathematician and logician
He invented the boolean math, essentially the math of modern computers, with laws about operations with true and false, here what I learned by myself:
'''

# True and False
a = True  # First input
b = False  # Second input
y = None  # result



# NOT: one input, opposite output
print("---------- NOT ----------")
a = True
y = not a
print(f"NOT {a} = {y}")

a = False
y = not a
print(f"NOT {a} = {y}\n")



# BUFFER: one input, same output (NOT(NOT A))
print("---------- BUFFER ----------")
a = True
y = not(not a) # a
print(f"{a} = {y}")

a = False
y = not(not a)
print(f"{a} = {y}\n")



# AND: gives 1, when all inputs are 1
print("---------- AND ----------")
a = True
b = True
y = True if a and b else False
print(f"{a} * {b} = {y}")  # AND operation is written as a moltiplication

a = True
b = False
y = True if a and b else False
print(f"{a} * {b} = {y}")

a = False
b = True
y = True if a and b else False
print(f"{a} * {b} = {y}")

a = False
b = False
y = True if a and b else False
print(f"{a} * {b} = {y}\n")  # With inputs, there are 2**n of inputs of possible combinations (in this case 4, 2**2)



# OR: gives 1, when at least one input is 1
print("---------- OR ----------")
a = True
b = True
y = True if a or b else False
print(f"{a} + {b} = {y}")  # OR operation is written as a addition

a = True
b = False
y = True if a or b else False
print(f"{a} + {b} = {y}")

a = False
b = True
y = True if a or b else False
print(f"{a} + {b} = {y}")

a = False
b = False
y = True if a or b else False
print(f"{a} + {b} = {y}\n")



# XOR: exclusive OR, true when just one of the inputs is 1
print("---------- XOR ----------")
a = True
b = True
y = True if (a and not b) or (not a and b) else False
print(f"({a} * NOT {b}) + (NOT {a} * {b}) = {y}")  # XOR operation can be written in different ways (↓ laws and principles)

a = True
b = False
y = True if (a and not b) or (not a and b) else False
print(f"({a} * NOT {b}) + (NOT {a} * {b}) = {y}")

a = False
b = True
y = True if (a and not b) or (not a and b) else False
print(f"({a} * NOT {b}) + (NOT {a} * {b}) = {y}")

a = False
b = False
y = True if (a and not b) or (not a and b) else False
print(f"({a} * NOT {b}) + (NOT {a} * {b}) = {y}\n")



# NAND: negation of AND, true when at least one input is 0
print("---------- NAND ----------")
a = True
b = True
y = True if not (a and b) else False
print(f"NOT ({a} * {b}) = {y}")  # NAND operation can be written in different ways

a = True
b = False
y = True if not (a and b) else False
print(f"NOT ({a} * {b}) = {y}")

a = False
b = True
y = True if not (a and b) else False
print(f"NOT ({a} * {b}) = {y}")

a = False
b = False
y = True if not (a and b) else False
print(f"NOT ({a} * {b}) = {y}\n")



# NOR: negation of OR, true when all inputs are 1
print("---------- NOR ----------")
a = True
b = True
y = True if not (a or b) else False
print(f"NOT ({a} + {b}) = {y}")  # NOR operation can be written in different ways

a = True
b = False
y = True if not (a or b) else False
print(f"NOT ({a} + {b}) = {y}")

a = False
b = True
y = True if not (a or b) else False
print(f"NOT ({a} + {b}) = {y}")

a = False
b = False
y = True if not (a or b) else False
print(f"NOT ({a} + {b}) = {y}\n")



# XNOR: negation of XOR, true when both inputs are 1 or 0
print("---------- XNOR ----------")
a = True
b = True
y = True if (a and b) or (not a and not b) else False
print(f"({a} * {b}) + (NOT {a} * NOT {b}) = {y}")  # XNOR operation can be written in different ways

a = True
b = False
y = True if (a and b) or (not a and not b) else False
print(f"({a} * {b}) + (NOT {a} * NOT {b}) = {y}")

a = False
b = True
y = True if (a and b) or (not a and not b) else False
print(f"({a} * {b}) + (NOT {a} * NOT {b}) = {y}")

a = False
b = False
y = True if (a and b) or (not a and not b) else False
print(f"({a} * {b}) + (NOT {a} * NOT {b}) = {y}\n")



# LAWS AND PRINCIPLES: how boolean math works

## LAWS COMMON IN BOTH MATH AND BOOLEAN ALGEBRA:
### ASSOCIATIVE PROPERTIES
'''
a * (b * c) = b * (a * c)
a + (b + c) = b + (a + c)
'''

### COMMUTATIVE PROPERTIES
'''
a + b = b + a
a * b = b * a
'''

### DISTRIBUTIVE PROPERTY
'''
a * (b + c) = (a * b) + (a * c)
'''

### IDENTITY PROPERTIES
'''
a * 1 = a
a + 0 = a
'''

### ANNIHILATOR PROPERTY
'''
a * 0 = 0
'''


## LAWS VALID JUST IN BOOLEAN ALGEBRA:
### ANNIHILATOR PROPERTY
'''
a + 1 = 1  # Here, for example, the result would be 1 just when a = 0 in math
'''

### IDEMPOTENCE PROPERTIES
'''
# Same thing here, in math the result would be different (2a and a**2)
a + a = a
a * a = a
'''

### ABSORPTION PROPERTIES
'''
a + (a * b) = a
a * (a + b) = a
'''

### DISTRIBUTIVE PROPERTY
'''
a + (b * c) = (a + b) * (a + c)
'''

### COMPLETITION LAWS
'''
a + NOT a = 1
a * NOT a = 0
'''

### DOUBLE NEGATION LAW (OR INVOLUTION LAW)
'''
a = NOT(NOT a)  # This is how buffers work
'''

### DE MORGAN'S LAWS
'''
# That's why there are different ways to write, for example, the NOR (NOT (a + b) = NOT a * NOT b)
NOT (a * b) = NOT a + NOT b
NOT (a + b) = NOT a * NOT b
'''