szam:int = 3456
osszeg:int = 0
while szam % 10 != 0:
    szam = int(input('írj be egy számot: '))
    osszeg += szam
print(f'számok összege: {osszeg}')