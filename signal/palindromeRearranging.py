# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico
def palindromeRearranging(inputString):
    # s = [i for i in inputString]
    # c=0
    # while len(s)!=0:
    #     if s.count(s[0])==1:
    #         c+=1
    #         if c>1:
    #             return False
    #         s.pop(0)
    #         continue
    #     a = s.pop(0)
    #     s.pop(s.index(a))
    # return True
    return sum(inputString.count(i)%2 for i in set(inputString))<2
