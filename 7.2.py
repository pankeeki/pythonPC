nimet = set()


while True:
    nimi = input('Anna nimi: ')
    if nimi == '':
        break
    elif nimi in nimet:
        print('Aiemmin syötetty nimi.')
    else:
        print('Uusi nimi.')
        nimet.add(nimi)
for nimi in nimet:
    print(nimi)
