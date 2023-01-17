class Artikli:
    def __init__(self, naziv_proizvoda, bar_kod, osnovna_cena):
        self.naziv_proizvoda = naziv_proizvoda
        self.bar_kod = bar_kod
        self.osnovna_cena = osnovna_cena
    def cena(self):
        pdv = 0.20 * self.osnovna_cena
        return f"Iznos sa PDV-om je: {pdv + self.osnovna_cena}"
    def __str__(self):
        return f"Naziv proizvoda {self.naziv_proizvoda}, bar-kod: {self.bar_kod}, Osnovna cena: {self.osnovna_cena}, Porez: {self.cena() - self}"

class Vino(Artikli):
    def __init__(self, naziv_proizvoda, bar_kod, osnovna_cena):
        super().__init__(naziv_proizvoda, bar_kod, osnovna_cena)
    def cena(self):
        self.porez = 1.20
        self.dodatan_prez = 1.10
        return f"Cena iznosi: {self.osnovna_cena * self.porez * self.dodatan_prez}"


class Cokolada(Artikli):
    def __init__(self, naziv_proizvoda, bar_kod, osnovna_cena):
        super().__init__(naziv_proizvoda, bar_kod, osnovna_cena)
    def cena(self):
        self.porez = 1.20
        return f"Cena iznosi: {self.osnovna_cena * self.porez}"

miki = Artikli("aaa", 2516, 80)
print(miki.cena())
sangrija = Vino("Sangrija", 556, 500)
print(sangrija.cena())

milka = Cokolada("Milka nugat", 685, 400)
print(milka.cena())