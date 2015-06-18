# Matrix
Revolutionary python class. It can all of the major matrix functions, including addition, subtraction, multiplication, inverse, determinant, and it can solve a system of equations.


Examples
==
    a = Matrix([[1,2],[3,4]])
    b = Matrix([[4,3],[2,1]])
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
Division
--
        print(a / b) #a * ~b
        >>> [1.5, -2.5]
            [2.5, -3.5]
Solving Systems
--
    g = Matrix([[1,3,7],[2,4,10]])
    print(g.solve())
    >>> (1.0,2.0) #x = 1.0, y = 2.0
    
