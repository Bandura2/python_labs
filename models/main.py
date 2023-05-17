"""python package with models"""


class Insect:
    """
    Create class Insect with fields: name, number_of_legs, has_wings,
     is_dangerous, is_sleeping and methods: is_poisonous, hibernate, wake_up
    """
    __instance = None

    # pylint: disable= too-many-arguments
    def __init__(self, name="", number_of_legs=0,
                 has_wings=False, is_dangerous=False, is_sleeping=False):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping

    def is_poisonous(self) -> bool:
        """Method return field is_dangerous"""
        return self.is_dangerous

    def hibernate(self) -> None:
        """Method assigns a variable is_sleeping True"""
        self.is_sleeping = True

    def wake_up(self) -> None:
        """Method assigns a variable is_sleeping False"""
        self.is_sleeping = False

    @staticmethod
    def get_instance():
        """Method return singleton field instance"""
        if not Insect.__instance:
            Insect.__instance = Insect()
        return Insect.__instance

    def __str__(self):
        return f"Insect(name={self.name}, number_of_legs={self.number_of_legs}," \
               f" has_wings={self.has_wings}, is_dangerous={self.is_dangerous}," \
               f" is_sleeping={self.is_sleeping})"

    @staticmethod
    def count_of_element(*args) -> int:
        """Method counts int in list"""
        count = 0

        for element in args:
            count += 1

        print(f"count = {count}")
        return count


if __name__ == '__main__':
    list_insects = [
        Insect("Mantis", 6, False, True, False),
        Insect(),
        Insect.get_instance(),
        Insect.get_instance()
    ]

    for insect in list_insects:
        print(insect)

    test_list = []

    for i in range(10):
        test_list.append(i)

    print(Insect.count_of_element(1, 2, 3))
    print(Insect.count_of_element(*test_list))
