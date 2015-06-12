#r1,r2,r3 = [-1,-5,1,17],[-5,-5,5,5],[2,5,-3,-10]
r1,r2, r3 = [24, 20, 4, -4], [16, 1, 60, 5], [-3, 30, -4, 8]
def addparts(a,b):
	return [a[i] + b[i] for i in range(len(a))]
def multList(scal,a):
	return list(map(lambda x: x * scal, a))

def toPos(arrays,pos):#takeout position, for 2x2 arrays
    arrays[1] = addparts(multList(-arrays[1][pos]/arrays[0][pos], arrays[0]), arrays[1])
    return arrays

class Process:
    def __init__(self,r1,r2,r3):
        self.rows = [r1,r2,r3]
    def toPos(self): #sort and eliminate
        self.rows[1:] = [addparts(i, multList(-i[0]/self.rows[0][0], self.rows[0])) for i in self.rows[1:]]
        return self.rows

    def Last2(self):
        arrays = [i[1:] for i in self.rows[1:]]
        arrays = toPos(arrays, 0)[::-1];arrays = toPos(arrays, 1)
        arrays = [multList(1/i[1-n], i) for n, i in enumerate(arrays)]
        self.rows[1:] = [[0] + i for i in arrays]
        return self.rows
    def backSubstitute(self):
        self.rows[0] = addparts(addparts(self.rows[0], multList(-self.rows[0][1], self.rows[2])), multList(-self.rows[0][2], self.rows[1]))
        self.rows[0] = multList(1/self.rows[0][0], self.rows[0])
        return self.rows
    def Run(self):
        self.rows = Process.toPos(self)
        self.rows = Process.Last2(self)
        self.rows = Process.backSubstitute(self)
        self.rows = [[round(i,5) for i in j] for j in self.rows]
        return self.rows
myset = Process(r1,r2,r3)
r1,r2,r3 = Process.Run(myset)
print(r1,r2,r3)
