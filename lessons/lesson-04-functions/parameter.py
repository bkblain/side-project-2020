animals = ("cat", "dog", "rabbit", "turtle", "bird")

def printer(air, land, water = None):
    print("air = ", air)
    print("land = ", land)

    if(water is not None):
        print("water = ", water)


print("common parameters")
printer(animals[4], animals[0], animals[3])
print("")

print("optional parameters")
printer(animals[4], animals[0])
print("")

print("parameters out of order")
printer(water = animals[3], air = animals[4], land = animals[0])
print("")



