class car:
    # class variable
    wheels = 4

    def __init__(self):
        # instance variable
        self.mile = 10
        self.comp = "BMW"


# c1 and c2 object
c1 = car()
c2 = car()

# changing the value of instance variable mile
c1.mile = 8

# changing the value of class variable wheels
car.wheels = 5

print(c1.mile, c1.comp, c1.wheels)
print(c2.mile, c2.comp, c2.wheels)
