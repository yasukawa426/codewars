def spin_word(sentence: str) -> str:
    """Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (just like the name of this kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
"""
    words = sentence.split(" ")

    new_sentence = []
    for word in words:
        if len(word) >= 5:
            reversed = ""
            word_length = len(word)
            for x in range(word_length):
                reversed += word[word_length -1 - x]
            new_sentence.append(reversed)
        else:
            new_sentence.append(word)

    return " ".join(new_sentence)


print(spin_word("Hey fellow warriors"))