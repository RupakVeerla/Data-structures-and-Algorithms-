# https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

def sortByHeight(a):
    l=sorted([i for i in a if i!=-1])
    for i in range(len(a)):
        if a[i] == -1:
            l.insert(i, -1)
    return l
