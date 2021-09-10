this_file = 'lab06.py'


def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2) 
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    step = -1

    def adder(x):
        nonlocal step
        step += 1
        return n + step + x

    return adder


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    # base0, base1, num_calls = -1, 0, 0
    prev_1, prev_2, num_calls = 0, 1, 0

    def fib():
        nonlocal prev_1
        nonlocal prev_2
        nonlocal num_calls
        if num_calls == 0:
            num_calls += 1
            return prev_1
        if num_calls == 1:
            return prev_2
        current_fib = prev_1 + prev_2
        prev_1, prev_2,  = prev_2, current_fib
        return current_fib

        # nonlocal base0, base1, num_calls

        # if num_calls == 0:
        #     # base0, num_calls = base1 - 1, num_calls + 1
        #     num_calls += 1
        #     return base0 + 1
        # # base1, base2 = base1 + 1, base2 + 1
        # if num_calls == 1:
        #     num_calls += 1
        #     return base1 + 1
        # base0, base1 = base0 + 1, base1 + 1
        # return base0 + base1

    return fib

# Generators


def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"


def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
