class Address:
    liste_d_adresses: list['Address'] = []
    street: str
    city: str
    postal_code: str

    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code
        Address.liste_d_adresses += [self]
    @property
    def to_string(self):
        return self.street + " " + self.city + " " + self.postal_code
