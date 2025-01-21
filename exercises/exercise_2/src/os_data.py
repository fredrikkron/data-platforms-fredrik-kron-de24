import pandas as pd
import matplotlib as plt
import seaborn as sns
from pathlib import Path
import sys
import pkg_resources as pkg

for package in pkg.working_set:
    print(f"{package.key}=={package.version}")

print(sys.version)

data_path = Path(__file__).parent

data = pd.read_csv(data_path / "athlete_events.csv").head()

print(data)

plot = sns.barplot(data,x="Sex",y="Age")
fig = plot.get_figure()
fig.savefig(data_path/"barplot.png")
