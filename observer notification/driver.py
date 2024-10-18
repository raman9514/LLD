# from .Observable.Iphone16 import *
# from .Observer.EmailAlertObserver import *


class IphoneObserver:
    def __init__(self):
        self.subscriber = list()
        self.stockCount = 0

    def subscribe(self, subscriber):
        self.subscriber.append(subscriber)

    def setStockCount(self, count):
        if self.stockCount == 0:
            self.notify()
        self.stockCount = count

    def notify(self):
        for obj in self.subscriber:
            obj.update()


class EmailAlertObserver:
    def __init__(self, observable, email):
        self.email = email
        self.observable = observable

    def update(self):
        print('sent the mail to ', self.email)


observable = IphoneObserver()

o1 = EmailAlertObserver(observable, 'raman9514@gmail.com')
o2 = EmailAlertObserver(observable, 'Pawan@11.in')

observable.subscribe(o1)
observable.subscribe(o2)
observable.setStockCount(10)
