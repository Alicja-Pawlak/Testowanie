class Game:
    def __init__(self, throws):
        self.throws = throws

    def sumPoints(self):
        return sum(self.throws)

    def firstStrike(self):
        if self.throws[0] == 10:
            if len(self.throws) == 3:
                print("Strike + 2 rzuty = koniec rundy")
                return sum(self.throws)
    
    def spare(self):
        if self.throws[0] + self.throws[1] == 10:
            if len(self.throws) == 3:
                print("Spare + 1 rzut = koniec rundy")
                return sum(self.throws)