def mergeSort(array):
  mid = len(array)//2
  if len(array) == 1:
    return array

  return merge(mergeSort(array[:mid]), mergeSort(array[mid:]))
  
def merge(a, b):
  l = []
  i=0
  j=0
  while True: 
    if len(a)==i:
      l+=b[j:]
      break
    if len(b)==j:
      l+=a[i:]
      break
    if a[i]>b[j]:
      l.append(b[j])
      j+=1
    else:
      l.append(a[i])
      i+=1
  return l


print(mergeSort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
