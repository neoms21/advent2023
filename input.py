def openFile(path):
    inputs= [];
    f = open(path)
    for x in f:
        inputs.append(x)

    return inputs
