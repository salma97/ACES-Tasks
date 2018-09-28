class matrix():

    __id = 0

    def __init__ (self, *list):
        if len(list) == 0:
            self.list = [0]
        else:
            self.list = list
        matrix.__id = matrix.__id + 1
        self.__specialid = matrix.__id

    def description (self):
        if len(self.list) == 1:
            print(self.list)
        else:
            for i in self.list:
                for k in i:
                    print ("{} " .format(k))

    def columns (self):
        columns = len(self.list[0])
        return columns

    def rows (self):
        rows = len(self.list[0][0])
        return rows

    def dimensions (self):
        dimensions = str(len(self.list[0][0])) + "x" + str(len(self.list[0]))
        return dimensions

    def get_id(self):
        return self.__specialid


#matrix of 3 rows and 3 columns
A = matrix([[1,2,3],[2,3,4],[5,6,7]])
#matrix of 4 rows and 2 columns
B = matrix([[1,2,3,4],[5,8,4,7]])
#empty matrix
C = matrix()

#matrix A:
A.description()
print("\n")
#number of columns in matrix A:
A_columns = A.columns()
print("number of columns in matrix A = %d" %A_columns)
#number of rows in matrix A:
A_rows = A.rows()
print("number of rows in matrix A = %d" %A_rows)
#dimensions of matrix A:
A_dim = A.dimensions()
print("dimensions of matrix A = ")
print(A_dim)
#id of matrix A:
A_id = A.get_id()
print("id of matrix A = %d" %A_id)
print("\n")

#matrix B:
B.description()
print("\n")
#number of columns in matrix B:
B_columns = B.columns()
print("number of columns in matrix B = %d" %B_columns)
#number of rows in matrix B:
B_rows = B.rows()
print("number of rows in matrix B = %d" %B_rows)
#dimensions of matrix B:
B_dim = B.dimensions()
print("dimensions of matrix B = ")
print(B_dim)
#id of matrix B:
B_id = B.get_id()
print("id of matrix B = %d" %B_id)
print("\n")

#matrix C:
C.description()
print("\n")
#id of matrix C:
C_id = C.get_id()
print("id of matrix C = %d" %C_id)
print("\n")
