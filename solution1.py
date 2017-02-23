import lib

# test
def memoize(function):
    from functools import wraps

    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

#@memoize
def solve(data):
    res = [None] * 3

    res[0] = [2]
    res[1] = [3, 1]
    res[2] = [0, 1]

    return res

data = lib.read_data("me_at_the_zoo.in")

solution = solve(data)

lib.write_data("output1.txt", solution)


