import os
import sys

import pandas as pd
from loguru import logger

from src.utilities.reading_tools import get_root

logger.remove()  # Remove the default setting

# Set up the preferred logging colors and format unless overridden by its environment variable
logger.level("INFO", color="<white>")
logger.level("DEBUG", color="<d><white>")
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)
logger.add(sys.stderr, format=log_format)


@logger.catch
def save_files_for_test():
    csv_file_path = os.path.join(get_root(), r'files\Business Sales Transaction.csv')

    # Read initial DataFrame
    df = pd.read_csv(csv_file_path)
    df.drop(columns=[df.columns[0], df.columns[2]], inplace=True)
    df.reset_index(drop=True, inplace=True)

    csv_file_path = os.path.join(get_root(), r'files\Business Sales Transaction Test.csv')
    df.to_csv(csv_file_path, index=False)

    parquet_file_path = os.path.join(get_root(), r'files\Business Sales Transaction Test.parquet')
    df.to_parquet(parquet_file_path)

    hd5_file_path = os.path.join(get_root(), r'files\Business Sales Transaction Test.hd5')
    df.to_hdf(hd5_file_path, key='df', encoding='utf8')


if __name__ == '__main__':
    save_files_for_test()
    logger.info('All files saved successfully')
