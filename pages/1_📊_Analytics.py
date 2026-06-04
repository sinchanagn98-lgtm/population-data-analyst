import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Advanced Analytics")

df = pd.read_csv(
    "dataset/world_population.csv"
)

# Scatter Chart
fig = px.scatter(
    df,
    x="Growth Rate",
    y="2022 Population",
    size="Area (km²)",
    color="Continent",
    hover_name="Country",
    template="plotly_dark",
    title="Growth Rate vs Population"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Histogram
fig2 = px.histogram(
    df,
    x="Density (per km²)",
    color="Continent",
    nbins=50,
    template="plotly_dark",
    title="Population Density Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
