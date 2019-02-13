# -*- coding: utf-8 -*-


class Kilpailija:
    #pisteet = 0
    #vari = "punainen"

   # def __init__(self, __vari, __pisteet):
        #self.vari = __vari
        #self.pisteet = __pisteet

    def tilanne(self):
        print("Olen", self.vari,
              "ja minulla on", self.pisteet, "pistettä!")

    def maali(self, arvo=1):
        self.pisteet = + arvo
        # return self.__pisteet


eka = Kilpailija()
eka.vari = "sininen"
eka.maali()
eka.tilanne()
