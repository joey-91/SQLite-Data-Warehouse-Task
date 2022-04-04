import pandas as pd

def new_values(input_df: pd.DataFrame, lookup: pd.DataFrame, key: str, keep_columns: list):
    """
    creates a dataframe of new values that weren't in the existing lookup table
    """
    unique_values = lookup[key].unique()
    new_values = input_df[~input_df[key].isin(unique_values)]
    new_values_df = new_values[keep_columns]
    new_values_df_dd = new_values_df.drop_duplicates(keep='first')
    return new_values_df_dd