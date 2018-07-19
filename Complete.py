import random

from copy import deepcopy


class Matrix:
    #雙迴圈利用list的方式建立矩陣
    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.nrows=nrows
        self.ncols=ncols
        self.mat=[]
        for i in range(self.nrows):#列
            mat=[]
            for j in range(self.ncols):#行
                mat.append(random.randint(0,9))
            self.mat.append(mat)       
        
    def add(self, m):
        """return a new Matrix object after summation"""
        CM = Matrix(self.nrows, self.ncols)
        if nrows_A==nrows_B and ncols_A==ncols_B:#判斷兩個矩陣的大小要一樣
            for i in range(self.nrows):
                for j in range(self.ncols):
                    CM.mat[i][j] = AM.mat[i][j] + BM.mat[i][j]
            return CM
        else:
            print("Matrixs' size should be in the same size")
            return None

    def sub(self, m):
        """return a new Matrix object after substraction"""
        if nrows_A==nrows_B and ncols_A==ncols_B:
            for i in range(self.nrows):
                for j in range(self.ncols):
                    CM.mat[i][j] = AM.mat[i][j] - BM.mat[i][j]
            return CM
        else:
            print("Matrixs' size should be in the same size")
            return None

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        CM = Matrix(self.nrows, m.ncols)
        for i in range(self.nrows):
            for j in range(m.ncols):
                CM.mat[i][j] = 0
                for p in range(self.nrows):
                    CM.mat[i][j] = CM.mat[i][j] + AM.mat[i][p] * BM.mat[p][j]
        return CM

    def transpose(self):
        """return a new Matrix object after transpose"""
        CM = Matrix(self.nrows, self.ncols)
        for i in range(self.nrows):
            for j in range(self.ncols):
                CM.mat[j][i] = self.mat[i][j] 
        return CM
    
    def display(self):
        """Display the content in the matrix"""
        for i in range(self.nrows):
            for j in range(self.ncols):
                print(self.mat[i][j],end=' ')
            print('')
    
## main ##
#矩陣Ａ
nrows_A=int(input("Enter A matrix's row: "))
ncols_A=int(input("Enter A matrix's cols: "))
AM=Matrix(nrows_A,ncols_A)
print('Matrix A('+str(nrows_A)+','+str(ncols_A)+'):')
AM.display()
print('')


#矩陣B
nrows_B=int(input("Enter B matrix's row: "))
ncols_B=int(input("Enter B matrix's cols: "))
BM=Matrix(nrows_B,ncols_B)
print('Matrix B('+str(nrows_B)+','+str(ncols_B)+'):')
BM.display()
print('')

#A+B
print('======A + B======')
CM=AM.add(BM)
if CM != None:
    CM.display()
print('')

#A-B
print('======A - B======')
CM=AM.sub(BM)
if CM != None:
    CM.display()
print('')

#A*B
print('======A * B======')
CＭ = AM.mul(BM)
CＭ.display()
print('')

#轉置
print('======the tranpose of A * B======')
CＭ = CＭ.transpose()
CＭ.display()
