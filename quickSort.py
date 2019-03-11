def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint - 1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >=leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done =  True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp;

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

alist = []


arrInsert = input("What Do you want? :")
while 1:
    if arrInsert == "-o":
        arrType = input("Input array type you want: ")
        if arrType == "A":
            arrStart = input("You want to input to make array? : ")
            if arrStart == "-i":
                while 1:
                    value = int(input("Input Number(1010 = stop): "))
                    if(value) == 1010:
                        break
                    alist.append(value)
                quickSort(alist)
                print(alist)
        elif arrType == "D":
            arrStart = input("You want to input to make array? : ")
            if arrStart == "-i":
                while 1:
                    value = int(input("Input Number(1010 = stop): "))
                    if (value) == 1010:
                        break
                    alist.append(value)
                quickSort(alist)
                alist.reverse()
                print(alist)
        else:
            print("Plz Enter A or D")
    else:
        print("Err")