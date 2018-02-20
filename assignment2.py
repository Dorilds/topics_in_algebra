import numpy as np
from sympy import Matrix
import pdb # todo remove

def create_random_5x5():
    return np.random.random_sample((5,5))
    return np.random.randint(10, size=(5,5)) # todo what's a good range?
    
        
def main():
    # create 100 random matrices
    matrix_list = [create_random_5x5() for i in range(100)]
    get_info(matrix_list[0])
    
    pdb.set_trace()

def get_info(A):
    evals = eigenvalues(A)
    print('There are {} distinct evals'.format(len(set(evals))))
    print('The largest eval is {}'.format(max(evals)))
    print('The largest eval is {}'.format(min(evals)))

    print('The algebraic multiplicitiy: {}'.format(''' TODO '''))
    print('The geometric multiplicitiy: {}'.format(''' TODO '''))
    print('And hence, the geometric multiplicitiy: {}'.format(''' TODO '''))

    print('Finally, the matrix in jordon normal form: ')

    sympy_matrix = Matrix(A)
    P, J = sympy_matrix.jordan_form()
    print(J)
    import pdb
    pdb.set_trace()

    
def eigenvalues(A):
    e_val, _ = np.linalg.eig(A)
    return e_val


if __name__ == '__main__':
    main()
