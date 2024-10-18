from abc import ABC, abstractmethod
class EnemyShip(ABC):
    name = ''
    damage = 0
    @abstractmethod
    def setName(self,name):
        pass
    
    @abstractmethod
    def getName(self):
        pass
    def __name__(self):
        return self.name

class UFOEnemeyShip(EnemyShip):
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

class RocketEnemyShip(EnemyShip):
    def setName(self,name):
        self.name = name
    
    def getName(self):
        return self.name

class JetEnemyShip(EnemyShip):
    def setName(self,name):
        self.name = name

class EnemyShipFactory:
    @staticmethod
    def create_ship(type):
        if type == 'UFO':
            return UFOEnemeyShip()
        elif type == 'ROCKET':
            return RocketEnemyShip()
        elif type == 'JetEnemyShip':
            return JetEnemyShip()

if __name__ == '__main__':
    ship = EnemyShipFactory.create_ship('UFO')
    ship.name = 'JL049'
    print(type(ship))
    print(ship.getName())
    
        
    