"""python package with models"""
from models.main import AbstractClassInsect


class Butterfly(AbstractClassInsect):
    """
    Create class Butterfly, that inheritance from Insect
    and have fields: name, number_of_legs, has_wings,
    is_dangerous, is_sleeping and methods: is_poisonous, hibernate, wake_up
    """

    def can_inject_poison(self) -> bool:
        """Method return field is_dangerous"""
        return self.is_dangerous

    def survive_over_winter(self) -> bool:
        """Method return field is_sleeping"""
        return self.is_sleeping

    def __str__(self) -> str:
        return f"Butterfly(name={self.name}, number_of_legs={self.number_of_legs}," \
               f" has_wings={self.has_wings}, is_dangerous={self.is_dangerous}," \
               f" is_sleeping={self.is_sleeping})"
