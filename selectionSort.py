def selectionSort(array):
  for i in range(len(array)):
    for j in range(i, len(array)):
      if array[i]>array[j]:
        array[i], array[j] = array[j], array[i]
  print(array)

selectionSort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])
