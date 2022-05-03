class Portfel:
    def __init__(self, saldo = 0):
        self.saldo = saldo

    def setInitialValue(self,value):
        self.saldo = value

    def add(self, value):
        self.saldo += value

    def spend(self, value):
        self.saldo -= value
