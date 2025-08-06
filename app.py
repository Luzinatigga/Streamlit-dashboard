import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("cleaned_expense_data.csv")

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar filters
st.sidebar.header("🔍 Filter Expenses")
selected_category = st.sidebar.selectbox("Select Category", ["All"] + sorted(df['Category'].unique().tolist()))

# Apply filters
filtered_df = df.copy()
if selected_category != "All":
    filtered_df = filtered_df[filtered_df['Category'] == selected_category]

# Main Title
st.title("💰 Personal Expense Dashboard")
st.caption("Track your monthly spending, visualize your habits, and identify where your money goes.")

# KPIs
total_spent = filtered_df['Amount'].sum()
top_category = filtered_df.groupby("Category")["Amount"].sum().idxmax()

st.subheader("📊 Key Metrics")
col1, col2 = st.columns(2)
col1.metric("Total Spent", f"₹{total_spent:.2f}")
col2.metric("Top Category", top_category)

# Expenses Table
st.subheader("📋 Expense Table")
st.dataframe(filtered_df, use_container_width=True)

# Pie Chart: Expense by Category
st.subheader("🧾 Expense Breakdown by Category")
category_totals = filtered_df.groupby("Category")["Amount"].sum()

fig, ax = plt.subplots()
ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Top 5 Expenses
st.subheader("💸 Top 5 Biggest Expenses")
top5 = filtered_df.sort_values(by="Amount", ascending=False).head(5)
st.dataframe(top5, use_container_width=True)

# Footer
st.caption("Created by Luzina Tigga 💖 | Built with Streamlit")
