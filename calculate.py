import streamlit as st
import math

def main():
    st.set_page_config(page_title="Attractive Calculator", page_icon="🧮")

    # Safe CSS injection
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0d1117;
            color: white;
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff8a00, #e52e71);
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
            width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🔥 Super Attractive Calculator 🔥")

    num1 = st.number_input("Enter first number", value=0.0, step=0.1)
    num2 = st.number_input("Enter second number", value=0.0, step=0.1)

    operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Square Root (First Number)"])

    if st.button("Calculate ✨"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Error! Division by zero"
        elif operation == "Power":
            result = math.pow(num1, num2)
        elif operation == "Square Root (First Number)":
            result = math.sqrt(num1) if num1 >= 0 else "Error! Negative number"
        
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
