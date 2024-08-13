class Address:
    """
    Représente une adresse.

    Attributes:
        street (str): La rue de l'adresse.
        city (str): La ville de l'adresse.
        postal_code (str): Le code postal de l'adresse.
    """

    # Liste contenant toutes les instances de la classe Address
    liste_d_adresses: list['Address'] = []

    # Attributs représentant les informations de l'adresse
    street: str        # Rue de l'adresse
    city: str          # Ville de l'adresse
    postal_code: str   # Code postal de l'adresse

    # Constructeur de la classe, initialisant une adresse avec une rue, une ville et un code postal
    def __init__(self, street, city, postal_code):
        """
        Initialise une adresse.

        Args:
            street (str): La rue de l'adresse.
            city (str): La ville de l'adresse.
            postal_code (str): Le code postal de l'adresse.
        """
        self.street = street
        self.city = city
        self.postal_code = postal_code

        # Ajout de l'instance actuelle à la liste globale des adresses
        Address.liste_d_adresses += [self]

    # Propriété qui retourne l'adresse sous forme de chaîne de caractères
    @property
    def to_string(self):
        """
                Convertit l'adresse en une chaîne de caractères.

                Returns:
                    str: L'adresse sous forme de chaîne.
                """
        return self.street + " " + self.city + " " + self.postal_code
