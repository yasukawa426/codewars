def to_camel_case(text):
    if text == "":
        return text

    #split the string with the delimitators
    text = text.replace("-", "_")
    w = text.split("_")
    
    #for each word (skipping the first one) in the sentence, we captalize it
    for x in range(len(w) - 1):
        word = w[x+1]
        word = word[0].upper() + word[1:]
        w[x+1] = word
                
    #then we transform the array of strings into a string
    text = ""
    for word in w:     
        text += word 
        
    return text