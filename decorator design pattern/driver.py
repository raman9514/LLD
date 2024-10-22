from modules.pizza import *

# pizza = VegPizza()
# pizza = ExtraVegii(ExtraCheese(pizza))
# print(pizza.get_price())
# print(pizza.get_description())

# print(pizza.get_bill())


class PizzaHouse:
    def __init__(self):
        self.pizza = None

    def main_menu(self):
        print(
            '''
            ------------------------------------------------
                               PIZZA HOUSE
            ------------------------------------------------
            ------------------------------------------------
            1. Veg Pizza
            2. Non Veg Pizza    
            ------------------------------------------------         
            '''
        )
        input('Choose : ')
        self.pizza = VegPizza()
        self.menu_extra()

    def menu_extra(self):
        print('''
              -----------------------------------------
              -----------------------------------------
              1. Add Extra Cheese
              2. Add Extra VEG
              3. Continue and Place Order
              ''')
        option = int(input('Choose : '))
        if option == 1:
            self.pizza = ExtraCheese(self.pizza)
            self.menu_extra()
        elif option == 2:
            self.pizza = ExtraVegii(self.pizza)
            self.menu_extra()
        else:
            print('---------------------------------')
            print('        ORDER SUCCESSFULL        ')
            print('---------------------------------')
            print(self.pizza.get_bill())
            print(f'({self.pizza.get_description()})')
            print('---------------------------------')
            print(f'TOTAL         {self.pizza.get_price()}')
            print('---------------------------------')

    def resolve_main_menue(self, option):
        self.pizza = VegPizza()
        self.menu_extra()

    def run(self):
        print(self.main_menu())


pizzahouse = PizzaHouse()
pizzahouse.run()
