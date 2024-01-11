class Child:
    def __init__(self, name, surname, age, geo):
        self.name = name
        self.surname = surname
        self.age = age
        self.geo = geo

    def __str__(self):
        return "{} {}, {}, {}".format(self.name, self.surname, self.age, self.geo)