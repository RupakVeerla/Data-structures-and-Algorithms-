# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso

def isIPv4Address(inputString):
    i = inputString.split('.')
    if len(i)!=4:
        return False
    for x in i:
        if not x.isdigit() or not int(x)<256 or (len(x)>1 and x.startswith('0')):
            return False
    return True
