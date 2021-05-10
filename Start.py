import json
import os.path
from os import path

from GardenMaker import GardenMaker
from PathMaker import PathMaker

# Generate Garden
rows = int(input("How many rows in the garden? "))

garden = GardenMaker().run()

"""
def getPath(distance=rows, array=pm.make_list()):
    #print(array)
    if distance != 0:
        for listI in array:
            print("\t" * (rows - distance) + listI.current_plant.name)
            #time.sleep(1)

            if distance != 0:
                list_next = listI.make_list()
                getPath(distance - 1, list_next)

getPath()
"""

# Generate settings file
if not path.exists("settings.txt"):
    settingOut = ""
    for plant in garden.plants:
        settingOut += "\"" + plant.name + "\": true\n"
    settingOut = settingOut[0:len(settingOut)-1]

# Output file
    f = open("settings.txt", "w")
    f.write(settingOut)
    f.close()
    print("Please edit the settings file:")
    input("Press Enter to continue...")

# Get file
f = open("settings.txt", "r")
settingsInString = "{" + (f.read()).replace("\n", ", ") + "}"
settingsIn = json.loads(settingsInString)

# Generate all possible combos
possible_combos = []
for plant in garden.plants:
    pm = PathMaker(plant, 0)
    while not pm.is_end():
        possible_combos.append(pm.get_path(rows))
#print(possible_combos)

# Remove all paths with these
for currentPlantName in settingsIn:
    # Gotta remove
    if not settingsIn[currentPlantName]:
        # loop through all possible paths
        for n in range(len(possible_combos)-1, -1, -1):
            currentPath = possible_combos[n]
            # Found one
            if currentPlantName in currentPath:
                possible_combos.pop(n)

# Show user
if len(possible_combos) == 0:
    print("No paths found")
for combo in possible_combos:
    print(combo)
