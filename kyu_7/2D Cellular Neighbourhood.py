def get_moore(mat: list[list[int]], coordinates: tuple[int, int]) -> list[int]:
    x, y = coordinates
    nbr: list[int] = []

    row = len(mat)
    col = len(mat[0])

    for i in range (x-1, x+2):
        print (f"for x value {x} : in {i}")

        if i == x-1 and i >= 0:
            if y - 1 >= 0:
                nbr.append(mat[i][y-1])
            
            nbr.append(mat[i][y])

            if y + 1 < col:
                nbr.append(mat[i][y+1])
        
        if i == x:
            if y - 1 >= 0:
                nbr.append(mat[i][y-1])

            if y + 1 < col:
                nbr.append(mat[i][y+1])
        
        if i == x+1 and i < row:
            if y - 1 >= 0:
                nbr.append(mat[i][y-1])
            
            nbr.append(mat[i][y])

            if y + 1 < col:
                nbr.append(mat[i][y+1])
            
    return nbr


def get_von_neumann(mat: list[list[int]], coordinates: tuple[int, int]) -> list[int]:
    x, y = coordinates

    nbrs = []

    if x - 1 >= 0:
        nbrs.append(mat[x-1][y])

    if y - 1 >= 0:
        nbrs.append(mat[x][y-1])

    if y + 1 < len(mat[0]):
        nbrs.append(mat[x][y+1])

    if x + 1 < len(mat):
        nbrs.append(mat[x+1][y])

    return nbrs


def get_neighbourhood(n_type: str, mat: list[list[int]], coordinates: tuple[int, int]) -> list[int]:
    """
        This kata is the first part of a series: Neighbourhood kata collection. If this one is too easy you can try out the harder katas. ;)

    The neighbourhood of a cell (in a matrix) are cells that are near to it. There are two popular types:

        The Moore neighborhood are eight cells which surround a given cell
        The Von Neumann neighborhood are four cells which share a border with the given cell

    Task

    Given a neighbourhood type ("moore" or "von_neumann"), a 2D matrix (a list of lists) and a pair of coordinates, return the list of neighbours of the given cell.

    Notes:

        The order of the elements in the output list is not important
        If the input indexes are outside the matrix, return an empty list
        If the the matrix is empty, return an empty list
        Order of the indices: the first index should be applied for the outer/first matrix layer and the last index for the most inner/last layer. coordinates = (m, n) should be applied like mat[m][n]

    Examples

    * n   0    1    2    3    4
    m  --------------------------
    0  |  0 |  1 |  2 |  3 |  4 |
    1  |  5 |  6 |  7 |  8 |  9 |
    2  | 10 | 11 | 12 | 13 | 14 |
    3  | 15 | 16 | 17 | 18 | 19 |
    4  | 20 | 21 | 22 | 23 | 24 |
    --------------------------

    get_neighborhood("moore", mat, (1,1)) == [0, 1, 2, 5, 7, 10, 11, 12]
    get_neighborhood("moore", mat, (0,0)) == [1, 6, 5]
    get_neighborhood("moore", mat, (4,2)) == [21, 16, 17, 18, 23]
    get_neighborhood("von_neumann", mat, (1,1)) == [1, 5, 7, 11]
    get_neighborhood("von_neumann", mat, (0,0)) == [1, 5]
    get_neighborhood("von_neumann", mat, (4,2)) == [21, 17, 23]

    -----------------------------------------
    [ [], [], [], [],]

    (x, y)
    |(0,0), (0, 1), (0, 2)	|
    |(1,0), (1, 1), (1, 2)	|
    |(2,0), (2, 1), (2, 2)	|
    |(3,0), (3, 1), (3, 2)	|


    Moore neighborhood are eight cells which surround a given cell - A.K.A, all the 8 that surround it - 
    for x-1 -> y-1, y and y+1
    for x -> y-1 and y+1
    for x+1 -> y-1, y and y+1


    The Von Neumann neighborhood are four cells which share a border with the given cell - A.K.A, all the directly up, down, left and right -
    get (x-1, y), (x, y-1), (x, y+1), (x+1, y)


    """

    if len(mat) == 0:
        print("matrix is empty")
        return []

    if len(mat) - 1 < coordinates[0] or len(mat[0]) - 1 < coordinates[1]:
        print("coordinates are out of bounds")
        return []

    print(f"coordinatse value: {mat[coordinates[0]][coordinates[1]]}")

    if n_type == "moore":
        return get_moore(mat, coordinates)

    else:
        return get_von_neumann(mat, coordinates)


mat = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
]

print(get_neighbourhood("moore", mat, (4,2)))
