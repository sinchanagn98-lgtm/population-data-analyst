import streamlit as st
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

st.title("📈 Population Predictions")

df = pd.read_csv(
    "dataset/world_population.csv"
)

country = st.selectbox(
    "Choose Country",
    df["Country"].unique()
)

country_df = df[
    df["Country"] == country
]

years = np.array([
    1970,1980,1990,
    2000,2010,2015,
    2020,2022
]).reshape(-1,1)

population = np.array([

    country_df["1970 Population"].values[0],
    country_df["1980 Population"].values[0],
    country_df["1990 Population"].values[0],
    country_df["2000 Population"].values[0],
    country_df["2010 Population"].values[0],
    country_df["2015 Population"].values[0],
    country_df["2020 Population"].values[0],
    country_df["2022 Population"].values[0]
])

# Train Model
model = LinearRegression()

model.fit(
    years,
    population
)

# Future Prediction
future_years = np.array([
    2030,
    2040,
    2050
]).reshape(-1,1)

predictions = model.predict(
    future_years
)

# Display Predictions
st.subheader("🔮 Future Predictions")

for year, pred in zip(
    [2030,2040,2050],
    predictions
):
    st.success(
        f"{year}: {int(pred):,}"
    )

# Plot
fig, ax = plt.subplots(
    figsize=(10,5)
)

ax.plot(
    years.flatten(),
    population,
    marker='o'
)

ax.plot(
    future_years.flatten(),
    predictions,
    marker='o'
)

ax.set_xlabel("Year")
ax.set_ylabel("Population")
ax.set_title("Population Forecast")

st.pyplot(fig)
