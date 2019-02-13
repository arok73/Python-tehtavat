import random

aseet = ["Jalka", "Ydinase", "Torakka", "Lopeta"]
pelaaja = 1

def kysy_ase(pelaaja):
    while True:
        ase = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa):")
        if ase in aseet:
            return ase
        else:
            print("Valitse joko Jalka, Ydinase tai Torakka!")

def tulosta_ase(ase_pelaaja, ase_tietokone):
    print("Sinä valitsit: {a}".format(a=ase_pelaaja))
    print("tietokone valitsi: {b}".format(b=ase_tietokone))

def kuka_voitti(ase_pelaaja, ase_tietokone, tasa):
    apuase = aseet[:3]
    heikkous = apuase[(apuase.index(ase_tietokone) + 1) % len(apuase)]
    if ase_pelaaja == ase_tietokone:
        print("Tasapeli!")
        return 0, 0, 1
    elif ase_pelaaja == heikkous:
        print("Voitit!")
        return 0, 1, 0
    else:
        print("Hävisit!")
        return 1, 0, 0

def nayta_voitot(kierros, voitto, tasatulos):
    print("Pelasit {k} kierrosta, joista voitit {v} ja pelasit tasan {t} peliä.".format(k=kierros, v=voitto, t=tasatulos))

if __name__ == "__main__":

    voitto = 0
    havio = 0
    tasatulos = 0
    jatka = True
    kierros = 0

    while jatka:
        ase_pelaaja = kysy_ase(pelaaja)
        if ase_pelaaja == "Lopeta":
            jatka = False
        else:
            aseen_arvonta = random.randint(1,3)
            if aseen_arvonta == 1:
                ase_tietokone = "Jalka"
            elif aseen_arvonta == 2:
                ase_tietokone = "Torakka"
            elif aseen_arvonta == 3:
                ase_tietokone = "Ydinase"
            tulosta_ase(ase_pelaaja, ase_tietokone)
            tulos = kuka_voitti(ase_pelaaja, ase_tietokone, tasatulos)
            voitto += tulos[1]
            tasatulos += tulos[2]
            kierros = kierros + 1
    nayta_voitot(kierros, voitto, tasatulos)
