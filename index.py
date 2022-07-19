from models import slithering_animals, swimming_animals, walking_animals, attractions
from models.attractions.petting_zoo import PettingZoo
from models.attractions.snake_pit import SnakePit
from models.attractions.wetlands import Wetlands

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

burt = Llama("Burt", "LLAMA", "Morning", "Sand")

trent = Donkey("Trent","Donk", "Morning", "Bagels")

joni = Horse("Joni", "Cut Horse", "Midday", "Man Hands")

rachel = Piggy("Rachel", "Big Belly Boy", "Afternoon", "Socks")

gwen = Cow("Gwen","Hefferrrr", "Afternoon", "veggies")

janet = Snake("Janet", "Snek", "grass")

stefan = Snekky("Stefan", "Snek Mode", "curses")

bruce = Skink("Bruce", "Blue Tongue Skink", "tents")

franko = Snail("Franko", "Gross Snail", "poison!")

lug = Slug("Lub", "Gross ass slug", "spiders")

yurgi = Fish("Yurgi", "TOONA", "beans")

tabitha = Eel("Tabitha", "electric eel", "whole milk")

guy = Shark("Guy Fieri", "Big boi", "sizable man")

porka = Orca("Porka", "Big Orca", "chow")

nick = Kraken("Nick","big squid", "rice cereal")

roberto = Llama("Roberto", "alpaca", "midday", "jimmy johns")

bobbies_zoo = PettingZoo("Bobbies Big 'Ol Zoo", "a ton of filthy rats")
bobbies_pit = SnakePit("Bobbies Big 'Ol Snake Pit", "a ton of gross... things")
bobbies_wetland = Wetlands("Bobbies Big 'Ol Wetland", "squishy, mucky, sloppy creatures")

bobbies_zoo.add_animal(roberto)
bobbies_zoo.add_animal(burt)
bobbies_zoo.add_animal(trent)
bobbies_zoo.add_animal(joni)
bobbies_zoo.add_animal(rachel)
bobbies_zoo.add_animal(gwen)

print(bobbies_zoo)

bobbies_wetland.add_animal(yurgi)
bobbies_wetland.add_animal(tabitha)
bobbies_wetland.add_animal(guy)
bobbies_wetland.add_animal(porka)
bobbies_wetland.add_animal(nick)

print(bobbies_wetland)

bobbies_pit.add_animal(janet)
bobbies_pit.add_animal(stefan)
bobbies_pit.add_animal(lug)
bobbies_pit.add_animal(bruce)
bobbies_pit.add_animal(franko)

print(bobbies_pit)
