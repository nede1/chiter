import itertools
from functools import reduce
from operator import add

from chiter import ChIter


def test_filter():
    i = ChIter(range(5)).filter(lambda x: x > 2)

    assert isinstance(i, ChIter)
    assert list(i) == list(range(3, 5))


def test_map():
    i = ChIter(range(5)).map(lambda x: x + 1)

    assert isinstance(i, ChIter)
    assert list(i) == list(range(1, 6))


def test_enumerate():
    i = ChIter(range(5)).enumerate()

    assert isinstance(i, ChIter)
    assert list(i) == list(enumerate(range(5)))


def test_enumerate_start():
    i = ChIter(range(5)).enumerate(start=2)

    assert isinstance(i, ChIter)
    assert list(i) == list(enumerate(range(5), start=2))


def test_zip():
    i = ChIter(enumerate(range(5))).zip()

    assert isinstance(i, ChIter)
    assert list(i) == list(zip(*enumerate(range(5))))


def test_reduce():
    i = ChIter(range(5)).reduce(add)

    assert isinstance(i, int)
    assert i == reduce(add, range(5))


def test_reduce_initial():
    i = ChIter(range(5)).reduce(add, initial=2)

    assert isinstance(i, int)
    assert i == reduce(add, range(5), 2)


def test_sorted():
    i = ChIter(range(5)).sorted()

    assert isinstance(i, ChIter)
    assert list(i) == sorted(range(5))


def test_sorted_key():
    i = ChIter(range(5)).sorted(key=lambda x: -x)

    assert isinstance(i, ChIter)
    assert list(i) == sorted(range(5), key=lambda x: -x)


def test_sorted_key_reverse():
    i = ChIter(range(5)).sorted(key=lambda x: -x, reverse=True)

    assert isinstance(i, ChIter)
    assert list(i) == sorted(range(5), key=lambda x: -x, reverse=True)


def test_reversed():
    i = ChIter(range(5)).reversed()

    assert isinstance(i, ChIter)
    assert list(i) == list(reversed(range(5)))


def test_accumulate():
    i = ChIter(range(5)).accumulate()

    assert isinstance(i, ChIter)
    assert list(i) == list(itertools.accumulate(range(5)))


def test_flatten():
    i = ChIter(enumerate(range(5))).flatten()

    assert isinstance(i, ChIter)
    assert list(i) == list(itertools.chain.from_iterable(enumerate(range(5))))


def test_tee():
    i = ChIter(range(5)).tee()

    assert isinstance(i, ChIter)
    i1, i2 = i

    assert isinstance(i1, ChIter)
    assert isinstance(i2, ChIter)

    assert list(i1) == list(i2)


def test_tee_n():
    i = ChIter(range(5)).tee(3)

    assert isinstance(i, ChIter)
    i1, i2, i3 = i

    assert isinstance(i1, ChIter)
    assert isinstance(i2, ChIter)
    assert isinstance(i3, ChIter)

    assert list(i1) == list(i2) == list(i3)


def test_cycle():
    i = ChIter([None]).cycle()

    assert isinstance(i, ChIter)
    assert list(zip(i, range(5))) == list(zip(itertools.cycle([None]), range(5)))


def test_combinations():
    i = ChIter(range(5)).combinations(2)

    assert isinstance(i, ChIter)
    assert list(itertools.combinations(range(5), 2)) == list(i)


def test_combinations_with_replacement():
    i = ChIter(range(5)).combinations_with_replacement(2)

    assert isinstance(i, ChIter)
    assert list(itertools.combinations_with_replacement(range(5), 2)) == list(i)


def test_compress():
    selectors = [True, False, True]
    i = ChIter(range(5)).compress(selectors)

    assert isinstance(i, ChIter)
    assert list(itertools.compress(range(5), selectors)) == list(i)


def test_dropwhile():
    def func(x):
        return x > 2

    i = ChIter(range(5)).dropwhile(func)

    assert isinstance(i, ChIter)
    assert list(itertools.dropwhile(func, range(5))) == list(i)


def test_filterfalse():
    def func(x):
        return x % 2

    i = ChIter(range(5)).filterfalse(func)

    assert isinstance(i, ChIter)
    assert list(itertools.filterfalse(func, range(5))) == list(i)


def test_groupby():
    iterable = [1, 1, 3, 2, 2]

    i = ChIter(iterable).groupby()

    assert isinstance(i, ChIter)
    assert [(k, list(g)) for k, g in itertools.groupby(iterable)] == [(k, list(g)) for k, g in i]


def test_groupby_key():
    def key(x):
        return x % 2

    iterable = [1, 1, 3, 2, 2]

    i = ChIter(iterable).groupby(key)

    assert isinstance(i, ChIter)
    assert [(k, list(g)) for k, g in itertools.groupby(iterable, key)] == [(k, list(g)) for k, g in i]
