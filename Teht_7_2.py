# -*- coding: cp1252 -*-

from random import choice

aseet = ["Jalka", "Ydinase", "Torakka"]


def main():

    jatka = True
    kierros = 0

    while jatka:
        oma_valinta = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa):")
        if sana == "Lopeta":
            jatka = False
        if oma_valinta == "Jalka":
            oma_ase = 0
        elif oma_valinta == "Ydinase":
            oma_ase = 1
        elif oma_valinta == "Torakka":
            oma_ase = 2
        tietokone = random.randint(0, 2)
        if tietokone == 0 and oma_ase == 0:
            print("Sinä valitsit: Jalka")
            print("tietokone valitsi: Jalka)

        else:
            print("Kruuna")

        print("Sinä valitsit: ", oma_ase)
        kierros += 1


if __name__ == "__main__":
    main()
