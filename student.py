from datetime import date  # Importation de la classe date pour gérer les dates
from parent import Parent  # Importation de la classe Parent
from person import Person  # Importation de la classe Person (classe parente)
from teacher import Teacher  # Importation de la classe Teacher
from lesson import Lesson  # Importation de la classe Lesson


class Student(Person):

    """
    Représente un élève.

    Attributes:
        _id_student (int): L'identifiant unique de l'élève.
        _parent (list[Parent]): Liste des parents de l'élève.
        _ref_teacher (Teacher): Le professeur référent de l'élève.
        courses_list (list[AcademicRecord]): Liste des dossiers académiques associés à l'élève.
    """

    _id_student: int  # Identifiant unique de l'étudiant
    _parent: list[Parent] = []  # Liste des parents associés à l'étudiant
    _ref_teacher: Teacher  # Professeur référent de l'étudiant
    courses_list: list = []  # Liste des cours associés à l'étudiant via des AcademicRecord

    # Constructeur de la classe Student
    def __init__(self, name, surname, age, address, phone, mail,
                 arrival_date: date, parent: Parent,
                 ref_teacher: Teacher, student_id: int):
        """
        Initialise un élève avec les informations fournies.

        Args:
            name (str): Le prénom de l'élève.
            surname (str): Le nom de famille de l'élève.
            age (int): L'âge de l'élève.
            address (Address): L'adresse de l'élève.
            phone (int): Le numéro de téléphone de l'élève.
            mail (str): L'adresse e-mail de l'élève.
            arrival_date (date): La date d'arrivée de l'élève dans le système.
            parent (Parent): Le parent de l'élève.
            ref_teacher (Teacher): Le professeur référent de l'élève.
            student_id (int): L'identifiant unique de l'élève.
        """
        super().__init__(name, surname, age, address, phone, mail, arrival_date)
        self._parent += [parent]  # Associe le parent à l'étudiant
        self._ref_teacher = ref_teacher  # Associe le professeur référent à l'étudiant
        self._id_student = student_id  # Assigne un identifiant unique à l'étudiant

    # Méthode pour ajouter un parent à la liste des parents de l'étudiant
    def add_parent(self, parent: Parent):
        """
        Ajoute un parent à la liste des parents de l'élève.

        Args:
            parent (Parent): Le parent à ajouter.
        """
        if not parent in self._parent:
            self._parent += [parent]
            parent.add_child(self)  # Associe également l'étudiant au parent

    # Méthode pour définir ou changer le professeur référent de l'étudiant
    def set_tutor(self, prof: Teacher):
        """
        Définit le professeur référent de l'élève.

        Args:
            prof (Teacher): Le nouveau professeur référent.
        """
        if self._ref_teacher is not None and self._ref_teacher is not prof:
            self._ref_teacher.del_pupil(self)  # Retire l'étudiant de l'ancien professeur référent
        self._ref_teacher = prof  # Définit le nouveau professeur référent
        if self not in self._ref_teacher.tutor_of:
            self._ref_teacher.tutor_of += [self]  # Ajoute l'étudiant au nouveau professeur référent

    # Méthode pour ajouter un cours à la liste des cours de l'étudiant via un AcademicRecord
    def add_course(self, cours: Lesson):
        """
        Associe un cours à l'élève via un dossier académique.

        Args:
            cours (Lesson): Le cours à ajouter.
        """
        from academicrecord import AcademicRecord  # Importation locale pour éviter les importations circulaires
        sholar = AcademicRecord(self, cours)  # Crée un lien entre l'étudiant et le cours via AcademicRecord
        self.courses_list += [sholar]  # Ajoute le dossier académique (AcademicRecord) à la liste des cours

    @property
    def student_id(self):
        """
        Récupère l'identifiant unique de l'élève.

        Returns:
            int: L'identifiant de l'élève.
        """
        """Retourne l'identifiant unique de l'étudiant."""
        return self._id_student

    # Méthode pour obtenir les détails de l'étudiant, y compris les cours suivis et les résultats
    def get_details(self):
        """
        Récupère les détails de l'élève, y compris les cours et les notes.

        Returns:
            str: Une chaîne de caractères contenant les détails de l'élève.
        """
        from academicrecord import AcademicRecord  # Importation locale pour éviter les importations circulaires
        retour: str = self.get_complete_name() + " a pour professeur référent " \
                      + self._ref_teacher.get_complete_name() + ".\n" \
                      + "Il étudie les matières suivantes :\n"
        for curriculum in self.courses_list:
            retour += curriculum.course.denomination + "\n"
            retour += "Son palmarès est le suivant : \n"
        for note in self.courses_list:
            appreciation: AcademicRecord = note
            retour += appreciation.get_details()
        return retour  # Retourne les détails de l'étudiant et de ses résultats académiques
