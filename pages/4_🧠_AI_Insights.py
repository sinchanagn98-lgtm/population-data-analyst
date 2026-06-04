import streamlit as st
import pandas as pd

from utils.insights import (
    generate_insights
)

st.title("🧠 AI Insights")

df = pd.read_csv(
    "countries-continents-capitals.csv"
)

insights = generate_insights(df)

st.success(f"""

🚀 Highest Growth Country:
{insights['highest_growth']}

""")

st.error(f"""

📉 Lowest Growth Country:
{insights['lowest_growth']}

""")

st.info(f"""

📊 Average Growth Rate:
{insights['avg_growth']}

""")
