from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="show-orders",
    auto_offset_reset="earliest",
)

orders_topic = app.topic(name="orders", value_deserializer="json")

sdf = app.dataframe(topic=orders_topic)

sdf = sdf.update(lambda message: print(f"Input: {message}"))

# transform the message
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


sdf = sdf.apply(print_order_details, expand=True)

sdf.update(lambda order_details: print (f"Output: {order_details}"))


if __name__ == '__main__':
    app.run()