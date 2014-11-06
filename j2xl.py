import openpyxl
import json
import uuid

class j2xl:
    def __init__(self, jsonString, output_directory):
        self.output_directory = output_directory
        self.data = json.loads(jsonString)
        self._filename = 'autoTest' + str(uuid.uuid4()) + '.xlsx'
        self.wb = openpyxl.Workbook()
        self.save()

    def getFilename(self):
        return self._filename

    def save(self):
        self.wb.save(self.output_directory + '/' + self._filename)