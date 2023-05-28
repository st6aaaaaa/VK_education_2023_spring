import cProfile
import pstats


diction = dict()


def profile_deco(func):

    def wrap(*args, **kwargs):
        tmp = cProfile.Profile()
        tmp.enable()
        res = func(*args, **kwargs)
        tmp.disable()

        stats = pstats.Stats(tmp)

        if func.__name__ in diction:
            diction[func.__name__].append(stats)
        else:
            diction[func.__name__] = [stats]

        return res

    def print_stat():

        combined_stats = None

        for stat in diction[func.__name__]:
            if combined_stats is None:
                combined_stats = stat
            else:
                combined_stats.add(stat)
        combined_stats.print_stats()

    wrap.print_stat = print_stat
    return wrap


@profile_deco
def add(tmp1, tmp2):
    return tmp1 + tmp2


@profile_deco
def minus(tmp1, tmp2):
    return tmp1 - tmp2


for i in range(10_000):
    add(i, i)

for i in range(10_000):
    add(i, 2*i)

for i in range(10_000):
    minus(i, 2*i)


add.print_stat()
print('='*120)
minus.print_stat()
 
