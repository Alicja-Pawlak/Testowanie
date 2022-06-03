class Osoba:
    def __init__(self, kwota):
        self.kwota = kwota
    def podatek(self):
        if self.kwota in range(100,1000):
            return self.kwota*23/100
        else: 
            return "Wpisz kwotę między 100-1000"
    def netto(self):
        if self.kwota in range(100,1000):
            netto = self.kwota - self.kwota*23/100
            return netto
        else:
            return "Wpisz kwotę między 100-1000"
    def prog(self):
        if self.kwota in range(100,400):
            return "I prog"
        elif self.kwota in range(401,700):
            return "II prog"
        elif self.kwota in range(701,1000):
            return "III prog"
        else:
            return "Wpisz kwotę między 100-1000"