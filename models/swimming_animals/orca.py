from datetime import date

class Orca:
    """ANIMAL DOCSTRANG
    """
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True