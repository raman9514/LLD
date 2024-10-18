

class IObservable:
    def __init__(self):
        self.subscriber = list()
        self.stockCount = 0

    def subscribe(self, subscriber):
        self.subscriber.append(subscriber)

    def setStockCount(self, count):
        if self.stockCount == 0:
            self.notify()

    def notify(self):
        for obj in self.subscriber:
            obj.update()
