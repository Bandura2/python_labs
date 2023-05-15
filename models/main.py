class Insect:
    instance = None

    def __init__(self, name="", number_of_legs=0,
                 has_wings=False, is_dangerous=False, is_sleeping=False):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping

    def is_poisonous(self) -> bool:
        return self.is_dangerous

    def hibernate(self) -> None:
        self.is_sleeping = True

    def wake_up(self) -> None:
        self.is_sleeping = False

    @staticmethod
    def get_instance():
        if not Insect.instance:
            Insect.instance = Insect()
        return Insect.instance

    def __str__(self):
        return f"Insect(name={self.name}, number_of_legs={self.number_of_legs}," \
               f" has_wings={self.has_wings}, is_dangerous={self.is_dangerous}," \
               f" is_sleeping={self.is_sleeping})"


if __name__ == '__main__':
    array_insects = [Insect("Mantis", 6, False, True, False),
                     Insect(),
                     Insect.get_instance(),
                     Insect.get_instance()]

    for insect in array_insects:
        print(insect)
