import weakref
import time


class Something:
    def __init__(self, height=1, weight=2):
        self.height = height
        self.weight = weight


class SomethingSlots:
    __slots__ = ("height", "weight")

    def __init__(self, height=1, weight=2):
        self.height = height
        self.weight = weight


class SomethingWeak:
    def __init__(self, someclass):
        self.var = weakref.ref(someclass)


N = 100_000

startTime = time.time()
tmp1 = [Something(i) for i in range(N)]
endTime = time.time()
print('time of creation of ordinary class = ', endTime - startTime)

startTime = time.time()
tmp2 = [SomethingSlots(i) for i in range(N)]
endTime = time.time()
print('time of creation of class with "slots" = ', endTime - startTime)

startTime = time.time()
tmp3 = [SomethingWeak(i).var() for i in tmp1]
endTime = time.time()
print('time of creation of class with "weakref" = ', endTime - startTime, '\n')


startTime = time.time()
for i in range(N):
    tmp1[i].height += i
    tmp1[i].weight += i
endTime = time.time()
print('time of change of ordinary class = ', endTime - startTime)

startTime = time.time()
for i in range(N):
    tmp2[i].height += i
    tmp2[i].weight += i
endTime = time.time()
print('time of change of class with "slots" = ', endTime - startTime)

startTime = time.time()
for i in range(N):
    tmp3[i].height += i
    tmp3[i].weight += i
endTime = time.time()
print('time of change of class with "weakref" = ', endTime - startTime)
