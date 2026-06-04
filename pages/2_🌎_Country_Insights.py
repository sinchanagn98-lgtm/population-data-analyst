import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌎 Country Insights")

df = pd.read_csv(
    "dataset/world_population.csv"
)

country = st.selectbox(
    "Select Country",
    df["Country"].unique()
)

country_df = df[
    df["Country"] == country
]

years = [
    1970,1980,1990,
    2000,2010,2015,
    2020,2022
]

population = [

    country_df["1970 Population"].values[0],
    country_df["1980 Population"].values[0],
    country_df["1990 Population"].values[0],
    country_df["2000 Population"].values[0],
    country_df["2010 Population"].values[0],
    country_df["2015 Population"].values[0],
    country_df["2020 Population"].values[0],
    country_df["2022 Population"].values[0]
]

chart_df = pd.DataFrame({
    "Year": years,
    "Population": population
})

fig = px.line(
    chart_df,
    x="Year",
    y="Population",
    markers=True,
    template="plotly_dark",
    title=f"{country} Population Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
