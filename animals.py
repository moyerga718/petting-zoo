from models import slithering_animals, swimming_animals, walking_animals

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

burt = Llama("Burt", "LLAMA", "Morning")

trent = Donkey("Trent","Donk", "Morning")

joni = Horse("Joni", "Cut Horse", "Midday")

rachel = Piggy("Rachel", "Big Belly Boy", "Afternoon")

gwen = Cow("Gwen","Hefferrrr", "Afternoon")

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

roberto = Llama("Roberto", "alpaca", "midday")
print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
# prints Roberto the alpaca is available to pet during the midday shift.