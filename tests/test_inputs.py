import os.path

import pandas as pd
import pytest
from loguru import logger
from typing import AnyStr
from utilities.reading_tools import get_root
import sys

root = get_root()

# Read initial DataFrame from CSV
initial_file = os.path.join(root, 'files/Business Sales Transaction Test.csv')
logger.opt(colors=True).info(f'Reading initial DataFrom from <green>{initial_file}</green>')
initial_df = pd.read_csv(initial_file)


def log_comparing_error(file_extension: AnyStr):
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
