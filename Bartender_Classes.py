
class Bottle: 
    def __init__(self, flavor, percentage, type, name):
        self.flavor = flavor
    def print_flavor(self):
        print(self.flavor)


class Pump:
    def __init__(self,Port):
        self.Port = Port
    def start_pump(self, duration, ml):
        pass