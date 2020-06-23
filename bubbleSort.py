def bubbleSort(array):
  for i in range(len(array)):
    for j in range(1, len(array)-i):
      if array[j-1]>array[j]:
        array[j-1], array[j] = array[j], array[j-1]
  print(array)

bubbleSort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])
