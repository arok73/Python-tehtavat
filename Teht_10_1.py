# -*- coding: utf-8 -*-


class Kilpailija:
    def __init__(self, vari, pisteet):
        self.vari = vari
        self.pisteet = pisteet

    def tulosta(self):
        print("Kilpailijalla", self.vari,
              "on", self.pisteet, "pistettä!")


kisa = Kilpailija("sininen", 10)
kisa.tulosta()
