#Models
from Models.Salesman import Salesman
#Csv
import csv

class Salesman_repo:
    def __init__(self):
        pass

    def update_data(self, sales_dict):
        with open("./data/Salesman.csv", "+w") as Salesman_file:
            Salesman_file.write("name,email,ID,pw")
            for ID, values in sales_dict.items():
                name = values.get_name()
                email = values.get_email()
                pw = values.get_password()
                Salesman_file.write("\n{},{},{},{}".format(name,email,ID,pw))

    def get_salesmen(self):
        with open("./data/Salesman.csv", "r") as Salesman_file:
            csv_reader = csv.reader(Salesman_file)
            next(csv_reader)
            self.salesman_dict = {}
            for line in csv_reader:
                name, email, ID, pw = line
                new_salesman = Salesman(name, email, ID, pw)
                key = new_salesman.get_ID() 
            
                self.salesman_dict[key] = new_salesman

        return self.salesman_dict


