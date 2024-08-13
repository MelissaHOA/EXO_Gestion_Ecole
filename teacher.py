from datetime import date  # Importation de la classe date pour gérer les dates
from address import Address  # Importation de la classe Address
from lesson import Lesson  # Importation de la classe Lesson
from person import Person  # Importation de la classe Person (classe parente)
# from student import Student  # Importation commentée pour éviter les importations circulaires

class Teacher(Person):
    """
    Représente un enseignant.

    Attributes:
        tutor_of (list[Student]): Liste des élèves que l'enseignant supervise.
        teaches (list[Lesson]): Liste des cours que l'enseignant enseigne.
    """
    tutor_of: list = ['Student']  # Liste des élèves que le professeur encadre (initialisée par défaut avec le type 'Student')
    teaches: list[Lesson]  # Liste des cours que le professeur enseigne

    def __init__(self, name: str, surname: str, age: int, address: Address,
                 phone: int, e_mail: str, arrival_date: date,
                 courses: list[Lesson], pupils: list['Student.Student']):
        """
        Initialise un enseignant avec les informations fournies.

        Args:
            name (str): Le prénom de l'enseignant.
            surname (str): Le nom de famille de l'enseignant.
            age (int): L'âge de l'enseignant.
            address (Address): L'adresse de l'enseignant.
            phone (int): Le numéro de téléphone de l'enseignant.
            e_mail (str): L'adresse e-mail de l'enseignant.
            arrival_date (date): La date d'arrivée de l'enseignant dans le système.
            courses (list[Lesson]): Liste des cours que l'enseignant enseigne.
            pupils (list[Student]): Liste des élèves supervisés par l'enseignant.
        """
        if pupils is None:
            pupils = []  # Initialisation de la liste des élèves si elle est None
        super().__init__(name, surname, age, address, phone, e_mail, arrival_date)
        self.tutor_of = pupils  # Associe les élèves au professeur
        self.teaches = courses  # Associe les cours que le professeur enseigne

        # Associe le professeur aux élèves
        for pupil in self.tutor_of:
            pupil._ref_teacher = self
        # Associe le professeur aux cours qu'il enseigne
        for lesson in self.teaches:
            lesson.prof = self

    # Méthode pour ajouter un élève à la liste des élèves encadrés par le professeur
    def add_pupil(self, pupil: 'Student'):
        """
        Ajoute un élève à la liste des élèves supervisés par l'enseignant.

        Args:
            pupil (Student): L'élève à ajouter.
        """
        from student import Student  # Importation locale pour éviter les importations circulaires
        if pupil not in self.tutor_of:
            self.tutor_of += [pupil]  # Ajoute l'élève à la liste des élèves encadrés
        pupil.set_tutor(self)  # Définit ce professeur comme le tuteur de l'élève

    # Méthode pour ajouter un cours à la liste des cours que le professeur enseigne
    def add_subject(self, course: Lesson):
        """
        Ajoute un cours à la liste des cours enseignés par l'enseignant.

        Args:
            course (Lesson): Le cours à ajouter.
        """
        self.teaches += [course]  # Ajoute le cours à la liste des cours
        course.prof = self  # Associe ce professeur au cours

    # Méthode pour supprimer un élève de la liste des élèves encadrés par le professeur
    def del_pupil(self, pupil: 'Student'):
        """
        Supprime un élève de la liste des élèves supervisés par l'enseignant.

        Args:
            pupil (Student): L'élève à supprimer.
        """
        # from student import Student  # Importation commentée
        self.tutor_of.remove(pupil)  # Retire l'élève de la liste des élèves encadrés
        pupil.set_tutor(None)
    # Méthode pour supprimer un cours de la liste des cours que le professeur enseigne
    def del_course(self, subject: Lesson):
        """
        Supprime un cours de la liste des cours enseignés par l'enseignant.

        Args:
            subject (Lesson): Le cours à supprimer.
        """
        self.teaches.remove(subject)  # Retire le cours de la liste des cours
        subject.prof=None
    # Méthode pour obtenir les détails du professeur, y compris les cours enseignés et les élèves encadrés
    def get_details(self):
        """
        Récupère les détails de l'enseignant, y compris les cours enseignés et les élèves supervisés.

        Returns:
            str: Une chaîne de caractères contenant les détails de l'enseignant.
        """
        retour = f"{self.get_complete_name()} enseigne :\n"
        for course in self.teaches:
            retour += f"- {course.denomination}. "  # Liste des cours que le professeur enseigne
        retour += "Iel suit les élèves suivants \n"
        for pupil in self.tutor_of:
            retour += f"_ {pupil.get_complete_name()}"  # Liste des élèves encadrés par le professeur
        return retour  # Retourne les détails du professeur
