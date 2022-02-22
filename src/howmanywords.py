s = "he is a good programmer, he won 865 competitions, but sometimes he don't. What do you think? All test-cases should pass. Done-done?"


def howMany(s):
    x = s.split()
    out = []
    for i in range(len(x)):
        x[i]=x[i].replace("?","")
        x[i]=x[i].replace(",","")
        x[i]=x[i].replace(".","")
        x[i]=x[i].replace("!","")
        if x[i].isnumeric():
            pass
        else:
            out.append(x[i])
    # return out
    return len(out)


print(howMany(s))
