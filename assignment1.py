import numpy as np
import pdb

def determinant(A):
    return np.linalg.det(A)

def inverse(A):
    return np.linalg.inv(A)

def eigenvalues(A):
    return np.linalg.eig(A)

def nullspace(A):
    return np.linalg.nullspace()
    
def main():
    A = np.random.rand(10, 10)*10
    pdb.set_trace()
    print("Hello World!")

    # determinant, inverse, eigenvalues, basis of null space

if __name__ == '__main__':
    main()

    
