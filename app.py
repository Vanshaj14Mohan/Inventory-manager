# app.py
# Streamlit-based Smart Inventory Manager
import streamlit as st
from datetime import date, datetime
from product import Product
from inventory import Inventory

# Initialize inventory (in-memory for simplicity)
if 'inventory' not in st.session_state:
    st.session_state['inventory'] = Inventory()

inventory = st.session_state['inventory']

st.title('Smart Inventory Manager')

# Section to add a new product
st.header('Add Product')
with st.form('add_product_form'):
    name = st.text_input('Product Name')
    category = st.text_input('Category')
    quantity = st.number_input('Quantity', min_value=1, step=1)
    expiry = st.date_input('Expiry Date (optional)', value=None, min_value=date.today(), key='expiry', disabled=False)
    submitted = st.form_submit_button('Add Product')
    if submitted:
        expiry_date = expiry if expiry != date.today() else None
        product = Product(name, category, quantity, expiry_date)
        inventory.add_product(product)
        st.success(f'Added {name}')

# Section to remove a product
st.header('Remove Product')
remove_name = st.text_input('Enter product name to remove')
if st.button('Remove'):
    inventory.remove_product(remove_name)
    st.success(f'Removed {remove_name}')

# Section to list all products
st.header('Product List')
products = inventory.list_products()
if products:
    for p in products:
        st.write(f"Name: {p.name}, Category: {p.category}, Quantity: {p.quantity}, Expiry: {p.expiry_date}")
else:
    st.info('No products in inventory.')

# Auto-alert for perishable items expiring soon
st.header('Expiring Soon (within 5 days)')
expiring = inventory.get_expiring_soon()
if expiring:
    for p in expiring:
        st.warning(f"{p.name} (expires on {p.expiry_date})")
else:
    st.success('No items expiring soon!')
