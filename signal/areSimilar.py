#https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP

def areSimilar(a, b):
    i=0
    while len(a)>2 and i<len(a):
        if a[i] == b[i]:
            a.pop(i)
            b.pop(i)
            continue
        i+=1   
    
    return a==b or a==b[::-1]
