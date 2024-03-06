print ("\n***********************************\n")

print ("Weather Branch\n")

#import Libraries Here
import random
from time import sleep

#Create a function that rnadomly chooses the weather from a list
def weather():
        weatherForcast = ["Snowing", "Blizzards", "Raining", "Foggy", "Windy", "icy", "sunny"]
        weatherConditions = random.choice(weatherForcast)
        return weatherConditions

print(weather())
