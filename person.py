from datetime import date  # Importation de la classe date pour gérer les dates
from abc import ABC, abstractmethod  # Importation des classes ABC et abstractmethod pour créer des classes abstraites
from address import Address  # Importation de la classe Address

# Classe abstraite Person, servant de base pour d'autres classes représentant des personnes
class Person(ABC):
    """
    Classe abstraite représentant une personne dans le système.

    Attributes:
        name (str): Le prénom de la personne.
        surname (str): Le nom de famille de la personne.
        age (int): L'âge de la personne.
        address (Address): L'adresse de la personne.
        phone (int): Le numéro de téléphone de la personne.
        mail (str): L'adresse e-mail de la personne.
        arrival_date (date): La date d'arrivée de la personne dans le système.
    """

    name: str  # Prénom de la personne
    surname: str  # Nom de famille de la personne
    age: int  # Âge de la personne
    address: Address  # Adresse de la personne
    phone: int  # Numéro de téléphone de la personne
    mail: str  # Adresse e-mail de la personne
    arrival_date: date  # Date d'arrivée ou d'inscription de la personne

    # Constructeur de la classe Person, initialisant les attributs de base
    def __init__(self, name: str, surname: str, age: int, address: Address,
                 phone: int, mail: str, arrival_date: date):
        """
        Initialise une personne avec les informations fournies.

        Args:
            name (str): Le prénom de la personne.
            surname (str): Le nom de famille de la personne.
            age (int): L'âge de la personne.
            address (Address): L'adresse de la personne.
            phone (int): Le numéro de téléphone de la personne.
            mail (str): L'adresse e-mail de la personne.
            arrival_date (date): La date d'arrivée de la personne dans le système.
        """
        self.name = name  # Initialisation du prénom
        self.surname = surname  # Initialisation du nom de famille
        self.age = age  # Initialisation de l'âge
        self.address = address  # Initialisation de l'adresse
        self.phone = phone  # Initialisation du numéro de téléphone
        self.mail = mail  # Initialisation de l'adresse e-mail
        self.arrival_date = arrival_date  # Initialisation de la date d'arrivée

    # Méthode pour obtenir le nom complet de la personne (prénom + nom de famille)
    def get_complete_name(self):
        """
        Récupère le nom complet de la personne.

        Returns:
            str: Le prénom et le nom de famille concaténés.
        """
        return self.name + " " + self.surname

    # Méthode pour modifier l'adresse de la personne
    def modify_address(self, new_address: Address):
        """
        Modifie l'adresse de la personne.

        Args:
            new_address (Address): La nouvelle adresse.
        """
        self.address = new_address

    # Méthode abstraite pour obtenir les détails de la personne
    # Cette méthode doit être implémentée par toute classe qui hérite de Person
    @abstractmethod
    def get_details(self):
        """
        Méthode abstraite pour obtenir les détails de la personne.

        Returns:
            str: Une chaîne de caractères contenant les détails de la personne.
        """
        pass
