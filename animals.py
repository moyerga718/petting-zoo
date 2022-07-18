from models import slithering_animals, swimming_animals, walking_animals
from datetime import date
from models.slithering_animals.skink import Skink
from models.slithering_animals.slug import Slug
from models.slithering_animals.snail import Snail
from models.slithering_animals.snake import Snake
from models.slithering_animals.snekky import Snekky
from models.swimming_animals.eel import Eel
from models.swimming_animals.fish import Fish
from models.swimming_animals.kraken import Kraken
from models.swimming_animals.orca import Orca
from models.swimming_animals.shark import Shark
from models.walking_animals.cow import Cow
from models.walking_animals.donkey import Donkey
from models.walking_animals.horse import Horse
from models.walking_animals.llama import Llama
from models.walking_animals.piggy import Piggy

burt = Llama("Burt", "LLAMA")

trent = Donkey("Trent","Donk")

joni = Horse("Joni", "Cut Horse")

rachel = Piggy("Rachel", "Big Belly Boy")

gwen = Cow("Gwen","Hefferrrr")

janet = Snake("Janet", "Snek")

stefan = Snekky("Stefan", "Snek Mode")

bruce = Skink("Bruce", "Blue Tongue Skink")

franko = Snail("Franko", "Gross Snail")

lug = Slug("Lub", "Gross ass slug")

yurgi = Fish("Yurgi", "TOONA")

tabitha = Eel("Tabitha", "Electric")

guy = Shark("Guy Fieri", "Big boi")

porka = Orca("Porka", "Big Orca")

nick = Kraken("Nick","o shit o fuck")

print(nick)
print(nick.species)