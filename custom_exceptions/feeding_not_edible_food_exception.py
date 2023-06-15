"""python package with exceptions"""


class FeedingNotEdibleFood(Exception):
    """
    Class exception that raise when you feed insect not edible food
    """
    def __str__(self):
        return "<class 'FeedingNotEdibleFood'>\nmassage: This insect died"
