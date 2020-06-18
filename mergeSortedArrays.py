def mergeSortedArrays(array1, array2):
  # return sorted(array1+array2)
  
  if len(array1) == 0 or len(array2)==0:
    return array1+array2
  i = 0
  j = 0
  newArray = []

  while i<len(array1) and j<len(array2):
    if array1[i]<array2[j]:
      newArray.append(array1[i])
      i += 1
    else:
      newArray.append(array2[j])
      j += 1
  return newArray+array1[i:]+array2[j:]

print(mergeSortedArrays([0,3,4,31], [3,4,6,30]))
