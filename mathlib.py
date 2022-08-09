


class Mathlib(object):
    def __init__(self):
        pass
    def identity(self, size):
        self.matrix = []
        for i in range(size):
            self.matrix.append([])
            for j in range(size):
                if i == j:
                    self.matrix[i].append(1)
                else:
                    self.matrix[i].append(0)
                    
        return self.matrix
    
    def multiply(self, matrix_list):
        self.matrix = []
        matrix1 = matrix_list[0]
        matrix2 = matrix_list[1]
        
        for i in range(len(matrix1)):
            self.matrix.append([])
            for j in range(len(matrix2[0])):
                self.matrix[i].append(0)
                for k in range(len(matrix2)):
                    self.matrix[i][j] += matrix1[i][k] * matrix2[k][j]
                    
                    
        matrix_list[0] = self.matrix
        matrix_list.pop(1)

        if len(matrix_list) > 1:
            self.multiply(matrix_list)

        return self.matrix
    
    def HorVert(self, matrix):
        matrixFinal = []
        for i in range(len(matrix)):
            matrixFinal.append([matrix[i]])
        return matrixFinal

    def VertHor(self, matrix):
        matrixFinal = []
        for i in range(len(matrix)):
            matrixFinal.append(matrix[i][0])
        return [matrixFinal]
    
    def dot(self, matrix1, matrix2):
        matrixFinal = []
        for i in range(len(matrix1)):
            matrixFinal.append(matrix1[i] * matrix2[i])
        return matrixFinal

    def cross(self, matrix1, matrix2):
        matrixFinal = []
        matrixFinal.append(matrix1[1] * matrix2[2] - matrix1[2] * matrix2[1])
        matrixFinal.append(matrix1[2] * matrix2[0] - matrix1[0] * matrix2[2])
        matrixFinal.append(matrix1[0] * matrix2[1] - matrix1[1] * matrix2[0])
        return matrixFinal

    def add(self, matrix1, matrix2):
        matrixFinal = []
        for i in range(len(matrix1)):
            matrixFinal.append(matrix1[i] + matrix2[i])
        return matrixFinal
    
    def substract(self, matrix1, matrix2):
        matrixFinal = []
        for i in range(len(matrix1)):
            matrixFinal.append(matrix1[i] - matrix2[i])
        return matrixFinal
    
    def norm(self, x):
        c = x[0] ** 2 + x[1] ** 2 + x[2] ** 2
        c = c * 1.0

        if c >= 0:
            p = c
            i = 0

            while i != p:
                i = p
                p = (c / p + p) / 2
        else:
            print("Número negativo")
        h = [int(x[0] / p), int(x[1] / p), int(x[2] / p)]
        return c
    