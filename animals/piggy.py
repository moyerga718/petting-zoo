from animals.animal import Animal

class Piggy(Animal):
    """ANIMAL DOCSTRANG
    """
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True