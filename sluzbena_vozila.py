# -*- coding: utf-8 -*-

class SluzbenaVozila:
    def __init__(self, znamka, model, stevilo_kilometrov, datum_zadnjega_servisa):
        self.znamka = znamka
        self.model = model
        self.stevilo_kilometrov = stevilo_kilometrov
        self.datum_zadnjega_servisa = datum_zadnjega_servisa

    def izpis_vozila(self):
        return self.znamka + " " + self.model

    def dodaj_km(self, novi_km):
        self.stevilo_kilometrov += novi_km

    def posodobi_datum_servisa(self, nov_datum):
        self.datum_zadnjega_servisa = nov_datum


def vsa_vozila(vozila):
    for x, y in enumerate(vozila):
        print "Številka: " + str(x)
        print y.izpis_vozila()
        print y.stevilo_kilometrov
        print y.datum_zadnjega_servisa
        print ""


def dodaj_novo_vozilo(vozila):
    znamka = raw_input("Vpišite znamko vozila: ")
    model = raw_input("Vpišite model vozila: ")
    stevilo_kilometrov = raw_input("Vpišite število prevoženih km: ")
    datum_zadnjega_servisa = raw_input("Vpišite datum zadnjega servisa: ")

    novo = SluzbenaVozila(znamka=znamka, model=model, stevilo_kilometrov=stevilo_kilometrov, datum_zadnjega_servisa=datum_zadnjega_servisa)
    vozila.append(novo)

    print ""
    print "Uspešno ste dodali: %s s prevoženimi: %s km in datum zadnjega servisa: %s" % (novo.izpis_vozila(), stevilo_kilometrov, datum_zadnjega_servisa)


def izberi_vozilo(vozila):
    print "Izberite številko vozila, ki bi ga želeli spremeniti"
    print ""
    vsa_vozila(vozila)
    print ""
    izbira = raw_input("Napišite številko vozila: ")
    return vozila[int(izbira)]


def uredi_km(vozila):
    sel_vozila = izberi_vozilo(vozila)

    print "Izbrali ste: %s %s" %(sel_vozila.znamka, sel_vozila.model)
    print ""

    novi_kilometri = raw_input("Dodajte nove km: ")
    print ""

    novi_kilometri = novi_kilometri.replace(",", ".")
    novi_km = (novi_kilometri)

    sel_vozila.dodaj_km(novi_km)
    print "Novi kilometri: %s za vozilo %s %s." % (sel_vozila.stevilo_kilometrov, sel_vozila.znamka, sel_vozila.model)


def spremeni_datum_servisa(vozila):
    sel_vozila = izberi_vozilo(vozila)

    print "Izbrali ste: %s %s, datum zadnjega servisa: %s." %(sel_vozila.znamka, sel_vozila.model, sel_vozila.datum_zadnjega_servisa)
    print ""
    nov_datum_servisa = raw_input("Vpišite nov datum zadnjega servisa: ")
    print ""
    sel_vozila.posodobi_datum_servisa(nov_datum=nov_datum_servisa)
    print "Datum je posodobljen. Nov datum za %s %s je %s" % (sel_vozila.znamka, sel_vozila.model, sel_vozila.datum_zadnjega_servisa)


def shrani(vozila):
    with open("vozila.txt", "w") as vozila_datoteka:
        for vozilo in vozila:
            vozila_datoteka.write("%s,%s,%s,%s\n" % (vozilo.znamka, vozilo.model, vozilo.stevilo_kilometrov, vozilo.datum_zadnjega_servisa))

def main():
    print "Dobrodošli v programu za upravljanje s službenimi vozili."


    vw = SluzbenaVozila(znamka="VW", model="Golf", stevilo_kilometrov="55.670", datum_zadnjega_servisa="1.5.2016")
    audi = SluzbenaVozila(znamka="AUDI", model="A4", stevilo_kilometrov="70.847", datum_zadnjega_servisa="3.9.2016")
    bmw = SluzbenaVozila(znamka="BMW", model="Serija 5", stevilo_kilometrov="45.000", datum_zadnjega_servisa="25.11.2016")
    vozila = [vw, audi, bmw]

    while True:
        print ""
        print "Prosim izberite eno od možnosti: "
        print "a) Ogled seznama vozil"
        print "b) Dodati novo vozilo"
        print "c) Uredi število prevoženih km"
        print "d) Spremeni datum zadnjega servisa"
        print "e) Zapusti program"
        print ""

        izbira = raw_input("Vpišite svojo izbiro (a, b, c, d, e): ")
        print ""

        if izbira.lower() == "a":
            vsa_vozila(vozila)
        elif izbira.lower() == "b":
            dodaj_novo_vozilo(vozila)
        elif izbira.lower() == "c":
            uredi_km(vozila)
        elif izbira.lower() == "d":
            spremeni_datum_servisa(vozila)
        elif izbira.lower() == "e":
            print "Hvala, ker ste uporabljali naš program. Nasvidenje!"
            shrani(vozila)
            break

if __name__ == '__main__':
    main()