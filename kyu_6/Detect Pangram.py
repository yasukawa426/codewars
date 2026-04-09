def is_pangram(st):
    sentence = st.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in alphabet:
        if char not in sentence:
            return False   
    
    return True