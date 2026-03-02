# practice methods to edit list
planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1,"Venus")
planet_list.insert(2,"Earth")
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]
del planet_list[8]

# function to display array
def display_planets(list):
    for planet in list:
        print(f"- {planet}")

# display planet list
print("Planets:")
display_planets(planet_list)

# display rocky planet list
print("Rocky Planets:")
display_planets(rocky_planets)
