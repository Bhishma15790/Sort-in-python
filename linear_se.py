list = [5,6,7,8,9,3]
n = int(input("enter the any number:"))
pos = -1
def search(list, n):
 
    for i in range(len(list)):
        globals()['pos'] = i
        if list[i] == n:
            return True
 
    return False



if search(list, n):
    print("found at position:", pos )
else:
    print("not found")