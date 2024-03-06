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
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50mph.")
    elif weatherAlert == "Blizzards":
        print("\nNational weather Service has updated our alarm by 45 minutes because of the forcast of",weatherAlert,
        "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 40mph.")
    elif weatherAlert == "Raining":
        print("\nNational weather Service has updated our alarm by 10 minutes because of the forcast of",weatherAlert,
            "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60mph.")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60 MPH.")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 70 MPH.")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 30 MPH.")
    else:
        print("\nNational Weather Service forecasts", weatherAlert, "weather conditions.")
        sleep(1.5)
        print("VRS has been disengaged! Drive at your own risk.")


vehicleResponseSystem()