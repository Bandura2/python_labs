"""python package with manager"""


class SetManager:
    """
    Create class SetManager with magic methods
    """

    def __init__(self, regular_manager):
        self.regular_manager = regular_manager
        self.index = 0
        self.index_ = 0

    def __len__(self):
        return sum(len(insect.edible_food_set) for insect in self.regular_manager)

    def __getitem__(self, index__):
        for insect in self.regular_manager:
            if index__ < len(insect.edible_food_set):
                return list(insect.edible_food_set)[index__]
            index__ -= len(insect.edible_food_set)
        raise IndexError

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.regular_manager):
            raise StopIteration

        insect = self.regular_manager[self.index]
        list_set = list(insect.edible_food_set)
        if self.index_ >= len(list_set):
            self.index += 1
            self.index_ = 0
            return self.__next__()

        item = list_set[self.index_]
        self.index_ += 1
        return item
