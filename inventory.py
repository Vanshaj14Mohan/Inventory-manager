# inventory.py
# This module manages the inventory of products.
from datetime import date, timedelta
from product import Product

class Inventory:
    def __init__(self):
        # Store products in a list
        self.products = []

    def add_product(self, product: Product):
        # Add a product to the inventory.
        self.products.append(product)

    def remove_product(self, name: str):
        # Remove a product by name.
        self.products = [p for p in self.products if p.name != name]

    def list_products(self):
        # Return the list of all products.
        return self.products

    def get_expiring_soon(self, days=5):
        # Return products that are perishable and expiring within 'days'.
        today = date.today()
        soon = today + timedelta(days=days)
        return [p for p in self.products if p.is_perishable() and p.expiry_date <= soon and p.expiry_date >= today] 