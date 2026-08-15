import streamlit as st
import math

st.title("Vaibhav's Advanced Calculator")
st.write("Mathematical and Physical calculations in one place.")

# Dropdown to choose the category
category = st.selectbox("Select Category:", ["Basic Math", "Advanced Math", "Physics"])

st.markdown("---")

if category == "Basic Math":
    st.header("Basic Mathematics")
    num1 = st.number_input("First Number:", value=0.0)
    num2 = st.number_input("Second Number:", value=0.0)
    
    op = st.selectbox("Select Operation:", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])
    
    if st.button("Calculate"):
        if op == "Addition (+)": 
            st.success(f"Result: {num1 + num2}")
        elif op == "Subtraction (-)": 
            st.success(f"Result: {num1 - num2}")
        elif op == "Multiplication (*)": 
            st.success(f"Result: {num1 * num2}")
        elif op == "Division (/)": 
            if num2 != 0: 
                st.success(f"Result: {num1 / num2}")
            else: 
                st.error("Error: Cannot divide by zero!")

elif category == "Advanced Math":
    st.header("Advanced Mathematics")
    math_op = st.selectbox("Select Formula:", ["Square Root", "Factorial", "Sine", "Cosine", "Tangent"])
    num = st.number_input("Enter Number:", value=0.0)
    
    if st.button("Calculate"):
        if math_op == "Square Root":
            if num >= 0: 
                st.success(f"Result: {math.sqrt(num)}")
            else: 
                st.error("Error: Cannot calculate square root of a negative number!")
                
        elif math_op == "Factorial":
            if num >= 0 and num.is_integer(): 
                st.success(f"Result: {math.factorial(int(num))}")
            else: 
                st.error("Error: Factorial requires a non-negative integer!")
                
        elif math_op == "Sine": 
            st.success(f"Result: {math.sin(math.radians(num))} (calculated in degrees)")
        elif math_op == "Cosine": 
            st.success(f"Result: {math.cos(math.radians(num))} (calculated in degrees)")
        elif math_op == "Tangent": 
            st.success(f"Result: {math.tan(math.radians(num))} (calculated in degrees)")

elif category == "Physics":
    st.header("Physics Formulas")
    phy_op = st.selectbox("Select Calculation:", ["Force", "Speed", "Kinetic Energy"])
    
    if phy_op == "Force":
        st.write("**Formula:** Force (F) = Mass (m) * Acceleration (a)")
        m = st.number_input("Mass (in kg):", value=0.0)
        a = st.number_input("Acceleration (in m/s²):", value=0.0)
        if st.button("Calculate Force"): 
            st.success(f"Result: {m * a} Newtons (N)")
            
    elif phy_op == "Speed":
        st.write("**Formula:** Speed (v) = Distance (d) / Time (t)")
        d = st.number_input("Distance (in meters):", value=0.0)
        t = st.number_input("Time (in seconds):", value=1.0)
        if st.button("Calculate Speed"):
            if t != 0: 
                st.success(f"Result: {d / t} m/s")
            else: 
                st.error("Error: Time cannot be zero!")
                
    elif phy_op == "Kinetic Energy":
        st.write("**Formula:** Kinetic Energy (KE) = 0.5 * Mass (m) * Velocity (v)²")
        m = st.number_input("Mass (in kg):", value=0.0)
        v = st.number_input("Velocity (in m/s):", value=0.0)
        if st.button("Calculate Energy"): 
            st.success(f"Result: {0.5 * m * (v**2)} Joules (J)")
      
