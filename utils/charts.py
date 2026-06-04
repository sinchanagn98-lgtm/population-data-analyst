import plotly.express as px

def top_population_chart(df):

    top10 = df.sort_values(
        by="2022 Population",
        ascending=False
    ).head(10)

    fig = px.bar(
        top10,
        x="Country",
        y="2022 Population",
        color="2022 Population",
        template="plotly_dark"
    )

    return fig


def continent_chart(df):

    continent = df.groupby(
        "Continent"
    )["2022 Population"].sum().reset_index()

    fig = px.pie(
        continent,
        names="Continent",
        values="2022 Population",
        hole=0.4
    )

    return fig
