from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="text-splitter",
    auto_offset_reset="earliest",
)

jokes_topic = app.topic(name="jokes", value_deserializer="json")

sdf = app.dataframe(topic=jokes_topic)

# def print_message(message):
    # print(f"Input: {message})            different ways of writing
# sdf.update(print_message)
sdf = sdf.update(lambda message: print(f"Input: {message}"))

# transformations
# split the words

# def split_words(message):
#     return [word for word in message["joke_text"].split()]

# sdf = sdf.apply(split_words, expand=True)
# sdf.update(lambda words: print(f"Output: {words})) 

sdf = sdf.apply(
    lambda message: [{"word": word} for word in message["joke_text"].split()],
    expand=True,
)

sdf["length"] = sdf["word"].apply(lambda word: len(word))

sdf = sdf.update(lambda row: print(f"Output: {row}"))

if __name__ == "__main__":
    app.run()