import pandas as pd
from pathlib import Path

data_path = Path(__file__).parent / "data"

df = pd.read_json(data_path / "orders.json")
# product, quantity, price and total price
# Function to print order details
def print_order_details(order):
    print(f"Order ID: {order['order_id']}")
    total_price = 0
    for product in order['products']:
        product_name = product['name']
        quantity = product['quantity']
        price = product['price']
        total = quantity * price
        total_price += total
        print(f"Product: {product_name:<20} Quantity: {quantity:<5} Price: {price:<10.2f}")
    print(f"Total price: {total_price:.2f}\n")

# Iterate through orders and print details
df.apply(print_order_details, axis=1)
