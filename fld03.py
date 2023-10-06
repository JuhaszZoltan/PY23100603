x:int = int(input('egyik szám: '))
y:int = int(input('másik szám: '))

if x > y: (x, y) = (y, x)

osszeg:int = 0
for n in range(x+1, y):
    print(n, end=' ')
    osszeg += n

print(f'\nszámok összege: {osszeg}')