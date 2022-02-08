#%%
# Download data from libreview and run this code.

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime

import plotly.express as px
#%%

def parse_ts(x):
    ts = datetime.datetime.strptime(x, '%d-%m-%Y %H:%M')
    return pd.to_datetime(ts)

data = pd.read_csv("data/KasiaBoroszko_glucose_8-2-2022.csv", skiprows=1)

print(data.columns)

data['timestamp'] = data['Znacznik czasu w urządzeniu'].apply(parse_ts)
data['sugar'] = data['Historyczne stężenia glukozy mg/dL'].mean()
#%%
data.loc[data['Rodzaj zapisu'] == 0, 'sugar'] = data['Historyczne stężenia ' \
                                                  'glukozy mg/dL']
data.loc[data['Rodzaj zapisu'] == 1, 'sugar'] = data['Stężenie glukozy na ' \
                                                  'podstawie ' \
                                         'skanowania mg/dL']

data = data.sort_values('timestamp').reset_index()
#%%

cukier_kasi = data[['timestamp', 'sugar']].query('timestamp > "2022-01-01"')

#%%
plt.figure()
plt.plot(cukier_kasi.timestamp, cukier_kasi.sugar)
plt.show()
#%%
def posilki_ts(x):
    ts = datetime.datetime.strptime(x, '%d.%m.%Y %H:%M')
    return pd.to_datetime(ts)

food = pd.read_csv("data/posilki.csv")
food['timestamp'] = food['timestamp'].apply(posilki_ts)

#%%
START = datetime.datetime.strptime("2022-01-18", "%Y-%m-%d")
END = datetime.datetime.strptime("2022-02-01", "%Y-%m-%d")

# for each day
# get data for that day
# plot line and food
#%%
fig = px.line(cukier_kasi, x="timestamp", y="sugar")

# Add shape regions
fig.add_hrect(
    y0=70, y1=140,
    fillcolor="rgb(207, 228, 203)", opacity=0.5,
    layer="below", line_width=0,
),

fig.show()

