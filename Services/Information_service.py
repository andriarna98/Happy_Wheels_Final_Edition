#Models
from Models.Salesman import Salesman
#Repos
from Repository.Salesman_repo import Salesman_repo
#Os
import os

class Information_service:
    def __init__(self):
        #Repos
        self.salesman_repo = Salesman_repo()

    def get_salesman_dict(self):
        salesmen_dict = self.salesman_repo.get_salesmen()
        return salesmen_dict
        