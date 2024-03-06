#Import Libraries Here
import time
import sys
import random
from time import sleep

timeToSleep = 3

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsis add a dot .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message =("InInfoTech Center Operating System Booting" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # /r prints carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print ("\n\nOperating Syatem Booted up - Retina Scanned - Access Granted!")

print("\n***************************\n")
print("Gasoline Branch\n")

#Function that lists Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
        gasLevelList = ["Empty","Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
        currentGasLevel = random.choice(gasLevelList)
        return currentGasLevel

#Function that lists Gas Stations, m randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Marathon", "Circle K", "Moble", "Costco", "Meijer", "7Eleven"]
    gasStationsNearby = random.choice (gasStations)
    return gasStationsNearby


#Function will call the gasLecelGauge to detirmine out gas lave; and then find a close gas station
#by calling the listOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2.5)
        print("   ***Calling Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(), "which is",milesToGasStationsLow,"miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking google maps for the closest gas stations...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(), "which is",milesToGasStationsQuarterTank,"miles away")
    elif gasLevelIndicator == "Half Tank":
        print("Your has tank is a half of a tank full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarter tank.")
    else:
        print("Your gas tank is full - YEAHH!!! - Congratulations! - Vroom Vrooms!")

gasLevelAlert()






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

