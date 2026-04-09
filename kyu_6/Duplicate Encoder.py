def duplicate_encode(word):
    result = ""
    word = word.lower()
    
    for char in word:
        count = 0
        for x in range(len(word)):
            if char == word[x]:
                count += 1
        
        if count == 1:
            result = result + "("
        
        else:
            result = result + ")"
    
    return result