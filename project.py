import streamlit as st
import pandas as pd

# Set page title
st.title("☕ Cafe Management System ☕")

# Sidebar menu
st.sidebar.header("📜 Cafe Menu")

# Menu Items & Prices
menu = {
    "☕ Coffee": 200,
    "🍵 Tea": 150,
    "🥐 Croissant": 250,
    "🍩 Donut": 180,
    "🍰 Cake": 300
}

# Order selection
order = {}
for item, price in menu.items():
    qty = st.sidebar.number_input(f"{item} (Rs. {price})", min_value=0, max_value=10, step=1)
    if qty > 0:
        order[item] = qty

# Display Order Summary
st.subheader("🛒 Your Order Summary")
if order:
    order_df = pd.DataFrame(list(order.items()), columns=["Item", "Quantity"])
    order_df["Price per item"] = order_df["Item"].map(menu)
    order_df["Total Price"] = order_df["Quantity"] * order_df["Price per item"]
    
    st.table(order_df)  # Display order summary table
    
    total_bill = order_df["Total Price"].sum()
    st.markdown(f"### 🏷️ Total Bill: Rs. {total_bill}", unsafe_allow_html=True)

    # Confirm Order Button
    if st.button("✅ Confirm Order"):
        st.success("Your order has been placed successfully! 🎉")
else:
    st.info("Please select items from the menu to place an order.")

