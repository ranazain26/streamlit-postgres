from datetime import date
import pandas as pd


def to_df(rows):
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)
