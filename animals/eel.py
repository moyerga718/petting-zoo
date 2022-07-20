from animals.animal import Animal

class Eel(Animal):
    """ANIMAL DOCSTRANG
    """
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
        