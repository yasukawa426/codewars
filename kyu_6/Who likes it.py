def likes(names: list[str]) -> str:
    """You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases."""
    liked = ""
    names_length = len(names)

    if names_length == 0:
        liked = "no one likes this"

    elif names_length == 1:
        liked = f"{names[0]} likes this"

    elif names_length == 2:
        liked = f"{names[0]} and {names[1]} like this"
    
    elif names_length == 3:
        liked = f"{names[0]}, {names[1]} and {names[2]} like this"
    
    else:
        liked = f"{names[0]}, {names[1]} and {names_length - 2} others like this"
    
    return liked


print (likes([])   )