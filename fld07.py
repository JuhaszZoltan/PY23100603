dolgok:list[str] = ['bicikli', 'labda', 'F22es vadászgép', 'kenguru', 'vertikális paralelogramma', 'kecske', 'szánkó']

ker:str = input('mit keresel?: ')
for cucc in dolgok:
    if cucc == ker:
        print(f'megvan a {ker}, benne van a listában!')
        print(f'indexe: {dolgok.index(cucc)}')
        break
else: print(f'nem találom a {ker}-t :((')