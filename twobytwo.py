__author__ = 'DavidW'
arrays = [[1,4,19], [2,3,18]]


def multList(scalar, array):
    return list(map(lambda x: x * scalar, array))

def addLists(array1,array2):
    return [array1[i] + array2[i] for i in range(len(array1))]

def toPos(arrays,pos):#takeout position
    arrays[1] = addLists(multList(-arrays[1][pos]/arrays[0][pos], arrays[0]), arrays[1])
    return arrays

def printWell(arrays):
    print("x = ", arrays[1][2]);print("y = ", arrays[0][2])

#takes out first term, and second term of each equation
arrays = toPos(arrays, 0)[::-1];arrays = toPos(arrays, 1)

#finalizes it in array form
arrays = [multList(1/i[1-n], i) for n, i in enumerate(arrays)]
arrays = [[round(j, 5) for j in i] for i in arrays]

#prints it well
print(arrays)
printWell(arrays)
