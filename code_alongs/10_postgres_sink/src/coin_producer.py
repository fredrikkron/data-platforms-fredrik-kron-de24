import time
from quixstreams import Application
# from constants import COINMARKET_API
# from requests import Session, TooManyRedirects, Timeout
# import json
from connect_api import get_latest_coin_data


def main():
    app = Application(broker_address="localhost:9092", consumer_group="coin_group")
    coins_topic = app.topic(name="coins", value_serializer="json")

    with app.get_producer() as producer:
        while True:
            coin_latest = get_latest_coin_data("BTC")

            kafka_message = coins_topic.serialize(
                key=coin_latest["symbol"], value=coin_latest
            )

            print(
                f"produce event with key = {kafka_message.key}, price = {coin_latest['quote']['USD']['price']}"
            )

            producer.produce(
                topic=coins_topic.name, key=kafka_message.key, value=kafka_message.value
            )

            time.sleep(30)


if __name__ == "__main__":
    # result = get_latest_coin_data("BTC")
    # pprint(result)
    main()
