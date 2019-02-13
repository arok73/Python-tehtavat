# -*- coding: utf-8 -*-

lista = []

while True:
    valinta = int(input("""Haluatko
    (1)Lisätä listaan
    (2)Poistaa listalta vai
    (3)Lopettaa?: """))

    if valinta == 1:
        lisays = input("Mitä lisätään?: ")
        lista.append(lisays)
    elif valinta == 2:
        print("Listalla on {l} alkiota.".format(l=len(lista)))
        poistettava = int(input("Monesko niistä poistetaan?: "))
        try:
            #t = lista[poistettava]
            lista.pop(poistettava)
        except IndexError:
            print("Virheellinen valinta.")
    elif valinta == 3:
        print("Listalla oli tuotteet:")
        for i in lista:
            print(i)
        break
    else:
        print("Virheellinen valinta.")
