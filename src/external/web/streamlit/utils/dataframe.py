from typing import Any

import pandas as pd


def get_dataframe_rows_added(
    old_df: pd.DataFrame, new_df: pd.DataFrame, index: Any
) -> pd.DataFrame:
    _old_df = old_df.set_index(index).sort_values(by=index)
    _new_df = new_df.set_index(index).sort_values(by=index)

    # Identify rows in new_df that are not present in old_df
    return _new_df[~_new_df.index.isin(_old_df.index)].dropna()


def get_dataframe_rows_removed(
    old_df: pd.DataFrame, new_df: pd.DataFrame, index: Any
) -> pd.DataFrame:
    _old_df = old_df.set_index(index).sort_values(by=index)
    _new_df = new_df.set_index(index).sort_values(by=index)

    # Identify rows in old_df that are not present in new_df
    return _old_df[~_old_df.index.isin(_new_df.index)].dropna()


def get_dataframe_rows_cells_updated(
    old_df: pd.DataFrame, new_df: pd.DataFrame, index: Any
) -> pd.DataFrame:
    # removed_rows = get_dataframe_rows_removed(old_df, new_df)
    # added_rows = get_dataframe_rows_added(old_df, new)

    _old_df = old_df.set_index(index).sort_values(by=index)
    _new_df = new_df.set_index(index).sort_values(by=index)
    _new_df = _new_df[_new_df.index.isin(_old_df.index)].dropna()
    _old_df = _old_df[_old_df.index.isin(_new_df.index)].dropna()

    # Identify rows where any cell has changed
    return _old_df[(_old_df != _new_df).any(axis=1)]
