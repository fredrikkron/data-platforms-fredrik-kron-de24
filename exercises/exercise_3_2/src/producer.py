from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

data_path = Path(__file__).parents[1] / "data"

print(data_path)

with open(data_path / "orders.json", "r") as file:
    orders = json.load(file)

# pprint(orders)
# print(type(orders))