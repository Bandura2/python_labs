"""python package with manager"""

from decorators.log_method_call import log_method_call
from decorators.run_pylint import run_pylint
from models.butterfly import Butterfly
from models.hornet import Hornet
from models.mantis import Mantis
from models.mosquito import Mosquito
from manager.set_insect_manager import SetManager


class RegularInsectManager:
    """
    Create class InsectManager with private field list_of_insects.
    Manager have methods sdd_insect, find_all_dangerous
    and find_insects_that_have_num_of_legs_more_than
    """

    # @run_pylint
    def __init__(self):
        self.__list_of_insects = []

    def add_insect(self, insect):
        """
        Method add insect to list that are field
        :param insect: object insect that need to add to list
        """
        self.__list_of_insects.append(insect)

    @log_method_call
    def find_all_dangerous(self):
        """
        Method find all insects that dangerous
        :return: list of insects whose field is_dangerous is True
        """
        return list(filter(lambda insect: insect.is_dangerous, self.__list_of_insects))

    @run_pylint
    def find_insects_that_have_legs_more_than(self, num_of_leg):
        """
        Method find all insects that have leg more than num_of_leg
        :param num_of_leg: field used for find
        :return: list of insects whose field number_of_legs is more than
        parameter num_of_leg
        """

        # pylint: disable= line-too-long
        return list(filter(lambda insect: insect.number_of_legs > num_of_leg, self.__list_of_insects))

    def __len__(self):
        return len(self.__list_of_insects)

    def __getitem__(self, index):
        return self.__list_of_insects[index]

    def __iter__(self):
        return iter(self.__list_of_insects)

    def get_list_with_results_can_inject_poison(self):
        """
        Method create list with results working methods can_inject_poison
        :return: list of results from working the can_inject_poison method for insects
        """
        return [insect.can_inject_poison() for insect in self.__list_of_insects]

    def get_insects_with_index(self):
        """
        Method create list with index of insect and insect
        :return: list insects with it index
        """
        return [f'{index}: {insect}' for index, insect in enumerate(self.__list_of_insects)]

    def get_dictionary_with_insect_that_can_inject_poison(self):
        """
        Method create list with insects and bool fields results method can_inject_poison
        :return: list insects with results working methods can_inject_poison
        """
        results_first_method = self.get_list_with_results_can_inject_poison()
        # pylint: disable= line-too-long
        return [f'{insect}: {result}' for insect, result in zip(self.__list_of_insects, results_first_method)]

    @log_method_call
    def check_condition(self, condition):
        """
        Check if all insects satisfy condition and if any insect satisfies condition
        :param condition:
        :return: dictionary with keys "all" and "any" and corresponding boolean values
        """
        all_satisfy = all(condition(insect) for insect in self.__list_of_insects)
        any_satisfy = any(condition(insect) for insect in self.__list_of_insects)
        return {"all": all_satisfy, "any": any_satisfy}


if __name__ == '__main__':
    manager = RegularInsectManager()

    manager.add_insect(Mosquito("Vasa", 4, True, False, False, {"blood1", "plant nectar1"}))
    manager.add_insect(Mosquito("Artur", 6, True, True, True, {"blood2", "plant nectar2"}))
    manager.add_insect(Hornet("Loky", 2, True, False, True, {"bees1", "tree leaves1"}))
    manager.add_insect(Hornet("Overlook", 4, True, True, False, {"bees2", "tree leaves2"}))
    manager.add_insect(Butterfly("Name", 8, True, False, False, {"nectar1", "fruit1"}))
    manager.add_insect(Butterfly("Dinar", 6, True, False, True, {"nectar2", "fruit2"}))
    manager.add_insect(Mantis("Olena", 8, False, True, False, {"live insects1", "more insects1"}))
    manager.add_insect(Mantis("Zoro", 2, False, True, True, {"live insects2", "more insects2"}))

    set_manager = SetManager(manager)
    #
    # print("\n----------------------------Prints for regular manager----------------------------")
    #
    # print("\nPrint all insects that have more than 4 leg")
    # for element in manager.find_insects_that_have_legs_more_than(4):
    #     print(element)
    #
    # print("\nPrint all dangerous insects")
    # for element in manager.find_all_dangerous():
    #     print(element)
    #
    # print("\nPrint list of results method can_inject_poison()")
    # for element in manager.get_list_with_results_can_inject_poison():
    #     print(element)
    #
    # print("\nPrint vocabulary {num_insect: object_insect}")
    # for element in manager.get_insects_with_index():
    #     print(element)
    #
    # print("\nPrint vocabulary {object_insect: result_method_can_inject_poison}")
    # for element in manager.get_dictionary_with_insect_that_can_inject_poison():
    #     print(element)
    #
    # print("\nPrint all str fields with manager")
    # for element in manager:
    #     print(element.get_fields_by_type(str))
    #
    # results_check_condition = manager.check_condition(lambda insect: insect.number_of_legs > 4)
    #
    # print("\nPrint bool are all insect have more than 4 leg")
    # print(results_check_condition["all"])
    # print("Print bool is any insect have more than 4 leg")
    # print(results_check_condition['any'])
    #
    # print("\n----------------------------Prints for set manager----------------------------")
    #
    # print("\nPrint count of food for all insect")
    # print(len(set_manager))
    #
    # print("\nPrint food for all insect in manager")
    # food = iter(set_manager)
    # NUMBER_FOOD = 0
    # for _ in range(len(set_manager)):
    #     print(f"{NUMBER_FOOD} {next(food)}")
    #     NUMBER_FOOD += 1
    #
    # print("\nPrint food number 10")
    # print(set_manager[10])

    mantis = Mantis("NAME", 4, False, True, False, {"insects", "more"})
    mantis.eat("orange")
