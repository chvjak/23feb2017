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
    return []

data = lib.read_data("me_at_the_zoo.in")

solution = solve(data)

lib.write_data("output1.txt", solution)


