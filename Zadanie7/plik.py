class Plik:
    def __init__(self, klub1, klub2, fileName):
        self.klub1 = klub1
        self.klub2 = klub2
        self.fileName = fileName
    def stworzPlik(self):
        stworzonyPlik = open(f"{self.fileName}" + ".txt","w+")
        stworzonyPlik.write(f"{self.klub1}\n")
        stworzonyPlik.write(f"{self.klub2}\n")
        stworzonyPlik.close()
        