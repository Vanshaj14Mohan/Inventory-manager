# product.py
# This module defines the Product class for inventory items.
from datetime import date

#Initialize a product name, category, quantity, expiry date 
class Product:
    def __init__(self, name: str, category: str, quantity: int, expiry_date: date = None):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.expiry_date = expiry_date

    def is_perishable(self):
        # Return True if the product has an expiry date.
        return self.expiry_date is not None 