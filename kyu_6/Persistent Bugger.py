def persistence(n):
    tries = 0
    
    # number has more than 1 digit
    while len(str(n)) > 1:
        number = str(n)
        
        result = int(number[0])
        
        #multiples each char skipping first (first * first)
        for x in range(len(number) - 1):
            result = result * int(number[x+1])
        
        n = result
        
        tries = tries + 1
    
    return tries