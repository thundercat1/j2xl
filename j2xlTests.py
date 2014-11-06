from j2xl import *
import unittest
import openpyxl
import random
import os


class Testj2xl(unittest.TestCase):


    def setUp(self):
        self.testFileDirectory = './TestFiles'

        example_json_array_string = '[{"Name": "Michael", "Age": 30}, {"Name": "Allison", "Age": 29}]'
        self.j2xl_with_array_string = j2xl(example_json_array_string, self.testFileDirectory)

    def test_j2xl_generates_xlsx_filename(self):
        fname = self.j2xl_with_array_string.getFilename()
        fname_extension = fname.split('.')[1]
        self.assertEqual(fname_extension, 'xlsx', 'Filename should be created with xlsx extension.')

    def test_reading_example_xlsx_works(self):
        wb = openpyxl.load_workbook(self.testFileDirectory + '/ClimbingRoutes.xlsx')
        self.assertEqual(wb['Sheet1']['A4'].value, 'Schoolroom')

    def test_j2xl_creates_file_in_test_directory(self):
        fname = self.j2xl_with_array_string.getFilename()
        self.assertTrue(fname in os.listdir(self.testFileDirectory), 'j2xl did not return a filename that was actually '
                                                                     'in the test directory')



if __name__ == '__main__':
    unittest.main()