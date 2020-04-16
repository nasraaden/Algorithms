#  #!/usr/bin/python

# import sys

# # The cache parameter is here for if you want to implement
# # a solution that is more efficient than the naive
# # recursive solution
# def eating_cookies(n, cache=None):
#     # base cases, how many ways are there to eat each cookie
#     if cache is None:
#         cache = [0] * (n + 1)
#     if n <= 1:
#         cache[n] = 1
#     if n == 2:
#         cache[n] = 2
#     elif cache[n] == 0:
#         cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
#     return cache[n]


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')


#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # base cases
    # each n becomes the summation of the previous three ns
    if cache is None:
        cache = {}
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    # if we have cache, and if our item is in it, return cache[n]
    elif cache and cache[n]:
        return cache[n]
    # otherwise store it there
    else:
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]
# TypeError: 'NoneType' object does not support item assignment
# cache wasn't initialized
# pass cache into children
# we don't get to use it if we don't pass it around
# print(eating_cookies(4, {}))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
