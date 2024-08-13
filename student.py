from datetime import date
from parent import Parent
from person import Person
from teacher import Teacher
from lesson import Lesson


class Student(Person):
    """Il s'agit de la classe où
    on range les détails d'un élève"""
    _id_student: int
    _parent: list[Parent] = []
    _ref_teacher: Teacher
    courses_list: list = []

    def __init__(self, name, surname, age, address, phone, mail,
                 arrival_date: date, parent: Parent,
                 ref_teacher: Teacher, student_id: int):
        """C'est ici qu'on initialise l'objet étudiant, avec less renseignements qu'on possède"""
        super().__init__(name, surname, age, address, phone, mail, arrival_date)
        # On initialise l'objet de classe Student en tant que Person (un Student est une Person)
        self._parent += [parent]
        self._ref_teacher = ref_teacher
        self._id_student = student_id
   #     self.courses_list = []

    def add_parent(self, parent: Parent):
        if not parent in self._parent:
            self._parent += [parent]
            parent.add_child(self)

    def set_tutor(self, prof: Teacher):
        if self._ref_teacher is not None and self._ref_teacher is not prof:
            self._ref_teacher.del_pupil(self)
        self._ref_teacher = prof
        if self not in self._ref_teacher.tutor_of:
            self._ref_teacher.tutor_of += [self]

    def add_course(self, cours: Lesson):
        from academicrecord import AcademicRecord
        sholar=AcademicRecord(self, cours)
        self.courses_list
    @property
    def student_id(self):
        return self._id_student

    def get_details(self):
        from academicrecord import AcademicRecord
        retour: str = self.get_complete_name() + " a pour professeur référent " \
                      + self._ref_teacher.get_complete_name() + ".\n" \
                      + "Il étudie les matières suivantes :\n"
        for curriculum in self.courses_list:
            retour += curriculum.course.denomination + "\n"
            retour += "Son palmarès est le suivant : \n"
        for note in self.courses_list:
            appreciation: AcademicRecord = note
            retour += appreciation.get_details()
        return retour
