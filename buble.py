list = [4,5,6,9,2,11,1]
def sort(list):

    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


sort(list)

print(list)
