s = """HackerRank.com presents "Pythonist 2"."""
temp = """"""
for x in s:
    if x.isalpha():
        if x.islower():
            z = x.upper()
            temp = temp+str(z)
        else:
            z = x.lower()
            temp = temp+str(z)
    else:
        temp = temp+str(x)
