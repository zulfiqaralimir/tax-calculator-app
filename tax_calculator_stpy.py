# Import necessary libraries
import streamlit as st

# Function to calculate tax
def calculate_tax(income, tax_rate):
    return income * (tax_rate / 100)

# Streamlit app
def main():
    st.title("Tax Calculator")

    # Input fields for income and tax rate
    income = st.number_input("Enter your income:", min_value=0)
    tax_rate = st.number_input("Enter the tax rate (%):", min_value=0, max_value=100)

    # Calculate tax
    tax = calculate_tax(income, tax_rate)

    # Display the calculated tax
    st.write(f"Tax to be paid: ${tax:.2f}")

if __name__ == "__main__":
    main()
