from Observable.Iphone16 import *
from Observer.EmailAlertObserver import *

observable = IphoneObserver()

o1 = EmailAlertObserver(observable, 'raman9514@gmail.com')
o2 = EmailAlertObserver(observable, 'Pawan@11.in')

observable.subscribe(o1)
observable.subscribe(o2)
observable.setStockCount(10)
observable.setStockCount(4)
