"""
Sa se scrie un program care tine evidenta angajatilor dintr-o companie.
Informatiile pe care trebuie sa le retinem despre un angajat sunt urmatoarele:
	1) CNP
	2) Nume
	3) Prenume
	4) Varsta
	5) Salar
	6) Departament
	7) Senioritate (junior, mid, senior)

Programul trebuie sa dispuna de un meniu care ne permite sa efectuam urmatoarele actiuni:
	1) Adaugare angajat
	2) Cautare angajat (dupa CNP)
	3) Modificare date angajat (dupa CNP)
	4) Stergere angajat (dupa CNP)
	5) Afisare angajati
	6) Calcul cost total salarii companie
	7) Calcul cost total salarii departament
	8) Calcul fluturas salar angajat (dupa CNP) (CAS - 10% din brut, CASS - 25% din brut, Impozit - 10% din ce a ramas)
	9) Afisarea angajatilor pe baza senioritatii
	10) Afisarea angajatilor pe baza departamentului
	11) Iesire

Informatiile despre angajati trebuie sa fie stocate intr-un fisier astfel incat sa poata fi accesate si modificate ulterior.

Criterii notare:
    - 0.5p  documentare cod (docstrings, comentarii)
    - 0.5p  type hints
    - 1p    modularitate (impartirea codului in functii, module, etc)
    - 1p    naming conventions (denumire variabile, denumire functii, etc)
    - 1p    error handling (try-except, validare integritate date *, etc)
    - 1p    salvarea datelor intr-un fisier (citire/scriere)
    - 0.5p  adaugare angajati
    - 0.5p  afisare angajati
    - 0.5p  cautare angajat
    - 0.5p  modificare date angajat
    - 0.5p  stergere angajat
    - 0.5p  calcul cost total salarii companie
    - 0.5p  calcul cost total salarii departament
    - 0.5p  calcul fluturas salarial
    - 0.5p  afisarea angajatilor pe baza senioritatii
    - 0.5p  afisarea angajatilor pe baza departamentului

	* Verificare integriatate date (parametrii introdusi sa fie corespunzatori)
		- Exemple:
			- CNP sa fie de lungime corespunzatoare si sa contina doar cifre
			- Varsta sa fie mai mare de 18 ani
			- Salarul sa fie mai mare decat minimul pe economie (4050)
			- etc

Termen limita: Sambata 6 martie 2026 ora 23:59
Lucrul in echipa pentru acest proiect este permis, dar fiecare membru trebuie sa predea o versiune individuala a proiectului,
care sa fie diferita de cea a colegilor sai (de exemplu, prin adaugarea unor functionalitati suplimentare sau prin implementarea intr-un mod diferit a functionalitatilor cerute).
Pentru persoanele care depasesc termenul limita se vor scadea cate 0.25p pentru fiecare zi de intarziere.
Maximul de zile de intarziere este de 14 zile, dupa care proiectul nu va mai fi acceptat, iar nota va fi 1.

"""

from typing import List, Dict
FISIER = "angajati.txt"

def incarca_angajati() -> List[Dict]:
    angajati = []
    try:
        with open(FISIER, "r") as f:
            for linie in f:
                date = linie.strip().split(";")
                if len(date) == 7:
                    try:
                        angajati.append({
                            "cnp": date[0],
                            "nume": date[1],
                            "prenume": date[2],
                            "varsta": int(date[3]),
                            "salar": int(date[4]),
                            "departament": date[5],
                            "senioritate": date[6]
                        })
                    except:
                        pass
    except FileNotFoundError:
        pass
    return angajati


def salveaza_angajati(lista: List[Dict]) -> None:
    f = open(FISIER, "w")
    for angajat in lista:
        linie = (
            angajat["cnp"] + ";" +
            angajat["nume"] + ";" +
            angajat["prenume"] + ";" +
            str(angajat["varsta"]) + ";" +
            str(angajat["salar"]) + ";" +
            angajat["departament"] + ";" +
            angajat["senioritate"] + "\n"
        )
        f.write(linie)
    f.close()


def adauga_angajat(lista: List[Dict]) -> None:
    cnp = input("CNP (13 cifre): ")
    if len(cnp) != 13:
        print("CNP invalid!")
        return

    nume = input("Nume: ")
    prenume = input("Prenume: ")

    try:
        varsta = int(input("Varsta: "))
        if varsta < 18:
            print("Varsta prea mica.")
            return
    except:
        print("Varsta gresita.")
        return

    try:
        salar = int(input("Salar: "))
        if salar < 4050:
            print("Salar prea mic.")
            return
    except:
        print("Salar invalid.")
        return

    departament = input("Departament: ")
    senioritate = input("Senioritate: ")

    lista.append({
        "cnp": cnp,
        "nume": nume,
        "prenume": prenume,
        "varsta": varsta,
        "salar": salar,
        "departament": departament,
        "senioritate": senioritate
    })

    salveaza_angajati(lista)
    print("Angajat adaugat.\n")


def cauta_angajat(lista: List[Dict]) -> Dict:
    cnp = input("CNP cautat: ")

    for angajat in lista:
        if angajat["cnp"] == cnp:
            print(angajat)
            return angajat

    print("Nu am gasit angajatul.")
    return None


def modifica_angajat(lista: List[Dict]) -> None:
    cnp = input("CNP angajat modificat: ")

    for angajat in lista:
        if angajat["cnp"] == cnp:
            print("Lasati gol")

            nou_nume = input("Nume nou: ")
            if nou_nume != "":
                angajat["nume"] = nou_nume

            nou_prenume = input("Prenume nou: ")
            if nou_prenume != "":
                angajat["prenume"] = nou_prenume

            varsta_noua = input("Varsta noua: ")
            if varsta_noua != "":
                angajat["varsta"] = varsta_noua

            salar_nou = input("Salar nou: ")
            if salar_nou != "":
                angajat["salar"] = salar_nou

            salveaza_angajati(lista)
            print("Date modificate.\n")
            return

    print("CNP inexistent.\n")


def sterge_angajat(lista: List[Dict]) -> None:
    cnp = input("CNP angajat: ")

    for angajat in lista:
        if angajat["cnp"] == cnp:
            lista.remove(angajat)
            salveaza_angajati(lista)
            print("Sters.\n")
            return

    print("Nu exista acest CNP.\n")


def afisare_angajati(lista: List[Dict]) -> None:
    for angajat in lista:
        print(angajat)
    print()


def cost_total(lista: List[Dict]) -> None:
    total = 0
    for angajat in lista:
        try:
            total += int(angajat["salar"])
        except:
            pass
    print("Cost total:", total, "\n")


def cost_departament(lista: List[Dict]) -> None:
    dep = input("Departament: ")
    total = 0

    for angajat in lista:
        if angajat["departament"] == dep:
            try:
                total += int(angajat["salar"])
            except:
                pass

    print("Cost departament:", total, "\n")


def fluturas(lista: List[Dict]) -> None:
    cnp = input("CNP: ")

    for angajat in lista:
        if angajat["cnp"] == cnp:
            try:
                brut = int(angajat["salar"])
            except:
                print("Eroare salar.\n")
                return

            cas = brut * 0.10
            cass = brut * 0.25
            imp = (brut - cas - cass) * 0.10
            net = brut - cas - cass - imp

            print("Brut:", brut)
            print("CAS:", cas)
            print("CASS:", cass)
            print("Impozit:", imp)
            print("Net:", net, "\n")
            return

    print("CNP invalid.\n")


def afisare_dupa_senioritate(lista: List[Dict]) -> None:
    s = input("Senioritate: ")
    for angajat in lista:
        if angajat["senioritate"] == s:
            print(angajat)
    print()


def afisare_dupa_departament(lista: List[Dict]) -> None:
    d = input("Departament: ")
    for angajat in lista:
        if angajat["departament"] == d:
            print(angajat)
    print()


def meniu():
    angajati = incarca_angajati()

    while True:
        print("=== MENIU ===")
        print("1) Adaugare angajat")
        print("2) Cautare angajat")
        print("3) Modificare date angajat")
        print("4) Stergere angajat")
        print("5) Afisare angajati")
        print("6) Cost total salarii")
        print("7) Cost pe departament")
        print("8) Fluturas salarial")
        print("9) Afisare dupa senioritate")
        print("10) Afisare dupa departament")
        print("11) Iesire")

        opt = input("Optiune: ")

        if opt == "1":
            adauga_angajat(angajati)
        elif opt == "2":
            cauta_angajat(angajati)
        elif opt == "3":
            modifica_angajat(angajati)
        elif opt == "4":
            sterge_angajat(angajati)
        elif opt == "5":
            afisare_angajati(angajati)
        elif opt == "6":
            cost_total(angajati)
        elif opt == "7":
            cost_departament(angajati)
        elif opt == "8":
            fluturas(angajati)
        elif opt == "9":
            afisare_dupa_senioritate(angajati)
        elif opt == "10":
            afisare_dupa_departament(angajati)
        elif opt == "11":
            break
        else:
            print("Optiune nevalida!\n")


meniu()





















