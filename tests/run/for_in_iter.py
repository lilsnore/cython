# mode: run
# tag: forin

import sys

def for_in_pyiter(it):
    """
    >>> for_in_pyiter(Iterable(5))
    [0, 1, 2, 3, 4]
    """
    l = []
    for item in it:
        l.append(item)
    return l

def for_in_list():
    """
    >>> for_in_pyiter([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    """

class Iterable(object):
    """
    >>> for_in_pyiter(Iterable(5))
    [0, 1, 2, 3, 4]
    """
    def __init__(self, N):
        self.N = N
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.N:
            i = self.i
            self.i += 1
            return i
        raise StopIteration
    next = __next__

if sys.version_info[0] >= 3:
    class NextReplacingIterable(object):
        def __init__(self):
            self.i = 0
        def __iter__(self):
            return self

        def __next__(self):
            if self.i > 5:
                raise StopIteration
            self.i += 1
            self.__next__ = self.next2
            return 1
        def next2(self):
            self.__next__ = self.next3
            return 2
        def next3(self):
            del self.__next__
            raise StopIteration
else:
    class NextReplacingIterable(object):
        def __init__(self):
            self.i = 0
        def __iter__(self):
            return self

        def next(self):
            if self.i > 5:
                raise StopIteration
            self.i += 1
            self.next = self.next2
            return 1
        def next2(self):
            self.next = self.next3
            return 2
        def next3(self):
            del self.next
            raise StopIteration

def for_in_next_replacing_iter():
    """
    >>> for_in_pyiter(NextReplacingIterable())
    [1, 1, 1, 1, 1, 1]
    """

def for_in_gen(N):
    """
    >>> for_in_pyiter(for_in_gen(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i in xrange(N):
        yield i
