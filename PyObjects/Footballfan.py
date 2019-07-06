from partyAnimal import PartyAnimal
class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
            self.points = self.points +9
            self.party()
            print('Tounch down:', self.name,'points', self.points)

an = FootballFan('Jim')

an.party()
an.touchdown()
