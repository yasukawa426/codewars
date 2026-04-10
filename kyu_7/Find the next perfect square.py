from math import sqrt


def find_next_square(sq):
    """You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative."""
    if not sqrt(sq).is_integer():
        return -1

    sq += 1

    while not sqrt(sq).is_integer():
        sq += 1

    return sq
    #
    # return (sqrt(sq) + 1) ** 2


print(find_next_square(1))
