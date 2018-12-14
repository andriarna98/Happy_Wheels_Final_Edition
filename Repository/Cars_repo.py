#Models
from Models.Car import Car
#Csv
import csv

class Cars_repo:
    def __init__self(self):
        pass

    def add_car(self, plate_num, brand, size, location):
        with open("./data/Cars.csv", "a+") as Cars_file:
            Cars_file.write("\n{},{},{},{}".format(plate_num, brand, size, location))

    def get_cars(self):
        self.car_dict = {}
        with open("./data/Cars.csv", "r") as Cars_file:
            csv_reader = csv.reader(Cars_file)
            next(csv_reader)
            
            for line in csv_reader:
                plate_num, brand, size, location = line
                new_car = Car(plate_num, brand, size, location)
                key = new_car.get_plate_number() # platenumber is the key
            
                self.car_dict[key] = new_car

        return self.car_dict

