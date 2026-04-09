def int_to_digit_list(n: int) -> list[int]:
    # number to str, then list of chars parsed to int
    return  [int(digit) for digit in str(n)]

def next_bigger(n: int) -> int:
    if n <= 11:
        return -1
    
    #for example, 59876
    #first step - find the pivot: from the right, find the first number that is "pivot < n" than the directly next digit to its right - pivot is 5
    #second step - looking from the right of pivot, find the smallest digit that is bigger than pivot - 6
    #third step - swap the pivot with the smallest bigger digit - 69875
    #fourth step - sort the digits to the right of the pivot in ascending order - 65789
    #fifth step - ????
    #profit

    #1st step
    digits = int_to_digit_list(n)
    pivot:int|None = None
    
    count = len(digits) - 1 

    while count > 0:
        if digits[count - 1] < digits[count]:
            pivot = digits[count - 1]
            
            break

        count -= 1

    #couldn't find a pivot, meaning we are at the biggest possible number with those digits
    print(f"pivot: {pivot}")
    if pivot is None:
        return -1
    
    #2nd step, smallest bigger than pivot - pivot index = count - 1

    smallest = (digits[count], count)

    for i in range(count, len(digits)):
        if digits[i] > pivot and digits[i] < smallest[0]:
            smallest = (digits[i], i)

    print(f"smallest: {smallest}")

    #3rd step - swap the pivot with the smallest bigger digit
    digits[count - 1], digits[smallest[1]] = digits[smallest[1]], digits[count - 1]
    print(f"after swap: {digits}")

    #4th step - sort the digits to the right of the pivot in ascending order
    digits[count:] = sorted(digits[count:])
    print(f"after sort: {digits}")
    
    #convert back to int
    final_number = ""
    for digit in digits:
        final_number += str(digit)

    return int(final_number)

    
tests = [
    12,
    21,
    513,
    2017,
    111,
    115,
    414,
    144,
    1234,
    1243,
    4321,
    59876,
    10990,
    120,
    1020,
    907,
    534976,
    1234321
]

for test in tests:
    print(f"{test}: ")
    print(f"final result: {next_bigger(test)}")
