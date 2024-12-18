class FRUITS:
    def eat(self):
        print("we can eat fruits")
class ORANGE(FRUITS):
    pass
class APPLE(FRUITS):
    def eat(self):
        print("Apple is sweet")
org1=ORANGE()
app1=APPLE()
org1.eat()
app1.eat()
