#Models
from Models.Customer import Customer
#Csv
import csv

class Customer_repo:
    def __init__self(self):
        pass


    def add_customers(self, customer_dict):
        # first add to file then to private list
        with open("data/Customers.csv", "w+") as Customer_file:
            Customer_file.write("first_name,last_name,date_of_birth,email,country,address,zip_code,phone,card,security_code,exp_date")
            for customer in customer_dict.values():
                first_name = customer.get_first_name()
                last_name = customer.get_last_name()
                date_of_birth = customer.get_date_of_birth()
                email = customer.get_email()
                country = customer.get_country()
                address = customer.get_address()
                zip_code = customer.get_zip_code()
                phone = customer.get_phone()
                card, security_code, exp_date = customer.get_card_info()
                Customer_file.write("\n{},{},{},{},{},{},{},{},{},{},{}".format(first_name, last_name, date_of_birth, 
                email, country, address, zip_code, phone, card, security_code, exp_date))

    def get_customers(self):
        self.customer_dict = {}
        with open("./data/Customers.csv", "r") as Customer_file:
            csv_reader = csv.reader(Customer_file)
            next(csv_reader)
            
            for line in csv_reader:
                first_name,last_name,date_of_birth,email,country,address,zip_code,phone,card,security_code,exp_date = line
                new_customer = Customer(first_name, last_name, date_of_birth, 
                email, country, address, zip_code, phone, card, security_code, exp_date)

                key = new_customer.get_email() #email is the key
                self.customer_dict[key] = new_customer

        return self.customer_dict