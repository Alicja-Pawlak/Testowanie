class Plik:
    def __init__(self, klub1, klub2):
        self.klub1 = klub1
        self.klub2 = klub2
    def stworzPlik(self, fileName):
        stworzonyPlik = open(f"{fileName}"+".txt","w+")
        stworzonyPlik.write(f"{self.klub1}\n")
        stworzonyPlik.write(f"{self.klub2}\n")
        stworzonyPlik.close()
        