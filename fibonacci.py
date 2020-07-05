def fibonacciRecursive(n):
  if n<2:
    return n
  return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

def fibonacciIterative(n):
  s = [0,1]
  for i in range(2,n):
    s.append(s[i-2]+s[i-1])
  return s[n-2]+s[n-1]

def fibonacciRecursiveCache(n):
  d = {}
  def fibonacciRecursive(n):
    if n in d: 
      return d[n]
    if n<2:
      return n
    d[n] = fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
  return fibonacciRecursive(n)

print(fibonacciRecursiveCache(40))
