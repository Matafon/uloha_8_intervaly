cisla = [int(x) for x in input("Zadej číslo: ").split(',')]
zacatek = int(input("Zadej začátek intervalu: "))
konec = int(input("Zadej konce intervalu: "))
seznam = []

for cislo in cisla:
    if cislo > zacatek and cislo < konec:
        seznam.append(cislo)

print(seznam)