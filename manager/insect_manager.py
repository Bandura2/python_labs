"""python package with manager"""
from models.butterfly import Butterfly
from models.hornet import Hornet
from models.main import AbstractClassInsect
from models.mantis import Mantis
from models.mosquito import Mosquito


class InsectManager:
    """
    Create class InsectManager with private field list_of_insects
    with getter.
    Manager have methods sdd_insect, find_all_dangerous
    and find_insects_that_have_num_of_legs_more_than
    """

    def __init__(self):
        self.__list_of_insects = []

    def add_insect(self, insect) -> None:
        """Method add insect to list that are field"""
        self.__list_of_insects.append(insect)

    def find_all_dangerous(self) -> [AbstractClassInsect]:
        """Method return list of insects whose field is_dangerous is True"""
        return list(filter(lambda insect: insect.is_dangerous is True, self.__list_of_insects))

    def find_insects_that_have_legs_more_than(self, num_of_leg) -> [AbstractClassInsect]:
        """
        Method return list of insects whose field number_of_legs is more than
        parameter num_of_leg
        """
        # pylint: disable= line-too-long
        return list(filter(lambda insect: insect.number_of_legs > num_of_leg, self.__list_of_insects))


if __name__ == '__main__':
    manager = InsectManager()

    manager.add_insect(Mosquito("Vasa", 4, True, False, False))
    manager.add_insect(Mosquito("Artur", 6, True, True, True))
    manager.add_insect(Hornet("Loky", 2, True, False, True))
    manager.add_insect(Hornet("Overlook", 4, True, True, False))
    manager.add_insect(Butterfly("Name", 8, True, False, False))
    manager.add_insect(Butterfly("Dinar", 6, True, False, True))
    manager.add_insect(Mantis("Olena", 8, False, True, False))
    manager.add_insect(Mantis("Zoro", 2, False, True, True))

    print("\nPrint all insects that have more than 4 leg")
    for element in manager.find_insects_that_have_legs_more_than(4):
        print(element)

    print("\nPrint all dangerous insects")
    for element in manager.find_all_dangerous():
        print(element)
