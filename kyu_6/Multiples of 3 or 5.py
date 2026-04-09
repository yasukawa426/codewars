def solution(number):
    #negative return 0
    if number < 0:
        return 0
    
    sum = 0
    number -= 1
    
    while number > 0:
        if number % 5 == 0 or number % 3 == 0:
            sum = sum + number
        
        number -= 1
  
    return sum