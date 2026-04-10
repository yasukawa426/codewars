from math import sqrt

def find_next_square(sq):
    if not sqrt(sq).is_integer():
        return -1
    
    sq += 1

    while not sqrt(sq).is_integer():
        sq += 1

    return sq
    # 
    # return (sqrt(sq) + 1) ** 2


print (find_next_square(1))