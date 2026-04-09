import re

def strip_comments(strng, markers):
    """
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

"""
    print(f"string: \n{strng}\nmarkers: {markers}")
    
    #pattern to remove everything after markers upto new line
    patterns = []
    for marker in markers:
        pattern = re.escape(marker) + r"[^\n]*"
        patterns.append(pattern)
        
    sentences = strng.split("\n")
    
    formatted_sentences = []
     
    #for each line, apply the regex pattern (remove everything after marker), remove ending whitespace, and add to list
    for sentence in sentences:
        for pattern in patterns:
            sentence = re.sub(pattern, "", sentence).rstrip()
        
        
        formatted_sentences.append(sentence)

    #join them all to a single string adding "\n"
    return "\n".join(formatted_sentences)

string = "  oranges watermelons lemons pears bananas =\noranges ? apples watermelons ' strawberries\n@ bananas pears - ! apples"
markers = ['!', ',', "'", '.', '-', '@', '=']
print(strip_comments(string, markers))