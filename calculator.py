# calculator.py

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"

def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

def sin(angle):
    return math.sin(math.radians(angle))

def cos(angle):
    return math.cos(math.radians(angle))

def tan(angle):
    return math.tan(math.radians(angle))

def log(a):
    return math.log(a)

def log10(a):
    return math.log10(a)

# Constants
PI = math.pi
E = math.e
