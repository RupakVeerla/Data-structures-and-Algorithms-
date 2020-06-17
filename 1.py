# Find the sum of two elements in list equal to given number
#https://www.youtube.com/watch?v=XKu_SEDAykw

def hasPairWithSum(a,sum):
  list1 = []
  for i in a:
    if i in list1:
      return True
    list1.append(sum-i)
  return False

print(hasPairWithSum([6,4,3,1,7], 9))
