# app.py
import streamlit as st
import calculator as calc

st.title("Scientific Calculator API")

# Function to handle API calls
def perform_calculation(operation, a, b=None):
    try:
        if operation == 'add':
            return calc.add(a, b)
        elif operation == 'subtract':
            return calc.subtract(a, b)
        elif operation == 'multiply':
            return calc.multiply(a, b)
        elif operation == 'divide':
            return calc.divide(a, b)
        elif operation == 'power':
            return calc.power(a, b)
        elif operation == 'sqrt':
            return calc.sqrt(a)
        elif operation == 'sin':
            return calc.sin(a)
        elif operation == 'cos':
            return calc.cos(a)
        elif operation == 'tan':
            return calc.tan(a)
        elif operation == 'log':
            return calc.log(a)
        elif operation == 'log10':
            return calc.log10(a)
        elif operation == 'pi':
            return calc.PI
        elif operation == 'e':
            return calc.E
        else:
            return "Invalid operation"
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit interface for user interaction
operation = st.text_input("Operation (e.g., add, subtract, sin, log)", "")
a = st.number_input("First number", step=1e-5, format="%.5f")
b = st.number_input("Second number (optional)", step=1e-5, format="%.5f")

if st.button("Calculate"):
    result = perform_calculation(operation, a, b)
    st.write(f"Result: {result}")
