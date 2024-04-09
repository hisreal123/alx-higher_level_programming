#!/usr/bin/python3

class Ocean:
    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age

    def __str__(self):
        return "The creature type is {} and the age is {}".format(self.name, self.age)

    def __repr__(self):
        return "Ocean \'{}\',{}".format(self.name, self.age)


c = Ocean("Shark", 30)

if __name__ == "__main__":
    print(str(c))
    print(repr(c))
