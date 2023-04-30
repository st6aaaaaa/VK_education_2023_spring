import weakref
import cProfile
from memory_profiler import profile


class Something:
    def __init__(self, height=1, weight=2):
        self.height = height
        self.weight = weight

    def __repr__(self):
        return str(self.height) + ' ' + str(self.weight)


class SomethingSlots:
    __slots__ = ("height", "weight")

    def __init__(self, height=1, weight=2):
        self.height = height
        self.weight = weight

    def __repr__(self):
        return str(self.height) + ' ' + str(self.weight)


class SomethingWeak:
    def __init__(self, someclass):
        self.var = weakref.ref(someclass)


N = 100_000


@profile
def changeordinary(tmp):
    for i in range(N):
        tmp[i].height += i
        tmp[i].weight += i


@profile
def changewithslots(tmp):
    for i in range(N):
        tmp[i].height += i
        tmp[i].weight += i


@profile
def changewithrefs(tmp):
    for i in range(N):
        tmp[i].height += i
        tmp[i].weight += i


@profile
def creationordinary():
    tmp = [Something(i) for i in range(N)]


@profile
def creationwithslots():
    tmp = [SomethingSlots(i) for i in range(N)]


tmp1 = [Something(i) for i in range(N)]
tmp2 = [SomethingSlots(i) for i in range(N)]
tmp3 = [SomethingWeak(i).var() for i in tmp1]


profiler = cProfile.Profile()

profiler.enable()
creationordinary()
profiler.disable()

profiler.enable()
creationwithslots()
profiler.disable()

profiler.enable()
changeordinary(tmp1)
profiler.disable()

profiler.enable()
changewithslots(tmp2)
profiler.disable()

profiler.enable()
changewithrefs(tmp3)
profiler.disable()

