class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie,stala):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie = wynagrodzenie
        self.stala = stala
    def email(imie,nazwisko):
        return (f"{imie}.{nazwisko}@testemail.com")
    def pelna_nazwa(imie, nazwisko):
        return (f"{imie} {nazwisko}")
    def podwyzka(wynagrodzenie,stala):
        return wynagrodzenie*stala
