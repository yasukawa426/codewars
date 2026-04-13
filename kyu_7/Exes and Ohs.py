def xo(s):
    """Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
"""
    s = s.lower()    
    return s.count("x") == s.count("o")