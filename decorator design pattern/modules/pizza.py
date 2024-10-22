from abc import abstractmethod, ABC


class IPizza(ABC):
    @abstractmethod
    def get_description():
        pass

    @abstractmethod
    def get_price():
        pass

    @abstractmethod
    def get_bill():
        pass


class VegPizza(IPizza):
    def __init__(self):
        self.__description = 'Veg Pizza'
        self.__price: int = 30

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_bill(self):
        return f"{self.__description} : {self.__price}"


class PizzaDecorator(IPizza):
    def __init__(self, pizza, description='', price=0):
        self.__pizza: IPizza = pizza
        self.__description = description
        self.__price: int = price

    def get_description(self):
        return self.__pizza.get_description() + ' with ' + self.__description

    def get_price(self):
        return self.__pizza.get_price() + self.__price

    def get_bill(self):
        return self.__pizza.get_bill() + '\n' + f"{self.__description} : {self.__price}"


class ExtraCheese(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(
            pizza=pizza,
            description='Extra 20G Cheese',
            price=40)


class ExtraVegii(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza=pizza,
                         description='Exta Vegii',
                         price=35)


class CheeseBurst(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza,
                         description='Cheese Burst',
                         price=75)
