

class Battlefield:
    def __init__(self):
        self.battlefields = ['Desert', 'Valley', 'Jungle', 'Milwaukee']

        print(self.battlefields)
        self.user_input = input("Select battlefield from list: ")

        while self.user_input not in self.battlefields:
            self.user_input = input("Try Again: ")


    def __repr__(self):
        return f'\nBattlefield: {self.user_input}\n'
