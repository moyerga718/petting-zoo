class SnakePit:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'

    def add_animal(self, animal_obj):
        self.animals.append(animal_obj)
    
    def create_output_string(self):
        myString = f"{self.attraction_name} is where you'll find {self.description}, like"
        for animal in self.animals:
            myString += f"\n*{animal.name} the {animal.species}"
        return myString

    def  __str__(self):
        return self.create_output_string()