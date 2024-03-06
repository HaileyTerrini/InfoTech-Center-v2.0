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




weatherAlert = weather()



def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNational weather Service has updated our alarm by 30 minutes because of the forcast of",weatherAlert,
          "weather conditions.")
        print("VRS has been engaged only allowing you to drive 50mph.")
    elif weatherAlert == "Blizzards":
        print("\nNational weather Service has updated our alarm by 45 minutes because of the forcast of",weatherAlert,
        "weather conditions.")
        print("VRS has been engaged only allowing you to drive 40mph.")
    elif weatherAlert == "Raining":
        print("\nNational weather Service has updated our alarm by 10 minutes because of the forcast of",weatherAlert,
            "weather conditions.")
        print("VRS has been engaged only allowing you to drive 60mph.")


vehicleResponseSystem()
