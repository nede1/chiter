from __future__ import annotations

import itertools
from functools import reduce
from operator import length_hint, add
from typing import Any, Callable, Optional, Iterable, Iterator

from .meta import ChIterMeta


class ChIter(Iterator[Any], metaclass=ChIterMeta):
    __slots__ = ('_iterable', '_length_hint')

    @classmethod
    def from_iterables(cls, *iterables) -> ChIter:
        obj = cls(itertools.chain(*iterables))
        obj._length_hint = sum(map(length_hint, iterables))
        return obj

    def __init__(self, iterable: Iterable):
        self._length_hint = length_hint(iterable)
        self._iterable = iter(iterable)

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self._length_hint:
            self._length_hint -= 1
        return next(self._iterable)

    def __add__(self, other) -> ChIter:
        if not hasattr(other, '__iter__'):
            return NotImplemented
        return type(self).from_iterables(self, other)

    def __radd__(self, other) -> ChIter:
        if not hasattr(other, '__iter__'):
            return NotImplemented
        return type(self).from_iterables(other, self)

    def __length_hint__(self) -> int:
        return self._length_hint

    def filter(self, func: Optional[Callable]) -> ChIter:
        return filter(func, self)

    def map(self, func: Callable) -> ChIter:
        return map(func, self)

    def enumerate(self, start: int = 0) -> ChIter:
        return enumerate(self, start=start)

    def zip(self) -> ChIter:
        return zip(*self)

    def reduce(self, func: Callable, initial=None) -> Any:
        args = (i for i in (self, initial) if i is not None)
        return reduce(func, *args)

    def sorted(self, key: Optional[Callable] = None, reverse: bool = False) -> ChIter:
        return sorted(self, key=key, reverse=reverse)

    def reversed(self) -> ChIter:
        return reversed(tuple(self))

    def accumulate(self, func=add) -> ChIter:
        return itertools.accumulate(self, func)

    def combinations(self, r: int) -> ChIter:
        return itertools.combinations(self, r)

    def combinations_with_replacement(self, r: int) -> ChIter:
        return itertools.combinations_with_replacement(self, r)

    def compress(self, selectors: Iterable[bool]) -> ChIter:
        return itertools.compress(self, selectors)

    def dropwhile(self, predicate: Callable) -> ChIter:
        return itertools.dropwhile(predicate, self)

    def groupby(self, key: Optional[Callable] = None) -> ChIter:
        return itertools.groupby(self, key=key)

    def filterfalse(self, predicate: Callable) -> ChIter:
        return itertools.filterfalse(predicate, self)

    def slice(self, start: int, stop: Optional[int] = None, step: Optional[int] = None) -> ChIter:
        args = (start, stop, step)
        start_is_stop = all((i is None for i in args[1:]))
        slice_args = args[:1] if start_is_stop else args
        return itertools.islice(self, *slice_args)

    def permutations(self, r: Optional[int] = None) -> ChIter:
        return itertools.permutations(self, r)

    def product(self, *, repeat=1) -> ChIter:
        return itertools.product(self, repeat=repeat)

    def takewhile(self, func=Callable) -> ChIter:
        return itertools.takewhile(func, self)

    def starmap(self, func: Callable) -> ChIter:
        return itertools.starmap(func, self)

    def tee(self, n: int = 2) -> ChIter:
        return map(type(self), itertools.tee(self, n))

    def cycle(self) -> ChIter:
        return itertools.cycle(self)

    def zip_longest(self, *, fillvalue=None) -> ChIter:
        return itertools.zip_longest(*self, fillvalue=fillvalue)

    def flatten(self) -> ChIter:
        return itertools.chain.from_iterable(self)
