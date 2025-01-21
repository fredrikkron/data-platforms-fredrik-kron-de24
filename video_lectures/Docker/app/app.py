import pandas as pd
import sys

print("\n\n")
print(f"{sys.version}")

data = {
    "name": ["Erik", "Anna", "Johan", "Lisa", "Oskar"],
    "age": [28, 34, 40, 25, 50],
    "city": ["Stockholm", "Göteborg", "Malmö", "Uppsala", "Lund"],
    "salary_sek": [45000, 32000, 20000, 25000, 30000]
}

df = pd.DataFrame(data)

print(df)