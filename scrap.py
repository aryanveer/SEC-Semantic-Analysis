import os
from settings import *
import csv
import pandas as pd
from urllib.request import urlretrieve
import errno


def create_directories(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def get_download_path(path):
    path_list = [RAW_DATA_PATH] + path.split("/")
    return os.path.join(*path_list)


def main():
    file_path = os.path.join(DATA_DIR, IMPORT_FILE_NAME)
    cik_list = pd.read_excel(file_path, sheet_name=SHEET_NAME)

    for index, row in cik_list.iterrows():
        download_url = DATA_DOWNLOAD_URL + row["SECFNAME"]
        download_path = get_download_path(row["SECFNAME"])
        create_directories(download_path)
        urlretrieve(download_url, download_path)
        print("Download Complete: " + row["SECFNAME"])


if __name__ == "__main__":
    main()