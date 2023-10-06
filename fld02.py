x:int = int(input('egyik szám: '))
y:int = int(input('másik szám: '))

osszeg:int = 0
if y > x:
    for n in range(x+1, y):
        print(n, end=' ')
        osszeg += n
else:
    for n in range(y+1, x):
        print(n, end=' ')
        osszeg += n

print(f'\nszámok összege: {osszeg}')