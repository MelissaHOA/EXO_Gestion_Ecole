from lesson import Lesson
from student import Student


class AcademicRecord:
    pupil: Student
    course: Lesson
    score: int
    comment: str
    level_class: str

    def __init__(self, pupil: Student, course: Lesson):
        self.pupil = pupil
        self.course = course
        pupil.courses_list += [self]
        course.pupils_list += [self]
        self.score = 20
        self.comment = ""
        self.level_class = "Beginners"

    def set_comment(self, appreciation: str):
        self.comment = appreciation

    def set_note(self, note: int):
        self.score = note

    def get_details(self):
        return f"L'élève {self.pupil.get_complete_name()} dont l'ID est {self.pupil.student_id} \n" + \
            f"a eu la note {self.score} en {self.course.denomination}. \n" + \
            f"Le niveau de la classe est {self.level_class}\n" + \
            f"Le commentaire est le suivant :\n {self.comment}"
