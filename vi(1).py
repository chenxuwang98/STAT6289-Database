import pandas as pd
import json
import plotly.express as px
import plotly
from area import area

df = pd.read_csv("Testing.csv")
nycmap = json.load(open("./new-york-counties.geojson"))


#mapping
d = {}
county_data = nycmap['features']
for n in county_data:
    name = n['properties']['name']
    a = area(n['geometry'])
    d[name] = a

    # print(d)

df["area"] = df['county'].map(d)
df = df.dropna(subset=["area"])


fig = px.choropleth_mapbox(df, geojson=nycmap, locations='county',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           color="prob_positive",
                           featureidkey="properties.name",
                           mapbox_style="carto-positron",
                           zoom=5,center={"lat": 40.7, "lon": -73.9},
                           opacity=0.5,
                           hover_name= "county",
                           hover_data= ["total_tests", "new_positives" ,"positives_count"],
                        #    labels={"prob_positive": "prob_positive", "first_dose": "First dose"}
                                                     )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
plotly.offline.plot(fig, filename='file1.html')
fig.show()