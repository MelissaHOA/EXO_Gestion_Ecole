from datetime import date

from person import Person
from address import Address


class Parent(Person):
    _students: list =[]

    def __init__(self, name: str, surname: str, age: int, address: Address, phone: int, mail: str, arrival_date: date,
                 students: list = []):
        super().__init__(name, surname, age, address, phone, mail, arrival_date)
        _students = students

    def add_child(self, bambin):
        if bambin not in self._students:
            self._students += [bambin]

    def get_details(self):
        from student import Student
        retour: str = self.get_complete_name() + " est le parent de :\n"
        for pupil in self._students:
            retour += "- " + pupil.get_complete_name() + \
                      f" dont l'identifiant est {pupil.student_id}.\n"
        return retour
