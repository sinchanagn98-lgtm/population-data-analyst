import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="World Population Analytics",
    page_icon="🌍",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("dataset/world_population.csv")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right,#0f2027,#203a43,#2c5364);
}

h1,h2,h3,h4 {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    selected = option_menu(
        menu_title="Dashboard Menu",

        options=[
            "Home",
            "Analytics",
            "Country Insights",
            "Predictions",
            "AI Insights"
        ],

        icons=[
            "house",
            "bar-chart",
            "globe",
            "graph-up",
            "robot"
        ],

        default_index=0
    )

# ---------------- TITLE ----------------
st.title("🌍 World Population Analytics Dashboard")

st.markdown("""
### Deep Analytics and AI Insights
""")

# ---------------- KPI CARDS ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌎 Countries",
        len(df["Country"].unique())
    )

with col2:
    st.metric(
        "👥 Total Population",
        f"{df['2022 Population'].sum():,}"
    )

with col3:
    st.metric(
        "📈 Avg Growth",
        round(df["Growth Rate"].mean(), 2)
    )

with col4:
    st.metric(
        "🏆 Highest Population",
        df.loc[
            df["2022 Population"].idxmax(),
            "Country"
        ]
    )

st.markdown("---")

# ---------------- BAR CHART ----------------
col1, col2 = st.columns(2)

with col1:

    top10 = df.sort_values(
        by="2022 Population",
        ascending=False
    ).head(10)

    fig = px.bar(
        top10,
        x="Country",
        y="2022 Population",
        color="2022 Population",
        template="plotly_dark",
        title="Top 10 Most Populated Countries"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------- PIE CHART ----------------
with col2:

    continent = df.groupby(
        "Continent"
    )["2022 Population"].sum().reset_index()

    fig2 = px.pie(
        continent,
        names="Continent",
        values="2022 Population",
        hole=0.4,
        title="Population by Continent"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------- MAP ----------------
st.subheader("🗺 Global Population Map")

fig3 = px.scatter_geo(
    df,
    locations="CCA3",
    hover_name="Country",
    size="2022 Population",
    color="Continent",
    projection="natural earth",
    template="plotly_dark"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- TABLE ----------------
st.subheader("📋 Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)
