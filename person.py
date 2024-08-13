from datetime import date
from abc import ABC, abstractmethod
from address import Address


class Person(ABC):
    name: str
    surname: str
    age: int
    address: Address
    phone: int
    mail: str
    arrival_date: date

    def __init__(self, name: str, surname: str, age: int, address: Address,
                 phone: int, mail: str, arrival_date: date):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone = phone
        self.mail = mail
        self.arrival_date = arrival_date

    def get_complete_name(self):
        return self.name + " " + self.surname

    def modify_address(self, new_address: Address):
        self.address = new_address

    @abstractmethod
    def get_details(self):
        pass
