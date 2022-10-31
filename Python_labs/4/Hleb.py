mass = [5, 7, 35, 33, 13, 29, 24, 12, 11, 22]
print(mass)

for el in range(3):
    mass.insert(4, 1)
print(mass)

min = mass[0]
for el in mass:
    if el< min:
        min =el
print(min)