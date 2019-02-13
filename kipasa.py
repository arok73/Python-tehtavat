import random

aseet = ["Jalka", "Ydinase", "Torakka", "Lopeta"]
pelaaja = 1

def aseen_arvonta():
    ase = random.randint(1,3)
    if ase == 1:
        tietokone = "Jalka"
        return tietokone
    elif ase == 2:
        tietokone = "Ydinase"
        return tietokone
    else:
        tietokone = "Torakka"
        return tietokone

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

def kuka_voitti(ase_pelaaja, ase_tietokone):
    if ase_pelaaja == ase_tietokone:
        return 'Tasapeli!'
    elif ase_pelaaja == "Jalka" and ase_tietokone == "Ydinase":
        return 'Hävisit!'
    elif ase_pelaaja == "Ydinase" and ase_tietokone == "Torakka":
        return 'Hävisit!'
    elif ase_pelaaja == "Torakka" and ase_tietokone == "Jalka":
        return 'Hävisit!'
    else:
        return 'Voitit!'

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
            ase_tietokone = aseen_arvonta()
            tulosta_ase(ase_pelaaja, ase_tietokone)
            tulos = kuka_voitti(ase_pelaaja, ase_tietokone)
            print(tulos)
            if tulos == "Voitit!":
                voitto = voitto+1
            elif tulos == "Tasapeli!":
                tasatulos = tasatulos+1
            kierros = kierros + 1
    nayta_voitot(kierros, voitto, tasatulos)