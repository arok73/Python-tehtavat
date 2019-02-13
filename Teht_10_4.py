# -*- coding: utf-8 -*-


class Emo:
    arvo = 0
    tila = "Toiminnassa"

    def nimi(self):
        print("Minä olen emoluokka.")


class Lapsi(Emo):
    def nimi(self):
        print("Minä olen lapsiluokka.")


Emoluokka = Emo()
print(Emoluokka.tila)
Emoluokka.nimi()

Lapsiluokka = Lapsi()
print(Lapsiluokka.tila)
Lapsiluokka.nimi()
