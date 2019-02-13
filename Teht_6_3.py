# -*- coding: cp1252 -*-

def tulostaja(syote = "Oletustulostus"):
    print(syote)

def main():
    jatka = True

    while jatka:
        sana = input("Anna syöte (Lopeta lopettaa): ")
        if sana == "Lopeta":
            jatka = False
        elif len(sana) > 5:
            tulostaja(sana)
        else:
            tulostaja()

if __name__ == "__main__":
    main()
