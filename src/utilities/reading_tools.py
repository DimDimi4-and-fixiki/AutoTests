import sys
from pathlib import Path

import pandas as pd
from loguru import logger

logger.add(sys.stderr, format="{time} {level} {module} {message}", level="INFO")


def get_root():
    current_path = str(Path.cwd()).replace("\\", "/")

    # Gets root path to the directory of the project
    return '/'.join(current_path.split('/')) + '/../'


@logger.catch
def read_file(
    file_name, root=get_root(), encoding='cp1251', usecols=None, dtype=None, sep=',',
    sheetname=0, skiprows=None, nrows=None, header=0, names=None, index_col=None, quotechar='\"',
    df_name='df', verbose=False,
) -> pd.DataFrame:
    if file_name.endswith(".csv") | file_name.endswith(".zip"):
        df = pd.read_csv(
            root + file_name, encoding=encoding, dtype=dtype, sep=sep, names=names,
            usecols=usecols, error_bad_lines=False, nrows=nrows, index_col=index_col, quotechar=quotechar,
        )
        if verbose:
            logger.debug('Loaded ' + file_name)
        return df
    elif file_name.endswith(".txt"):
        df = pd.read_csv(
            root + file_name, encoding=encoding, dtype=dtype, sep=sep, header=header,
            usecols=usecols, error_bad_lines=False, nrows=nrows,
        )
        if verbose:
            logger.debug('Loaded ' + file_name)
        return df
    elif file_name.endswith(".xlsx") | file_name.endswith(".xls"):
        df = pd.read_excel(
            root + file_name, dtype=dtype, header=header, nrows=nrows, index_col=index_col,
            sheet_name=sheetname, skiprows=skiprows, engine='openpyxl',
        )
        if names is not None:
            df.dropna(how='all', axis=1, inplace=True)
            df.columns = names
        if usecols is not None:
            df = df[usecols]
        if verbose:
            logger.debug('Loaded ' + file_name)
        return df
    elif file_name.endswith('.hd5'):
        if verbose:
            logger.debug('Loaded ' + file_name)
        return pd.read_hdf(root + file_name, key=df_name)
    elif file_name.endswith('.f'):
        if verbose:
            logger.debug('Loaded ' + file_name)
        return pd.read_feather(root + file_name)

    elif file_name.endswith('.parquet'):
        if verbose:
            logger.debug('Loaded ' + file_name)
        return pd.read_parquet(root + file_name)

    else:
        file_name = file_name + '.csv'
        df = pd.read_csv(
            root + file_name, encoding=encoding, dtype=dtype, sep=sep,
            usecols=usecols, error_bad_lines=False, nrows=nrows, index_col=index_col, quotechar=quotechar,
        )
        if verbose:
            logger.debug('Loaded ' + file_name)
        return df
