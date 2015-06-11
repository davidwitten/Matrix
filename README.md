# Matrix
Revolutionary python class. It can all of the major matrix functions, including addition, subtract, multiplication, inverse, determinant.

Example
==
    a = Matrix([1,2],[3,4])
    b = Matrix([4,3],[2,1])
    #Sets matrices a,b
Printing
--
    print(a)
    >>> [1, 2]
        [3, 4]
    print(~a)
    >>> [-2.0,1.0]
        [1.5,-0.5]
Inverse
--
    g = ~a
    print(a * g)
    >>> [1, 0]
        [0, 1]
Determinant
--
    d = abs(b)
    print(d)
    >>> -2
Addition, Subtraction
--
    c = a + b
    d = a - b
Exponentiation
--
    c = a ** 3
    print(c)
    >>> [37, 54]
        [81, 118]
Multiplication
--
    print(a * 3)
    >>> [3, 6]
        [9, 12]
    print(a * b)
    >>> [8, 5]
        [20, 13]
