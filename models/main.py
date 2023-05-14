class Insect:
    instance = None

    def __init__(self, name="", number_of_legs=0,
                 has_wings=False, is_dangerous=False, is_sleeping=False):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping

    def is_poisonous(self):
        return self.is_dangerous

    def hibernate(self):
        self.is_sleeping = True

    def wake_up(self):
        self.is_sleeping = False

    @staticmethod
    def get_instance():
        if not Insect.instance:
            Insect.instance = Insect()
        return Insect.instance

    def __str__(self):
        return f"Insect(name={self.name}, numberOfLegs={self.number_of_legs}," \
               f" hasWings={self.has_wings}, isDangerous={self.is_dangerous}," \
               f" isSleeping={self.is_sleeping})"


array_insects = [Insect("Mantis", 6, False, True, False),
                 Insect(),
                 Insect.get_instance(),
                 Insect.get_instance()]

for insect in array_insects:
    print(insect.__str__())
