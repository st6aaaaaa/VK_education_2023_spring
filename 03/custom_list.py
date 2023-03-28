class CustomList(list):

    def __add__(self, other):
        if len(self) == len(other):
            return CustomList([self[i] + other[i] for i in range(len(self))])
        if len(self) > len(other):
            return CustomList([self[i] + other[i] for i in range(len(other))]
                              + self[len(other):])
        return CustomList([self[i] + other[i] for i in range(len(self))] +
                          other[len(self):])

    def __radd__(self, array):
        return self.__add__(array)

    def __sub__(self, other):
        if len(self) == len(other):
            return CustomList([self[i] - other[i] for i in range(len(self))])
        if len(self) > len(other):
            return CustomList([self[i] - other[i] for i in range(len(other))] +
                              self[len(other):])
        return CustomList([self[i] - other[i] for i in range(len(self))] +
                          list(map(lambda x: -x, other[len(self):])))

    def __rsub__(self, array):
        return CustomList(array).__sub__(self)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return super().__str__() + " " + str(sum(self))
