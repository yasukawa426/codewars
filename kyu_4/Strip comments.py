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

    if not markers:
        return strng
    #pattern to remove everything after markers upto new line
    #add escape characters and join them to a single string
    formatted_markers = "".join(map(re.escape, markers))
    pattern = r"[{}][^\n]*".format(formatted_markers)
    
        
    sentences = strng.split("\n")
    formatted_sentences = []
     
    #for each line, apply the regex pattern (remove everything after marker), remove ending whitespace, and add to list
    for sentence in sentences:
        sentence = re.sub(pattern, "", sentence).rstrip()
        
        formatted_sentences.append(sentence)

string = "  oranges watermelons lemons pears bananas =\noranges ? apples watermelons ' strawberries\n@ bananas pears - ! apples"
markers = ['!', ',', "'", '.', '-', '@', '=']
print(strip_comments(string, markers))