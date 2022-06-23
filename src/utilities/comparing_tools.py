import pandas as pd
from loguru import logger


def compare_data_frames(df1: pd.DataFrame, df2: pd.DataFrame) -> bool:
    """
    Checks if DataFrames are made out of the same values (df1 == df2)
    :param df1: First DataFrame
    :param df2: Second DataFrame
    :return: True if DataFrames have the same values, and False if not
    """

    # If first DataFrame is None
    if df1 is None and not (df2 is None):
        logger.info('First DataFrame is None and second is not None')
        return False

    # If second DataFrame is None
    elif df2 is None and not (df1 is None):
        logger.info('Second DataFrame is None and first is not None')
        return False

    # If both DataFrames are None
    elif df1 is None and df2 is None:
        logger.info('Both DataFrames are None')
        return True

    # Tries to get difference between DataFrames
    try:
        diff_df = df1.compare(df2)
        return diff_df.empty

    # Handler for pandas.compare() error
    except ValueError:
        return False
