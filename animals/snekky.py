from .animal import Animal

class Snekky(Animal):
    """ANIMAL DOCSTRANG
    """
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True