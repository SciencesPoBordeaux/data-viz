import altair as alt
import geopandas as gpd
from src.polk_gap import main as gap


df_gap = gap()

# Dynamic view in browser... Oui j'utilise encore et encore vim...
alt.renderers.enable("browser")

# Load Datasets (No ANES ATM)
# TODO include some useful ANES 2024 variable 

# Update title, reading example accordingly
data_hex_url = (
    "https://raw.githubusercontent.com/holtzy/"
    "R-graph-gallery/refs/heads/master/DATA/us_states_hexgrid.geojson.json"
)

gdf = gpd.read_file(data_hex_url)
gdf = gdf.rename(columns={"iso3166_2": "state"})

# Compute centroids for labels
gdf['centroid_lon'] = gdf.geometry.centroid.x
gdf['centroid_lat'] = gdf.geometry.centroid.y

# Merge Gap Variable
gdf = gdf.merge(df_gap, on='state', how='left')

gdf['gender_gap'] = gdf['gender_gap'] *-1


gdf['label'] = gdf['state'] + "\n" + (gdf['gender_gap'] * 100).round(1).astype(str) + "%"

# Chart Prep

tmp_val = max([abs(gdf['gender_gap'].min()), abs(gdf['gender_gap'].max())])
domain_range = [-tmp_val, tmp_val]

## Hexes Layer
hexes = (
    alt.Chart(gdf)
    .mark_geoshape(stroke="white", strokeWidth=3) 
    .encode(
        color=alt.Color(
            "gender_gap",
            type="quantitative",
            scale=alt.Scale(
                scheme="redgrey", 
                domainMid=0, 
                domain=domain_range
            ),
            legend=alt.Legend(
                title=["Écart de connaissance en faveur des femmes"], 
                titleLimit=500,
                orient='none',
                legendX=250*2, legendY=50*2,
                direction='horizontal',
                titleAnchor='middle',
                titleFontSize=10*2,
                labelFontSize=8*2,
                tickCount=5,
                gradientLength=250*2,
            )
        ),
        tooltip=["state", alt.Tooltip("gender_gap", type="quantitative", format=".1%"), "count"]
    )
)

## Labels Layer
hex_labels = (
    alt.Chart(gdf)
    .mark_text(
        fontSize=16*2, 
        fontWeight="bold", 
        color="black", 
        align="center", 
        baseline="middle"
    )
    .encode(
        longitude="centroid_lon",
        latitude="centroid_lat",
        text="state"
    )
)

subtitle = [
    "Au Massachusetts, en 2024, l'écart de connaissance politique entre les hommes et les femmes",
    "est de -18,7 points de pourcentage. Les valeurs négatives indiquent un biais en faveur des hommes."
]

## Text and stuff...
chart_title = alt.TitleParams(
    "Inégalités de connaissance politique selon le genre en 2024",
    subtitle=subtitle,
    fontSize=20*2,
    subtitleFontSize=13*2,
    anchor="start",
    fontWeight="bold"
)

source_text = alt.Chart().mark_text(
    align='right',
    baseline='bottom',
    fontSize=12*2,
    color='gray'
).encode(
    text=alt.value("Source: 2024 American National Election Study"),
    x=alt.value(800*2 - 10*2),
    y=alt.value(525*2 - 10*2),
)

hexmap = (hexes + hex_labels + source_text).project(
    type="mercator"
).properties(
    width=800*2,
    height=500*2,
    title=chart_title
).configure_view(stroke=None)

hexmap

hexmap.save('figures/visualization.svg')

