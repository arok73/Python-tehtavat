# -*- coding: utf-8 -*-


class Kilpailija:
    """Kilpailija: sisältää pisteet ja värin"""

    def __init__(self, vari, pisteet):
        vari = input("Anna minulle väri: ")
        self.vari = vari
        self.pisteet = pisteet

    def tilanne(self):
        print("Olen", self.vari,
              "ja minulla on", self.pisteet, "pistettä!")

    def maali(self, arvo=1):
        self.pisteet = + arvo


def main():
    eka = Kilpailija("sininen", 0)
    toka = Kilpailija("punainen", 0)
    eka.tilanne()
    toka.tilanne()
    print(eka.__doc__)


if __name__ == "__main__":
    main()
