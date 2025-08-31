import streamlit as st
import pandas as pd
import plotly as plt
import plotly.express as px
import pydeck as pdk
import altair as alt
import folium
from datetime import datetime


# ----------------------------
# 1. Load & tidy data
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("public_emdat_custom_request.csv")
    df.columns = df.columns.str.strip().str.rstrip(":")
    df["Total Affected"] = pd.to_numeric(df["Total Affected"], errors="coerce").fillna(0)
    return df

df = load_data()

# ---------------------
# 2. Page config
# ----------------------------
st.set_page_config(page_title="Global Disasters From 2000 to 2025", layout="wide")
st.title("🌍 Global Disasters")
st.markdown("> *An interactive, creative look at global disasters around the world.*")

# ----------------------------
# 3. Sidebar filters
# ----------------------------
st.sidebar.header("🔍 Dynamic Filters")
region = st.sidebar.multiselect("Region", sorted(df["Region"].unique()), default=df["Region"].unique())
dis_type = st.sidebar.multiselect("Disaster Type", sorted(df["Disaster Type"].unique()), default=df["Disaster Type"].unique())
min_deaths = st.sidebar.slider("Min Deaths", 0, int(df["Total Deaths"].max()), 0)

filt = df[(df["Region"].isin(region)) & (df["Disaster Type"].isin(dis_type)) & (df["Total Deaths"] >= min_deaths)]

# ----------------------------
# 4. Animated KPIs
# ----------------------------
st.subheader("📍 Disasters by Country")
if not filt.empty:
    map_df = (filt.groupby(["ISO", "Country", "Latitude", "Longitude"])
                .agg(**{"Deaths": ("Total Deaths", "sum"),
                        "Affected": ("Total Affected", "sum")})
                .reset_index())
    
    chart = alt.Chart(map_df).mark_circle().encode(
        longitude='Longitude:Q',
        latitude='Latitude:Q',
        color=alt.Color('Deaths:Q', scale=alt.Scale(scheme='yellowgreenblue'), title='Deaths'),
        tooltip=['Country', 'Deaths', 'Affected']
    ).properties(
        width=800,
        height=500
    ).project(
        type='equirectangular'
    )
    
    st.altair_chart(chart, use_container_width=True)
# ----------------------------
# 6. Charts
# ----------------------------
st.subheader("📊 Insights")


fig = px.bar(filt.groupby("Disaster Type")["Total Deaths"].sum().reset_index(),
                 x="Disaster Type", y="Total Deaths",
                 title="Deaths by Disaster Type", text_auto=True)
st.plotly_chart(fig, use_container_width=True)


fig = px.scatter_geo(filt, locations="ISO",
                         color="Disaster Type",
                         size="Total Affected",
                         projection="natural earth",
                         title="Global footprint")
st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# 7. Download
# ----------------------------
csv_data = filt.to_csv(index=False)
st.download_button(label="⬇️ Download filtered data (CSV)",
                   data=csv_data,
                   file_name=f"emdat_filtered_{datetime.now():%Y%m%d}.csv",
                   mime="text/csv")