# -*- coding: cp1252 -*-

def tulostaja(syote):
    lukumaara = len(syote)
    return lukumaara

def main():
    jatka = True

    while jatka:
        sana = input("Anna syöte (Lopeta lopettaa): ")
        if sana == "Lopeta":
            jatka = False
        else:
            pituus = tulostaja(sana)
            if pituus > 0:
                print("Antamasi syöte oli ", pituus, "merkkiä pitkä.")
            else:
                print("Et antanut syötettä")

if __name__ == "__main__":
    main()
