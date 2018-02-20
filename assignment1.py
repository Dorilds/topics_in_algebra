import numpy as np
import pdb

def determinant(A):
    return np.linalg.det(A)

def inverse(A):
    return np.linalg.inv(A)

def eigenvectors(A):
    _, e_vec = np.linalg.eig(A)
    return e_vec

def eigenvalues(A):
    e_val, _ = np.linalg.eig(A)
    return e_val

def nullspace(A):
    return np.linalg.nullspace()

def SVD(A):
    U,S,V = np.linalg.svd(A, full_matrices=True)    
    return S,V,D # note: order changed

    
def main():
    A = np.random.rand(10, 10)*10
    pdb.set_trace()

    # determinant, inverse, eigenvalues, basis of null space

if __name__ == '__main__':
    main()

    
