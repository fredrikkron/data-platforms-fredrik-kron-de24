import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys
import pkg_resources as pkg

for package in pkg.working_set:
    print(f"{package.key}=={package.version}")

print(sys.version)

data_path = Path(__file__).parent

data = pd.read_csv(data_path / "athlete_events.csv").tail(10)

fig,ax = plt.subplots(1)

print(data)

ax.bar(x = data["Sex"], height = data["Age"])
fig.savefig(data_path / "plotting.png")



