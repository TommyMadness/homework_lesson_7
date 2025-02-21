import shutil
import zipfile, os

import pytest

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
PROJECT_PATH = os.path.abspath(os.path.join(CURRENT_DIR, ".."))

RESOURCES_DIR = os.path.join(PROJECT_PATH, "resources")
TMP_DIR = os.path.join(PROJECT_PATH, "tmp")
ZIP_PATH = os.path.join(RESOURCES_DIR, "test_files.zip")

@pytest.fixture
def pack_files_to_zip():
    if not os.path.isdir(RESOURCES_DIR):
        os.makedirs(RESOURCES_DIR, exist_ok=True)
        print(f"Directory '{RESOURCES_DIR}' has been created.")

    if os.path.isfile(ZIP_PATH):
        print(f"File '{ZIP_PATH}' already exists")
    else:
        with zipfile.ZipFile(ZIP_PATH, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
            zf.write(os.path.join(TMP_DIR, 'currency.csv'), arcname='currency.csv')
            zf.write(os.path.join(TMP_DIR, 'file_example_XLSX_1000.xlsx'), arcname='file_example_XLSX_1000.xlsx')
            zf.write(os.path.join(TMP_DIR, 'sample.pdf'), arcname='sample.pdf')
        print(f"Files were added to '{ZIP_PATH}'.")

    yield

    if os.path.isdir(RESOURCES_DIR):
        shutil.rmtree(RESOURCES_DIR)
        print(f"Directory '{RESOURCES_DIR}' and its contents have been removed.")