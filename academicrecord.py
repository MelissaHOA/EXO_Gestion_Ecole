# Importation des classes Lesson et Student depuis leurs modules respectifs
from lesson import Lesson
from student import Student


# Classe AcademicRecord représentant une association entre un élève (Student) et un cours (Lesson)
class AcademicRecord:
    """
    Représente un dossier académique liant un élève à un cours.

    Attributes:
        pupil (Student): L'élève associé à ce dossier académique.
        course (Lesson): Le cours associé à ce dossier académique.
        score (int): La note obtenue par l'élève dans ce cours.
        comment (str): Les commentaires du professeur sur la performance de l'élève.
        level_class (str): Le niveau de la classe pour ce cours.
    """
    # Déclaration des attributs avec leurs types
    pupil: Student  # L'élève concerné par cet enregistrement académique
    course: Lesson  # Le cours concerné par cet enregistrement académique
    score: int  # La note de l'élève dans ce cours
    comment: str  # Un commentaire sur la performance de l'élève
    level_class: str  # Le niveau de la classe (par exemple : débutant, intermédiaire, avancé)

    # Initialisation de la classe avec un élève et un cours
    def __init__(self, pupil: Student, course: Lesson):
        """
        Initialise un dossier académique pour un élève et un cours.

        Args:
            pupil (Student): L'élève associé à ce dossier.
            course (Lesson): Le cours associé à ce dossier.
        """
        self.pupil = pupil
        self.course = course

        # Ajout de cet enregistrement à la liste des cours suivis par l'élève
        pupil.courses_list += [self]

        # Ajout de cet enregistrement à la liste des élèves suivant ce cours
        course.pupils_list += [self]

        # Initialisation des autres attributs
        self.score = 20  # Note par défaut, ici 20/20
        self.comment = ""  # Commentaire vide par défaut
        self.level_class = "Beginners"  # Niveau par défaut de la classe

    # Méthode pour définir un commentaire sur la performance de l'élève

    def set_comment(self, appreciation: str):
        """
        Définit un commentaire pour le dossier académique.

        Args:
            self (AcademicRecord) : le dossier scolaire lui-même
            appreciation (str): Le commentaire du professeur.
        """
        self.comment = appreciation

    # Méthode pour définir la note obtenue par l'élève dans le cours
    def set_note(self, note: int):
        """
        Définit la note obtenue par l'élève pour ce cours.

        Args:
            self (AcademicRecord) le carnet de note
            note (int): La note à attribuer.
        """
        self.score = note

    # Méthode pour obtenir les détails de l'enregistrement académique sous forme de chaîne de caractères

    def get_details(self):
        """
        Récupère les détails complets du dossier académique.

        Returns:
            str: Une chaîne de caractères contenant les détails du dossier.
        """
        return f"L'élève {self.pupil.get_complete_name()} dont l'ID est {self.pupil.student_id} \n" + \
            f"a eu la note {self.score} en {self.course.denomination}. \n" + \
            f"Le niveau de la classe est {self.level_class}\n" + \
            f"Le commentaire est le suivant :\n {self.comment}"
