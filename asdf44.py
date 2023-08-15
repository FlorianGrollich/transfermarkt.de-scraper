x = "asdf"
print(x.split(""))
for cha in resultWord:
    try:
        index = searchWord[lastIndex::].index(cha)
        lastIndex = index
        sub_string += cha
    except ValueError:
        break