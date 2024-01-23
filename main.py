class Kniha:
    nazov = None
    autor = None
    isbn = None
    rok_vydania = None
    dostupna = True

    def __init__(self, nazov, autor, isbn, rok_vydania, dostupna=True):
        self.nazov = nazov
        self.autor = autor
        self.isbn = isbn
        self.rok_vydania = rok_vydania
        self.dostupna = dostupna

    def __repr__(self):
        return f"Kniha s nazvom {self.nazov} od autora {self.autor}, isbn {self.isbn}, rok_vydania {self.rok_vydania}, {'dostupna' if self.dostupna else 'nedostupna'}"

    def vypozicat(self):
        if self.dostupna:
            self.dostupna = False
        else:
            raise Exception("Kniha nedostupna")

    def vratit(self):
        self.dostupna = True


class Kniznica:
    zoznam_knih = []

    def __init__(self, zoznam_knih=[]):
        self.zoznam_knih = zoznam_knih

    def pridat_knihu(self, kniha):
        self.zoznam_knih.append(kniha)

    def hladat_knihu(self, nazov):
        for kniha in self.zoznam_knih:
            if kniha.nazov == nazov:
                return kniha

    def hladat_knihu_podla_isbn(self, isbn):
        for kniha in self.zoznam_knih:
            if kniha.isbn == isbn:
                return kniha

    def vypozicat_knihu(self, isbn):
        kniha = self.hladat_knihu_podla_isbn(isbn)
        kniha.vypozicat()

    def zoznam_dostupnych_knih(self):
        dostupne_knihy = filter(lambda kniha: kniha.dostupna, self.zoznam_knih)
        for kniha in dostupne_knihy:
            print(kniha.nazov)


kniha1 = Kniha("Harry Potter", "Rowling", 123, 2010)
kniha2 = Kniha("Pan Prstenov", "Tolkien", 321, 2003)
kniha3 = Kniha("Daka Kniha", "Patrik", 222, 2010)

kniznica = Kniznica()
kniznica.pridat_knihu(kniha1)
kniznica.pridat_knihu(kniha2)
kniznica.pridat_knihu(kniha3)
kniznica.vypozicat_knihu(123)


print(kniha1)
print(kniha2)
print(kniha3)
print("--------------")
kniznica.zoznam_dostupnych_knih()

