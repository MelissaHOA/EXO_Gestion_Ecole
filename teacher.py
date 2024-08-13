from datetime import date
from address import Address
from lesson import Lesson
from person import Person
# from student import Student


class Teacher(Person):
    tutor_of: list = ['Student']
    teaches: list[Lesson]

    def __init__(self, name: str, surname: str, age: int, address: Address,
                 phone: int, e_mail: str, arrival_date: date,
                 courses: list[Lesson], pupils: list['Student.Student']):
        if pupils is None:
            pupils = []
        # from student import Student
        super().__init__(name, surname, age, address, phone,
                         e_mail, arrival_date)
        self.tutor_of = pupils
        self.teaches = courses
        for pupil in self.tutor_of:
            pupil._ref_teacher = self
        for lesson in self.teaches:
            lesson.prof = self

    def add_pupil(self, pupil: 'Student'):
        from student import Student
       # robin: Student = pupil
        if pupil not in self.tutor_of:
            self.tutor_of += [pupil]
        pupil.set_tutor(self)

    def add_subject(self, course: Lesson):
        self.teaches += [course]
        course.prof = self

    def del_pupil(self, pupil: 'Student'):
        # from student import Student
        # robin: Student = Student(pupil)
        self.tutor_of.remove(pupil)

    def del_course(self, subject: Lesson):
        self.teaches.remove(subject)

    def get_details(self):
        retour = f"{self.get_complete_name()} enseigne :\n"
        for course in self.teaches:
            retour += f"- {course.denomination}. "
        retour += "Iel suit les élèves suivants \n"
        for pupil in self.tutor_of:
            retour += f"_ {pupil.get_complete_name()}"
        return retour
