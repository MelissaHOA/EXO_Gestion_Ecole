from datetime import date  # Importation de la classe date pour gérer les dates
from person import Person  # Importation de la classe Person (classe parente)
from address import Address  # Importation de la classe Address

# Classe Parent, représentant un parent d'élève, héritant de la classe Person
class Parent(Person):
    """
    Représente un parent d'élève.

    Attributes:
        _students (list): Liste des élèves associés à ce parent.
    """
    _students: list = []  # Liste privée pour stocker les enfants (élèves) associés à ce parent

    # Constructeur de la classe Parent
    def __init__(self, name: str, surname: str, age: int, address: Address, phone: int, mail: str, arrival_date: date,
                 students: list = []):
        """
        Initialise un parent avec les informations fournies.

        Args:
            name (str): Le prénom du parent.
            surname (str): Le nom de famille du parent.
            age (int): L'âge du parent.
            address (Address): L'adresse du parent.
            phone (int): Le numéro de téléphone du parent.
            mail (str): L'adresse e-mail du parent.
            arrival_date (date): La date d'arrivée du parent dans le système.
            students (list): Liste des élèves associés à ce parent.
        """
        # Appel du constructeur de la classe parente (Person)
        super().__init__(name, surname, age, address, phone, mail, arrival_date)
        _students = students  # Initialisation de la liste des élèves associés (enfants) à ce parent

    # Méthode pour ajouter un enfant (élève) à la liste des enfants associés à ce parent
    def add_child(self, bambin):
        """
        Ajoute un enfant à la liste des enfants du parent.

        Args:
            bambin (Student): L'élève à ajouter.
        """
        if bambin not in self._students:  # Vérifie si l'élève n'est pas déjà dans la liste
            self._students += [bambin]  # Ajoute l'élève à la liste

    # Méthode pour obtenir les détails du parent et de ses enfants sous forme de chaîne de caractères
    def get_details(self):
        """
        Récupère les détails du parent, y compris les élèves associés.

        Returns:
            str: Une chaîne de caractères contenant les détails du parent et de ses enfants.
        """
        from student import Student  # Importation locale pour éviter les importations circulaires
        retour: str = self.get_complete_name() + " est le parent de :\n"
        for pupil in self._students:
            retour += "- " + pupil.get_complete_name() + \
                      f" dont l'identifiant est {pupil.student_id}.\n"
        return retour  # Retourne les détails du parent et des enfants associés
