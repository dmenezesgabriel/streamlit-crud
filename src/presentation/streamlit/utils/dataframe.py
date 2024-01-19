import pandas as pd


def get_dataframe_rows_added(old_df: pd.DataFrame, new_df: pd.DataFrame):
    _old_df = old_df.reset_index(drop=True)
    _new_df = new_df.reset_index(drop=True)

    # Identify rows in new_df that are not present in old_df
    return _new_df[~_new_df["ID"].isin(_old_df["ID"])].dropna()


def get_dataframe_rows_deleted(old_df: pd.DataFrame, new_df: pd.DataFrame):
    _old_df = old_df.reset_index(drop=True)
    _new_df = new_df.reset_index(drop=True)

    # Identify rows in old_df that are not present in new_df
    return _old_df[~_old_df["ID"].isin(_new_df["ID"])].dropna()


def get_dataframe_rows_cells_updated(
    old_df: pd.DataFrame, new_df: pd.DataFrame
):
    _old_df = old_df.reset_index(drop=True)
    _new_df = new_df.reset_index(drop=True)

    # Identify rows where any cell has changed
    return _old_df[(_old_df != _new_df).any(axis=1)]
