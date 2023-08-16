import time
import pandas as pd

from files import files


results = []


def get_csv_info(file_path):
    """

    Get csv info

    Args:
        file_path (str): file path of csv
    """

    result = {}

    import pandas as pd

    df = pd.read_csv(file_path)

    shape = df.shape

    result["rows"] = shape[0]
    result["columns"] = shape[1]

    return result


def get_file_size(file_path):
    """

    Get file info

    Args:
        file_path (str): file path of csv
    """

    result = {}

    import os

    file_stat = os.stat(file_path)

    result["file_size"] = file_stat.st_size

    return result


def test_with_pandas(file_path, filter_cols, filter_row_query):
    """
    Analysis of pandas csv loaders
    Args:
        file_path (str): file path of csv
        filter_cols ([str]): list of cols to be filtered
        filter_row_query (str): query for rows to be filtered
    """

    result = {}

    start = time.time()
    import pandas as pd

    result["pandas_import"] = time.time() - start

    df = pd.read_csv(file_path)

    result["pandas_read"] = time.time() - start

    result["pandas_display"] = time.time() - start

    df.filter(filter_cols)

    result["pandas_filter_cols"] = time.time() - start

    df.query(filter_row_query)

    result["pandas_filter_rows"] = time.time() - start

    return result


def test_with_duck_db(file_path, filter_cols, filter_row_query):
    """
    Analysis for duckdb loaders

    Args:
        file_path (str): file path of csv
        filter_cols ([str]): list of cols to be filtered
    """

    result = {}

    start = time.time()
    import duckdb

    result["duckdb_import"] = time.time() - start

    duckdb.read_csv(file_path).create("duck_db_conn")

    result["duckdb_read"] = time.time() - start

    duckdb.sql("SELECT * FROM duck_db_conn")

    result["duckdb_display"] = time.time() - start

    filter_col_str = ""

    for col in filter_cols:
        filter_col_str += f"'{col}', "

    filter_col_str = filter_col_str[:-1]

    duckdb.sql(f"SELECT {filter_col_str} FROM duck_db_conn")

    result["duckdb_filter_cols"] = time.time() - start

    duckdb.sql(f"SELECT * FROM duck_db_conn WHERE {filter_row_query}")

    result["duckdb_filter_rows"] = time.time() - start

    return result


for file in files:
    file_path = file.get("file_path")
    cols = file.get("cols")
    pandas_row_filter = file.get("pandas_row_filter")
    duck_db_row_filter = file.get("duck_db_row_filter")

    result = {}

    result.update(get_csv_info(file_path))
    result.update(get_file_size(file_path))

    result.update(
        test_with_pandas(
            file_path,
            cols,
            pandas_row_filter,
        )
    )

    result.update(test_with_duck_db(file_path, cols, duck_db_row_filter))

    results.append(result)


df = pd.DataFrame(data=results)


df.to_excel(f"results/analysis_output_{time.time()}.xlsx", index=False)
