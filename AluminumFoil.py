def foil(length):
    diameter, thickness = 4, 0.0025
    while length>=diameter*3.14:
        length-=diameter*3.14
        diameter+=2*thickness 
    if length>=diameter*3.14/2:diameter+=2*thickness
    elif length>0: diameter+=thickness
    return round(diameter,4)


print(f"{foil(0)} ➞ 4.0")
print(f"{foil(50)} ➞ 4.02")
print(f"{foil(4321)} ➞ 5.4575")
print(f"{foil(10000)} ➞ 6.9175")