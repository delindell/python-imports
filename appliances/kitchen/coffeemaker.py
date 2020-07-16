from appliances import Appliance

class Coffeemaker(Appliance):

    def __init__(self, color):
        super().__init__(color)

    def make_coffee(self):
        print("gurgle, gurgle. Ding. Your drug of choice is piping hot and ready!")
