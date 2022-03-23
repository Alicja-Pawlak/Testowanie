class Club:
    def __init__(self, club, trainer = None):
        self.club = club
        self.trainer = trainer
    def isTrainer(self):
        if(self.trainer != None):
            return True
        else:
            return False


