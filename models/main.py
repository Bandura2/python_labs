"""python package with models"""
from abc import ABC, abstractmethod


class AbstractClassInsect(ABC):
    """
    Create abstract class Insect with fields: name, number_of_legs, has_wings,
    is_dangerous, is_sleeping and methods: is_poisonous, hibernate, wake_up
    """
    __instance = None

    # pylint: disable= too-many-arguments
    def __init__(self, name="", number_of_legs=0, has_wings=False,
                 is_dangerous=False, is_sleeping=False, favorite_food_set=None):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping
        self.favorite_food_set = favorite_food_set or set()

    def is_poisonous(self):
        """
        :return: field is_dangerous
        """
        return self.is_dangerous

    def hibernate(self):
        """
        Method assigns a variable is_sleeping True
        """
        self.is_sleeping = True

    def wake_up(self):
        """
        Method assigns a variable is_sleeping False
        """
        self.is_sleeping = False

    @staticmethod
    def get_instance():
        """
        :return: singleton field instance
        """
        if not AbstractClassInsect.__instance:
            AbstractClassInsect.__instance = AbstractClassInsect()
        return AbstractClassInsect.__instance

    def __str__(self):
        return f"Insect(name={self.name}, number_of_legs={self.number_of_legs}," \
               f" has_wings={self.has_wings}, is_dangerous={self.is_dangerous}," \
               f" is_sleeping={self.is_sleeping})"

    @staticmethod
    def count_of_element(*args):
        """
        Method counts how many elements are passed to it
        :param args: parameter allows you to pass any number of positional arguments to function
        :return: count of element that passed to it
        """
        count = 0

        for _ in args:
            count += 1

        print(f"count = {count}")
        return count

    # pylint: disable= missing-function-docstring
    @abstractmethod
    def can_inject_poison(self):
        pass

    # pylint: disable= missing-function-docstring
    @abstractmethod
    def survive_over_winter(self):
        pass

    def get_fields_by_type(self, type_field):
        """
        Method create dictionary with all attributes and values of the object,
        filtered by the specified value type
        :param type_field: type fields to filter
        :return: a dictionary with all attributes and values of the object,
        filtered by the specified value type
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, type_field)}

    def __iter__(self):
        return self.favorite_food_set
