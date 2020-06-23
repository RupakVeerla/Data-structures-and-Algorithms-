def factoral(n):
  if n!=2:
    return n*factoral(n-1)
  return 2

def factoralIteration(n):
  r = n
  for i in range(1,n):
    r*=i
  return r

print(factoral(5))
