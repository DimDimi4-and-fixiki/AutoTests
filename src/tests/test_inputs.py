import os.path

import pandas as pd
from loguru import logger

from src.utilities.reading_tools import get_root

root = get_root()

# Read initial DataFrame from CSV
initial_file = os.path.join(root, 'files/Business Sales Transaction Test.csv')
logger.opt(colors=True).info(f'Reading initial DataFrom from <green>{initial_file}</green>')
initial_df = pd.read_csv(initial_file)


def log_comparing_error(file_extension: str):
    # Method for quick logging if DataFrame.compare() raised an Exception
    logger.error(f'Error while comparing initial DataFrame with DataFrame from {file_extension} file')


def test_hdf_input():
    file_extension = 'HDF'
    file_path = os.path.join(root, 'files/Business Sales Transaction Test.hd5')

    hdf_df: pd.DataFrame = pd.read_hdf(file_path, key='df')
    try:
        diff_df = hdf_df.compare(initial_df)
    except ValueError:
        log_comparing_error(file_extension)
        assert False

    assert diff_df.empty


def test_parquet_input():
    file_extension = 'Parquet'
    file_path = os.path.join(root, 'files/Business Sales Transaction Test.parquet')

    parquet_df: pd.DataFrame = pd.read_parquet(file_path)
    try:
        diff_df = parquet_df.compare(initial_df)
    except ValueError:
        log_comparing_error(file_extension)
        assert False

    assert diff_df.empty
