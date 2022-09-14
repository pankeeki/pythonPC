lentoasemat = {"EFHK": "Helsinki-Vantaa"}

while True:
    kysymys = int(input('Haluatko syöttää uuden lentoaseman (vastaa 1), '
                        'hakea lentoaseman tiedot (vastaa 2) vai lopettaa (vastaa 3)? '))
    if kysymys == 3:
        break
    elif kysymys == 2:
        iceo = input('Anna lentoaseman ICAO-koodi: ')
        if iceo in lentoasemat:
            print(f'Lentoasema {lentoasemat.get(iceo)}')
    elif kysymys == 1:
        icao = input('Anna uuden lentoaseman ICEO-koodi: ')
        nimi = input('Anna uuden lentoaseman nimi: ')
        lentoasemat[icao] = nimi
    else:
        print('Virheellinen vastaus. Valitse 1, 2 tai 3.')
