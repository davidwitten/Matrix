__author__ = 'DavidW'

def multList(scalar, array):
    return list(map(lambda x: x * scalar, array))

def addLists(array1,array2):
    return [array1[i] + array2[i] for i in range(len(array1))]

def toPos(arrays,pos):#takeout position
    arrays[1:] = [addLists(multList(-arrays[i][pos]/arrays[0][pos], arrays[0]), arrays[i]) for i in range(1, len(arrays))]
    return arrays

def printWell(arrays):
    print("x = ", arrays[1][2]);print("y = ", arrays[0][2])

def func(arrays):
    #takes out first term, and second term of each equation
    arrays = toPos(arrays, 0)[::-1]
    arrays = toPos(arrays, 1)
    arrays = arrays[::-1]
#finalizes it in array form
    arrays = [multList(1/i[n], i) for n, i in enumerate(arrays)]
    arrays = [[round(j, 5) for j in i] for i in arrays]
    return arrays
#prints it well
'''
print(main(arrays))
printWell(main(arrays))
'''
