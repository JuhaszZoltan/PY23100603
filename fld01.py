a:int = int(input('e.oldalu 3szog oldala (cm): '))
print(f'kerület hetede: {3*a/7:.2f} cm')

r:int = int(input('kör sugara (cm): '))
print(f'kör kerülete: {round(2*r*3.14, 2)} cm')

n:int = int(input('hány csillag legyen: '))
print(f'Béla jutalma: {n * "*"}')
print('Béla jutalma:', end=' ')
for _ in range(n):
    print('*', end='')
print('\n')