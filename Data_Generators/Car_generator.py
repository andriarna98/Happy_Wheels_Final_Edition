# Random car generator

import random
import os
from tqdm import tqdm

def generate_plate_number():
        # Plate num 2 bokst - 3 tolust
        LETTERS = "ABCDEFGHIJKLMNOPQRSTUVXZYW"
        NUMBERS = "1234567890"
        plate_number = ""
        for i in range(2):
                plate_number += LETTERS[random.randint(0,25)]  
        plate_number += "-"                   
        for i in range(3):
                plate_number += NUMBERS[random.randint(0,9)]
        
        return plate_number 

def add_new_car(new_car):
    try:
        with open("data/Cars.csv", "a+") as Cars_file:
                plate_number, car_size, brand, location = new_car.split(",")
                Cars_file.write("{},{},{},{}\n".format(plate_number, car_size, brand, location))
    except(PermissionError):
        print("Close file to make changes")
        input("Press enter to continue ")

def generate_car():
    plate_number = generate_plate_number()

    size = ["1", "2", "3"]  # Available sizes
    size_let = random.randint(0, 2) # Picks one of the sizes randomly

    if size_let == 0:       # Searches for brands in selected size
            brands = ["Yaris", "Aygo", "Golf"]
    elif size_let == 1:
            brands = ["Passat", "Legacy", "Corolla"]
    elif size_let == 2:
            brands = ["Sorento", "Land Cruiser", "Range Rover"]
    brand_num = random.randint(0, 2)
                    
    location = ["1", "2", "3"]      # Available locations
    loc_num = random.randint(0, 2)  # Picks one of the locations randomly

    new_car = [plate_number, brands[brand_num], size[size_let], location[loc_num]]
    new_car = ','.join(new_car)
    return new_car

def print_menu():
    os.system('cls||clear')
    print("~ Car database menu ~")
    print("1. Generate cars to file")
    print("2. Delete all cars from file\n")
    print("Press 'X' to exit.")
    return str(input("Choose your option: "))

def main():
    choice = ""
    while choice != "x":
        choice = print_menu()
        if choice == "1":
            number = int(input("Number of cars to generate: "))
            for i in tqdm(range(number)):
                new_car = generate_car()
                add_new_car(new_car)
            print("Installation complete")
            raw_input("Press enter to continue ")
        elif choice == "2":
            choice = input("Are you sure you want to delete all cars from file? (y/n) ")
            if choice == "y":
                try:
                    Cars_file = open("data/Cars.csv", "w+")
                    Cars_file.close()
                except(PermissionError):
                    print("Close file to make changes")
                    input("Press enter to continue ")
            

main()