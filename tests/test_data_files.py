"""Check that the data files are existed, readable and nonempty.

To run these tests from the project root, run:

    python3 -m unittest --verbose tests.test_data_files
"""

import pathlib
import unittest
import os

DATA_ROOT = pathlib.Path(__file__).parent.parent / '_data/DogQuotes/'


class TestDataFiles(unittest.TestCase):
    def setUp(self):
        self.csv_file = DATA_ROOT / 'DogQuotesCSV.csv'
        self.docx_file = DATA_ROOT / 'DogQuotesDOCX.docx'
        self.pdf_file = DATA_ROOT / 'DogQuotesPDF.pdf'
        self.txt_file = DATA_ROOT / 'DogQuotesTXT.txt'

    def test_data_files_exist(self):
        self.assertTrue(self.csv_file.exists())
        self.assertTrue(self.docx_file.exists())
        self.assertTrue(self.pdf_file.exists())
        self.assertTrue(self.txt_file.exists())

    def test_data_files_are_readable(self):
        self.assertTrue(os.access(self.csv_file, os.R_OK))
        self.assertTrue(os.access(self.docx_file, os.R_OK))
        self.assertTrue(os.access(self.pdf_file, os.R_OK))
        self.assertTrue(os.access(self.txt_file, os.R_OK))

    def test_data_files_are_not_empty(self):
        try:
            self.assertTrue(self.csv_file.stat().st_size >
                            0, "Empty CSV file.")
            self.assertTrue(self.docx_file.stat().st_size >
                            0, "Empty DOCX file.")
            self.assertTrue(self.pdf_file.stat().st_size >
                            0, "Empty PDF file.")
            self.assertTrue(self.txt_file.stat().st_size >
                            0, "Empty TXT file.")
        except OSError:
            self.fail("Unexpected OSError.")


if __name__ == '__main__':
    unittest.main()
