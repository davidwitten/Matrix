import twobytwo

def addPart(array):
    return [sum([array[k][i] for k in range(len(array))]) for i in range(len(array[0]))]

def bigList(array):
    if len(array) == 2:
        return twobytwo.func(array)
    else:
        array = twobytwo.toPos(array, 0)
        Barray = bigList([i[1:] for i in array[1:]])
        array = [array[0]]  + [[0] + Barray[i] for i in range(len(Barray))] #For n x n array, it solves the bottom right (n-1) x (n-1)   
        for i in range(1,len(array)): #Can't do it inline, 
            array[0] = addPart([array[0], twobytwo.multList(-array[0][i],array[i])]) #Solves for one, but it still won't be simplified
        array[0] = twobytwo.multList(1/array[0][0], array[0]) #simplify
        return array

#print(bigList([[1,2,-1,4],[2,1,1,-2],[1,2,1,2]]))
print(bigList([[2,-1,5,1,-3],[3,2,2,-6,-32],[1,3,3,-1,-47],[5,-2,-3,3,49]]))
'''
self.rows[0] = addparts(addparts(self.rows[0], multList(-self.rows[0][1], self.rows[2])), multList(-self.rows[0][2], self.rows[1]))
self.rows[0] = multList(1/self.rows[0][0], self.rows[0])
        
'''
m
