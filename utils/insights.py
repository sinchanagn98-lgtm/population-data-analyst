def generate_insights(df):

    highest = df.loc[
        df["Growth Rate"].idxmax()
    ]

    lowest = df.loc[
        df["Growth Rate"].idxmin()
    ]

    insights = {

        "highest_growth":
        highest["Country"],

        "lowest_growth":
        lowest["Country"],

        "avg_growth":
        round(df["Growth Rate"].mean(),2)
    }

    return insights
