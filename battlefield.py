

class Battlefield:
    def __init__(self):
        self.battlefields = ['Desert', 'Valley', 'Jungle', 'Milwaukee']

        print(f'Battlefields: {self.battlefields}')
        self.user_input = input("Select battlefield from list: ")
        option_list = self.battlefields.copy()
        lower = []
        upper = []
        for options in option_list:
            lower.append(options.lower())
            upper.append(options.upper())

        while self.user_input not in self.battlefields and self.user_input not in lower and self.user_input not in upper:
            self.user_input = input("Try Again: ")
        else:
            self.user_input = self.user_input.capitalize()

    def __repr__(self):
        return f'\nBattlefield: {self.user_input}\n'
