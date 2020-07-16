from appliances import Appliance

class Dishwasher(Appliance):

    def __init__(self, color):
        super().__init__(color)

    def wash_dishes(self):
        return("grind, grind, clunk. Time to call the repair person")
