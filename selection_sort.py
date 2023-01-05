list = [8,4,5,6,7,88,99,1,20]
size = len(list)
def sort(list, size):
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if list[j] < list[min]:
                min = j
        (list[i], list[min]) = (list[min], list[i])


sort(list, size)
print(list)