from functools import reduce
def dot(a,b):
	return sum([a[i] * b[i] for i in range(len(b))])
class Matrix:
	def __init__(self, rows):
		self.row = rows
	def __repr__(self):
		return '\n'.join([str(i) for i in self.row]) + "\n"

	def __abs__(self):
		if len(self.row) > 2:
			a = 0
			for replace, place in enumerate(self.row[0]):
				sec = Matrix([[i for n,i in enumerate(self.row[j]) if (n != replace)] for j in range(1, len(self.row))])
				a += (-1)**replace * place * abs(sec)
			return a
		elif len(self.row) == 2:
			return (self.row[0][0] * self.row[1][1]) - (self.row[0][1] * self.row[1][0])
		else:
			return self.row[0][0]
	def __mul__(self, other):
		if type(other) == Matrix:
			return Matrix([[round(dot(i, [other.row[k][j] for k in range(len(other.row))]),4) for j in range(len(other.row[0]))] for i in self.row])
		return Matrix.scalar(self, other)
	def __add__ (self, other):
		return Matrix([[self.row[k][i] + other.row[k][i] for i in range(len(self.row[0]))] for k in range(len(self.row))])
	def __neg__(self):
		return Matrix([[-1 * i for i in j] for j in self.row])
	def __sub__(self,other):
		return Matrix([self + -other])
	def transpose(something):
		return Matrix([[something.row[k][i] for k in range(len(something.row[0]))] for i in range(len(something.row))])
	def scalar(self, number):
		return Matrix([[round(number * i,4) for i in j] for j in self.row])
	def __pow__(self, power):
		g = [self for i in range(power)]
		return reduce(lambda x,y: x * y, g)
	def __invert__(self):
		try:
			determinant = abs(self)
		except:
			return self #Returns, if invertible
		news = Matrix.transpose(self)
		news = [[(-1) ** (column + row) * abs(Matrix([[news.row[k][i] for i in range(len(self.row[0])) if i != column] for k in range(len(self.row)) if k != row])) for column in range(len(self.row[0]))] for row in range(len(self.row))]
		return Matrix.scalar( Matrix(news),1/determinant)

mat = Matrix([[1,2,0,0],[0,1,9,0],[8,0,1,0],[4,3,5,1]])

a = Matrix([[1,3],[3,4]])
b = Matrix([[1,2],[3,4]])
print(a-b)
print(~a)
print(a ** 15)
print(a * ~a)
