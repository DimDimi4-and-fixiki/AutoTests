import os.path

import pandas as pd
import pytest
from loguru import logger
from typing import AnyStr
from utilities.reading_tools import get_root
import sys
from utilities.reading_tools import get_root, read_file

# Read DataFrame for testing
root = get_root()
initial_file = os.path.join(root, 'files/Business Sales Transaction Test.csv')
logger.opt(colors=True).info(f'Reading initial DataFrom from <green>{initial_file}</green>')
initial_df = pd.read_csv(initial_file)

# DataFrame with dummy values for testing
dummy_data = {
    'first_column': ['Dog', 'Dolphin', 'Horse'],
    'second_column': ['Dima', 'Nick', 'Jack']
}
dummy_df = pd.DataFrame(data=dummy_data)


def compare_data_frames(df1: pd.DataFrame, df2: pd.DataFrame) -> bool:
    """
    Checks if DataFrames are made out of the same values (df1 == df2)
    :param df1: First DataFrame
    :param df2: Second DataFrame
    :return: True if DataFrames have the same values, and False if not
    """
    try:
        diff_df = df1.compare(df2)
        return diff_df.empty

    # Handler for compare() error
    except ValueError:
        return False


@pytest.mark.parametrize("input_path, test_df, result", [

    # Tests for checking that DataFrame was read correctly
    ('files/Business Sales Transaction Test.hd5', initial_df, True),
    ('files/Business Sales Transaction Test.parquet', initial_df, True),
    ('files/Business Sales Transaction Test.csv', initial_df, True),

    # Tests for checking that read function result is different from dummy DataFrame
    ('files/Business Sales Transaction Test.hd5', dummy_df, False),
    ('files/Business Sales Transaction Test.parquet', dummy_df, False),
    ('files/Business Sales Transaction Test.csv', dummy_df, False),
])
def test_file_reading(input_path, test_df, result):
    try:
        # Tries to read DataFrame with read_file()
        df = read_file(input_path)

        # Compare DataFrame from read_file() with test_df and assert result
        df_to_test = test_df.copy(deep=True)
        comp_result = compare_data_frames(df, df_to_test)
        del df_to_test
        assert comp_result == result

    # Log an Exception
    except Exception as e:
        logger.error(f'Exception occurred while reading file: {str(e)}')
        assert False



