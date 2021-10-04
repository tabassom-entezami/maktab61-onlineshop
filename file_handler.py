import csv
from csv import DictWriter


class FileHandler:
    def __init__(self, file_path='data.csv'):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as myfile:
            reader = csv.DictReader(myfile)
            return list(reader)

    def add_to_file(self, new_value):
        if isinstance(new_value, dict):
            fields = new_value.keys()
            new_value = [new_value]
        elif isinstance(new_value, list):
            fields = new_value[0].keys()

        with open(self.file_path, 'a') as myfile:

            writer = DictWriter(myfile, fieldnames=fields)
            if myfile.tell() == 0:
                writer.writeheader()
            writer.writerows(new_value)




    def unblock_an_user(self, seller,value):
        inputs = []
        with open(self.file_path, 'r+') as myfile:
            reader = csv.DictReader(myfile)
            inputs.append(list(reader))
        for i in range(len(inputs)):
            if inputs[i]["seller"] == seller and inputs[i]["blocked"] == value:
                inputs.remove(inputs[i])
        with open(self.file_path, "w") as myfile:
            for i in range(len(inputs)):
                writer = DictWriter(myfile)
                writer.writerows({inputs[i]})
