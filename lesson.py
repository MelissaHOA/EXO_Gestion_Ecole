from datetime import date  # Importation de la classe date pour gérer les dates
from person import Person  # Importation de la classe Person

# Classe Lesson représentant un cours enseigné par un professeur à un groupe d'élèves


class Lesson:
    """
    Représente un cours.

    Attributes:
        denomination (str): Le nom ou la dénomination du cours.
        start_date (date): La date de début du cours.
        end_date (date): La date de fin du cours.
        prof (Person): Le professeur qui enseigne ce cours.
        pupils_list (list): Liste des dossiers académiques associés à ce cours.
    """
    denomination: str      # Nom du cours (ex: "Mathématiques")
    start_date: date       # Date de début du cours
    end_date: date         # Date de fin du cours
#    time: datetime         # (Commenté) Heure du cours
#    duration: int          # (Commenté) Durée du cours en minutes
#    location: str          # (Commenté) Lieu où se déroule le cours
    prof: Person           # Professeur responsable du cours
    pupils_list: list = []  # Liste des élèves inscrits au cours

    # Constructeur de la classe, initialisant un cours avec son nom, ses dates et son professeur
    def __init__(self, subject: str,
                 start_date: date,
                 end_date: date,
                 teacher: 'Teacher'):
        """
            Initialise un cours avec les informations fournies.

            Args:
                subject (str): Le nom ou la dénomination du cours.
                start_date (date): La date de début du cours.
                end_date (date): La date de fin du cours.
                teacher (Teacher): Le professeur enseignant ce cours.
            """
        self.denomination = subject  # Attribution du nom du cours
        self.start_date = start_date  # Attribution de la date de début du cours
        self.end_date = end_date      # Attribution de la date de fin du cours
#        self.time = edt_debut         # (Commenté) Initialisation de l'heure du cours
#        self.duration = edt_duration  # (Commenté) Initialisation de la durée du cours
        self.prof = teacher           # Attribution du professeur en charge
        teacher.add_subject(self)     # Ajout de ce cours à la liste des cours du professeur

    # Méthode pour ajouter un élève au cours
    def add_pupil(self, pupil):
        """
            Associe un élève au cours via un dossier académique.

            Args:
                pupil (Student): L'élève à associer au cours.
            """
        from academicrecord import AcademicRecord  # Importation locale pour éviter les importations circulaires
        cdc = AcademicRecord(pupil, self)          # Création d'un enregistrement académique pour l'élève et le cours

    # Méthode pour obtenir les détails du cours sous forme de chaîne de caractères
    def get_details(self):
        """
        Récupère les détails du cours.

        Returns:
            str: Une chaîne de caractères contenant les détails du cours.
        """
        return f"Cours de {self.denomination} \n" + \
            f"Enseigné par {self.prof.get_complete_name()}.\n" +  \
            f"a commencé le {self.start_date} \n" + \
            f"se termine le {self.end_date}"
