from datetime import date  # , datetime

from person import Person


# from academicrecord import AcademicRecord
# from teacher import Teacher


class Lesson:
    denomination: str
    start_date: date
    end_date: date
#    time: datetime
#    duration: int
#    location: str
    prof: Person
    pupils_list: list = []

    def __init__(self, subject: str,
                 start_date: date,
                 end_date: date,
                 teacher: 'Teacher'):
        self.denomination = subject
        self.start_date = start_date
        self.end_date = end_date
#        self.time = edt_debut
#        self.duration = edt_duration
        self.prof = teacher
        teacher.add_subject(self)

    def add_pupil(self, pupil):
        from academicrecord import AcademicRecord
        cdc=AcademicRecord(pupil, self)
    def get_details(self):
        return f"Cours de {self.denomination} \n" + \
            f"Enseigné par {self.prof.get_complete_name()}.\n" +  \
            f"a commencé le {self.start_date} \n" + \
            f" se termine le {self.end_date}"
