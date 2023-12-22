__author__ = "Mischa Jampen"

class Matrix:
        # Remember that instanes variables should be private (i.e., prepended with two underscores: __)
        def __init__(self, matrix):
            assert isinstance(matrix, list), "matrix is not  a list"
            assert matrix != [], "empty list"
            for l in matrix:
                assert isinstance(l, list), "not a nested list"
                assert l != [], "empty sub-list"
                assert len(l) == len(matrix[0]), "matrix not same length"
                for i in l:
                    assert isinstance(i, (float,int)), "invalid value in sub-list"
            self.__matrix = matrix
        
        def __add__(self, other):
            assert isinstance(other, Matrix)

            assert len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0])

            C = []
            for i in self.__matrix:
                C.append([0] * len(self.__matrix[0]))

            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[0])):
                    C[i][j] = self.__matrix[i][j] + other.__matrix[i][j]
            return Matrix(C)


        def __mul__(self, other):
            assert isinstance(other, Matrix)
            assert len(self.__matrix[0]) == len(other.__matrix)
            
            C = []
            for i in self.__matrix:
                C.append([0] * len(other.__matrix[0]))
            for i in range(len(self.__matrix)):
                for j in range(len(other.__matrix[0])):
                    for k in range(len(other.__matrix)):
                        C[i][j] += self.__matrix[i][k] * other.__matrix[k][j]
            return Matrix(C)
        
        def __eq__(self, other) -> bool:
            assert isinstance(other, Matrix)
            return self.__matrix == other.__matrix

        def __hash__(self):
            matrix_elements = []
            for list in self.__matrix:
                matrix_elements.append(tuple(list))
            return hash(tuple(matrix_elements))

        def __repr__(self):
            return repr(self.__matrix)

            


    # Also, implement the special methods __eq__, __hash__, __add__, and __mul__
    # as per the task description.

    # def __eq__(self, other):
    #   etc ...

# Make sure to work on task/tests.py as well to test your implementation!

if __name__ == "__main__":
    m = Matrix([[1,2],[3,4]])
    t = Matrix([[1,2],[3,4]])
    e = Matrix([[2,5],[5,9]])
    #f = [[1,2],[3,4]]

    print(m)
    print(t)
    print(e)
    print(m == t)       #True
    print(t == e)       #False
    #print(m == f)       #NotImplemented

    d = {m: "1", t: "2", e: "3"}
    d.update({m: "4"})

    #print(m + t)
    print(m * t)
