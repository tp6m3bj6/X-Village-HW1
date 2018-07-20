import random

from copy import deepcopy
#可測試加法矩陣是否合理
#也可測試乘法矩陣是否合理 [ＭxN]*[NxK] =[M*K]

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
        CM = Matrix(nrows_A, m.ncols) #先利用Ｍatrix 創造一個nrows_A x m.cols的矩陣，等等要用
        if ncols_A==nrows_B:
            for i in range(nrows_A):
                for j in range(ncols_B):
                    CM.mat[i][j] = 0
                    for p in range(ncols_A):
                        CM.mat[i][j] = CM.mat[i][j] + AM.mat[i][p] * BM.mat[p][j]
            return CM
        else:
            print("Matrixs' size should be MxN NxM")
            return None

    def transpose(self):
        """return a new Matrix object after transpose"""
        DM = Matrix(ncols_B, nrows_A)#利用Ｍatrix 創造一個ncols_B x nrows_A 的矩陣
        if ncols_A==nrows_B:
            for i in range(nrows_A):
                for j in range(ncols_B):
                    DM.mat[j][i] = CM.mat[i][j]
            return DM
        else:
            print("Matrixs' size should be MxN NxM")
            return None
    
    
    def display(self):
        """Display the content in the matrix"""
        for i in range(self.nrows):
            for j in range(self.ncols):
                print("%4d"%self.mat[i][j],end='')
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
else:
    pass
print('')

#A-B
print('======A - B======')
CM=AM.sub(BM)
if CM != None:
    CM.display()
else:
    pass    
print('')

#A*B
print('======A * B======')
CＭ=AM.mul(BM)
if CM != None:
    CM.display()
else:
    pass
print('')

#轉置
print('======the tranpose of A * B======')
DＭ=AＭ.transpose()
if DM != None:
   DM.display()
else:
    pass

print('==========Finish==========')
