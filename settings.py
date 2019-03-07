import os

BASE_DIR = os.path.dirname(__file__)

DATA_DIR = os.path.join(BASE_DIR, "data")

IMPORT_FILE_NAME = "cik_list.xlsx"

SHEET_NAME = "cik_list_ajay"

RAW_DATA_PATH = os.path.join(DATA_DIR, "raw_data")

DATA_DOWNLOAD_URL = "https://www.sec.gov/Archives/"

OUTPUT_FILE = "output.xlsx"
