import pandas as pd
from pathlib import Path

data_path = Path(__file__).parent / "data"

df = pd.read_json(data_path / "orders.json")

print(f"Input: {df}")

# Do a for-loop to iterate through each order

# Input: {'order_id': 'ORD-1009', 'customer': 'George Clark', 'products': [{'name': 'Smartwatch', 'price': 199.99, 'quantity': 1}, {'name': 'USB-C Cable', 'price': 14.99, 'quantity': 2}, {'name': 'Iphone 15', 'price': 600.99, 'quantity': 1}], 'order_date': '2024-01-17', 'status': 'Processing'}
# Product: Smartwatch           Quantity: 1                    Price: 199.99              
# Product: USB-C Cable          Quantity: 2                    Price: 14.99               
# Product: Iphone 15            Quantity: 1                    Price: 600.99              
# Total price: 830.96