from appliances import Dishwasher
from appliances import Dryer
from appliances import Washer
from appliances import Refrigerator
from appliances import Coffeemaker
from appliances import Canopener

whirlpool_dishwasher = Dishwasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "gas")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = Coffeemaker("white")
mr_coffee.make_coffee()

can_master = Canopener("green")
can_master.open_can()

