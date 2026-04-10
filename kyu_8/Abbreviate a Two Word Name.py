def abbrev_name(name: str) -> str:
    return ".".join([word[0].upper() for word in name.split(" ")])

print(abbrev_name("Sam Harris")) # return "S.H"
print(abbrev_name("patrick feeney")) # return "P.F"