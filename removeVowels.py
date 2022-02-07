def disemvowel(name):
    for i in "aAeEiIoOuU":
        name = name.replace(i,"")
    return name

print(disemvowel("This website is for losers LOL!"))