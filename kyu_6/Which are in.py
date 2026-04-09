def in_array(array1, array2):
    result = []
    
    for word in array1:
        for candidate in array2:
            if word in candidate:
                if word not in result:
                    result.append(word)
                    break

    result.sort()
            
    
    return result