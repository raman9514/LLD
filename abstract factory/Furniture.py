from abc import ABC,abstractclassmethod



class ModernChair:
    def __str__(self):
        return 'Modern Chair'

class ModernSofa:
    def __str__(self):
        return 'Modern Sofa'

class ModernTable:
    def __str__(self):
        return 'Modern Table'

class TraditionalChair:
    def __str__(self):
        return 'Traditional Chair'


class TraditionalSofa:
    def __str__(self):
        return 'Traditional Sofa'


class TraditionalTable:
    def __str__(self):
        return 'Traditional Table'


class FurnitureFactory(ABC):
    @abstractclassmethod
    def create_chair():
        pass
    @abstractclassmethod
    def create_sofa():
        pass
    @abstractclassmethod
    def create_table():
        pass
    
    @staticmethod
    def create_furniture(type='Modern'):
        if type == 'Modern':
            return ModernFactory()
        elif type == 'Traditional':
            return TraditionalFactory()
    

class ModernFactory(FurnitureFactory):
    @staticmethod
    def create_chair():
        return ModernChair()
    @staticmethod
    def create_sofa():
        return ModernSofa()
    @staticmethod
    def create_table():
        return ModernTable()

class TraditionalFactory(FurnitureFactory):
    @staticmethod
    def create_chair():
        return TraditionalChair()
    @staticmethod
    def create_sofa():
        return TraditionalSofa()
    @staticmethod
    def create_table():
        return TraditionalTable()

if __name__ == '__main__':
    furniture1 = FurnitureFactory.create_furniture('Modern')
    sofa = furniture1.create_sofa()
    print(sofa)
    