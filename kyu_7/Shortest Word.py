def find_short(s: str) -> int:
    """Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types."""
    # your code here
    words = s.split(" ")
    words.sort(key=len)

    lol = len(words[0])
    return lol  # l: shortest word length
