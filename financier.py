import streamlit as st
import pandas as pd

# Initialize session state to keep track of transactions and balance
if 'transactions' not in st.session_state:
    st.session_state.transactions = []
if 'balance' not in st.session_state:
    st.session_state.balance = 0

# Title of the app
st.title("Expense Tracker")

# Sidebar for input
st.sidebar.header("Add Transaction")
description = st.sidebar.text_input("Description", "")
amount = st.sidebar.number_input("Amount", min_value=0.01, format="%.2f")
transaction_type = st.sidebar.selectbox("Transaction Type", ["Income", "Expense"])

# Function to add a new transaction
def add_transaction(description, amount, transaction_type):
    transaction = {
        "description": description,
        "amount": amount,
        "type": transaction_type,
    }
    
    st.session_state.transactions.append(transaction)

    # Update the balance based on the transaction type
    if transaction_type == "Income":
        st.session_state.balance += amount
    elif transaction_type == "Expense":
        st.session_state.balance -= amount

# Button to add transaction
if st.sidebar.button("Add Transaction"):
    if description and amount:
        add_transaction(description, amount, transaction_type)
        st.success(f"Transaction added: {description} - {amount} ({transaction_type})")
    else:
        st.error("Please enter both description and amount.")

# Display Transaction History
st.header("Transaction History")
if st.session_state.transactions:
    transactions_df = pd.DataFrame(st.session_state.transactions)
    st.dataframe(transactions_df)

else:
    st.write("No transactions yet.")

# Display the balance
st.header("Balance")
st.write(f"Current Balance: ${st.session_state.balance:.2f}")

# Styling (optional)
st.markdown("""
    <style>
        .css-18e3th9 {
            background-color: #f4f4f4;
        }
        .css-1v3fvcr {
            font-size: 24px;
            color: #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)
