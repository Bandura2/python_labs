"""python package with exceptions"""


class FeedingNotEdibleFood(Exception):
    def __str__(self):
        return "This insect died"
