class EmailAlertObserver:
    def __init__(self, observable, email):
        self.email = email
        self.observable = observable

    def update(self):
        print('sent the mail to ', self.email)
