from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

data_path = Path(__file__).parents[1] / "data"

with open(data_path / "orders.json", "r") as file:
    orders = json.load(file)

app = Application(broker_address="localhost:9092", consumer_group="show-orders")

orders_topic = app.topic(name="orders", value_serializer="json")

def main():
    with app.get_producer() as producer:
        for order in orders:
            kafka_msg = orders_topic.serialize(key=order["order_id"], value=order['products'])
            print(f"Order number: {kafka_msg.key} \nProducts: {kafka_msg.value}")
            print()

            producer.produce(topic="orders", key=kafka_msg.key, value=kafka_msg.value)

if __name__ == "__main__":
    main()