# -*- coding: utf-8 -*-

import time
import pickle

sisalto = []


def lue_muistio():
    n = 1
    for i in sisalto:
        print("{}: ".format(n) + i)  # tulostetaan sisalto
        n = n+1


def lisaa_merkinta():
    # aikaleima muuttujan alustus tämän hetkisellä ajalla ja päivämäärällä
    aikaleima = ":::" + time.strftime("%X %x")
    lisays = input("Kirjoita uusi merkintä: ")
    lisays = lisays + aikaleima  # lisätään merkintä ja aikaleima
    sisalto.append(lisays)


def muokkaa_merkintaa():
    # aikaleima muuttujan alustus tämän hetkisellä ajalla ja päivämäärällä
    aikaleima = ":::" + time.strftime("%X %x")
    print("Listalla on {s} merkintää.".format(s=len(sisalto)))
    muokattava = int(input("Mitä niistä muutetaan?: ")) - 1
    try:
        print(sisalto[muokattava])
        muokkaus = input("Anna uusi teksti: ")
        sisalto[muokattava] = muokkaus + aikaleima
    except IndexError:
        print("Virheellinen valinta.")


def poista_merkinta():
    print("Listalla on {s} merkintää.".format(s=len(sisalto)))
    poistettava = int(input("Mitä niistä poistetaan?: "))
    try:
        print("Poistettiin merkintä:", sisalto.pop(poistettava-1))
    except IndexError:
        print("Virheellinen valinta.")


if __name__ == "__main__":

    muistion_nimi = "muistio.dat"

    # luodaan tekstitiedosto

    try:
        with open(muistion_nimi, 'rb') as f:
            sisalto = pickle.load(f)
    except FileNotFoundError:
        print("Virhe tiedostossa, luodaan uusi muistio.dat.")
        with open(muistion_nimi, 'wb'):
            pass

    while True:
        print("""(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta""")
        valinta = int(input("\nMitä haluat tehdä?: "))

        if valinta == 1:
            lue_muistio()  # suljetaan tiedosto
        elif valinta == 2:
            lisaa_merkinta()
        elif valinta == 3:
            muokkaa_merkintaa()
        elif valinta == 4:
            poista_merkinta()
        elif valinta == 5:
            print("Lopetetaan.")
            with open(muistion_nimi, "wb") as f:
                pickle.dump(sisalto, f)
            break  # ohjelman lopetus
        else:
            print("Tuntematon valinta.")
