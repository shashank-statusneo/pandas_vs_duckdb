files = [
    {
        "file_path": "sample_csv_files/homes.csv",
        "cols": ["Sell", "List", "Taxes"],
        "pandas_row_filter": "Sell >= 170",
        "duck_db_row_filter": "'Sell' >= 170",
    },
    {
        "file_path": "sample_csv_files/airtravel.csv",
        "cols": ["Month", "Year", "Day"],
        "pandas_row_filter": "Year >= 370",
        "duck_db_row_filter": "'Year' >= 370",
    },
    {
        "file_path": "sample_csv_files/hw_25000.csv",
        "cols": ["Height", "Weight"],
        "pandas_row_filter": "Height >= 65.05",
        "duck_db_row_filter": "'Height' >= 65.05",
    },
    # {
    #     "file_path": "sample_csv_files/organizations.csv",
    #     "cols": ["Founded", "Name"],
    #     "pandas_row_filter": "Founded >= 2000",
    #     "duck_db_row_filter": "'Founded' >= 2000",
    # },
    # {
    #     "file_path": "sample_csv_files/ip_data.csv",
    #     "cols": ["Protocol", "ProtocolName"],
    #     "pandas_row_filter": "ProtocolName == 'GOOGLE'",
    #     "duck_db_row_filter": "'ProtocolName' == 'GOOGLE'",
    # },
]
