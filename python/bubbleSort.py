def bubble_sort(list):
    l = len(list)
    for i in range(l):
        for j in range(l-i-1):
            if (list[j] > list[j+1]):
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
            
    return list

unsortedList = [10,9,1,5,3,3]

sortedList = bubble_sort(unsortedList)
print(sortedList)