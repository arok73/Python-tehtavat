# -*- coding: cp1252 -*-
def toinenpotenssi(tulos):
    lasku = tulos*tulos
    return lasku

def main():
    luku = int(input("Anna lukuarvo: "))
    print("Toinen potenssi on ", toinenpotenssi(luku))

if __name__ == "__main__":
    main()
