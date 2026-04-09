def generate_hashtag(s):
    s = s.strip()
    
    if s == "":
        return False
    
    hashtag = "#"
    words = s.split(" ")
    for word in words:
        hashtag = hashtag +  word.strip().capitalize()
    
    if len(hashtag) > 140:
        return False
    
    return hashtag