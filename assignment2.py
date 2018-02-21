import numpy as np
from sympy import Matrix
import pdb # todo remove

def create_random_5x5():
    # return np.random.random_sample((5,5))
    return np.random.randint(10, size=(5,5)) # todo what's a good range?
    
        
def main():
    # create 100 random matrices
    matrix_list = [create_random_5x5() for i in range(100)]
    display_info(matrix_list[0])
    
    pdb.set_trace()

def display_info(A):
    evals = eigenvalues(A)

    evals, evecs = np.linalg.eig(A)

    print('There are {} distinct evals'.format(len(set(evals))))
    print('The largest eval is {}'.format(max(evals)))
    print('The largest eval is {}'.format(min(evals)))

    num_indep_evals = len(set([str(x) for x in evals]))
    print('The algebraic multiplicitiy: {}'.format(num_indep_evals)) 
    num_indep_evecs = len(set([''.join(str(list(evecs[:,i]))) for i in range(evecs.shape[1])]))    
    print('The geometric multiplicitiy: {}'.format(num_indep_evecs))


    import pdb
    pdb.set_trace()

    
def eigenvalues(A):
    e_val, _ = np.linalg.eig(A)
    return e_val


if __name__ == '__main__':
    main()
