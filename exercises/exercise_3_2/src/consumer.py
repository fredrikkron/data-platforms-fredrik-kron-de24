from quixstreams import Application
import json

app = Application(
    broker_address="localhost:9092",
    consumer_group="show-orders",
    auto_offset_reset="earliest",
)

orders_topic = app.topic(name="orders", value_deserializer="json")

sdf = app.dataframe(topic=orders_topic)

sdf = sdf.update(lambda message: print(f"Input: {message}"))


if __name__ == '__main__':
    app.run()
