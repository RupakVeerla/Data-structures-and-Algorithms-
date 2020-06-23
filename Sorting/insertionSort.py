def insertionSort(array):
  for i in range(1,len(array)):
    while i!=0:
      if array[i-1] < array[i]:
        break
      array[i-1], array[i] = array[i], array[i-1]
      i-=1
  
  print(array)

insertionSort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])
