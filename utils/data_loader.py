import pandas as pd

def load_data():

    df = pd.read_csv(
        "dataset/world_population.csv"
    )

    return df
