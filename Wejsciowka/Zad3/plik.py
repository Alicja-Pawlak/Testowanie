class Plik:
    def stworzPlik(self):
        stworzonyPlik = open(f"plik.txt","w+")
        stworzonyPlik.write(f"1|Arsenal|Arteta\n")
        stworzonyPlik.write(f"2|Pogon Szczecin|Kosta\n")
        stworzonyPlik.write(f"3|Legia|Vuko\n")
        stworzonyPlik.write(f"4|Roma|brak\n")
        stworzonyPlik.close()