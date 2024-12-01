from random import randrange
import json
import sys

print(sys.argv)

number_of_buildings = 10000

buildings = []
for x in range(0, number_of_buildings):
  buildings.append({
    "buildingId": x + 1,
    "floor_area": randrange(500, 3000),
    "construction_cost": randrange(500, 2000),
    "hazard_probability": randrange(1, 10) / 200,
    "inflation_rate": randrange(3, 10) / 100,
  })
  
with open(sys.argv[1], "w") as outfile:
  json.dump(buildings, outfile)  
  