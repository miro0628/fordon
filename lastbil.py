import fordon
class Lastbil:

    #constructor
    def __init__(self, fabrikat, color, flakvolym):
        self.flakvolym = flakvolym
        self.fabrikat = fabrikat
        self.color = color


    #metoder
    def set_flakvolym(self, flakvolym):
        self.flakvolym = flakvolym

    def get_flakvolym(self):
        return self.flakvolym

    def print_fordon(self):
        print(self.fabrikat +" Färg: " + self.color + " flakvolym=" + str (self.flakvolym))