from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="show-orders",
    auto_offset_reset="earliest",
)

orders_topic = app.topic(name="orders", value_deserializer="json")

sdf = app.dataframe(topic=orders_topic)

sdf = sdf.update(lambda message: print(f"Input: {message}"))


# create an output on the keys and values

app.run(sdf)