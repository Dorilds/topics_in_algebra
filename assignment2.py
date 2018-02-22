import numpy as np
from collections import defaultdict
import sys
import pdb
import matplotlib.pyplot as plt

def create_random_5x5():
    ''' Return 5x5 matrix with random numbers pulled from discrete uniform distribution
    '''
    return np.random.randint(10, size=(5,5)) 
            
def main():

    n = int(input('How many random matrices would you like to create?\n'))

    # create a list of matrix 5x5 random matrices
    matrix_list = [create_random_5x5() for i in range(n)]
    max_eval_list = [] # List of max e_vals. Used later to graph distribution.
    min_eval_list = [] # List of min e_vals. Used later to graph distribution.

    # For every matrix in our matrix list
    for i, matrix in enumerate(matrix_list):
        # Call get_info(), which returns a python dictionary called info.
        # It has the keys max, min, algebraic_multiplicities, associated_evecs
        # Read more about each of the keys in the readme
        # GoTo: https://github.com/WilliamCarlos/topics_in_algebra
        info = get_info(matrix)
        max_eval_list.append(info['max'])
        min_eval_list.append(info['min'])
        for e_val in info['algebraic_multiplicities']:
            geometric_multiplicity = len(info['associated_evecs'][e_val])
            if info['algebraic_multiplicities'][e_val] != geometric_multiplicity:
                print('The {}th matrix is not diagonalizable! This is a first.'.format(i))
                pdb.set_trace()

            if info['algebraic_multiplicities'][e_val] > 1 or  geometric_multiplicity > 1:
                pdb.set_trace()

    print('\n****************************************************************************'\
          '\nAll {} randomly created matrices are diagonalizable (algebraic multiplicity' \
          ' is equal to the geometric multiplicity for all eigenvalues). \n' \
          '****************************************************************************'.format(n))

    ''' Plot Graphs
    plt.title("Distribution of maximum eigenvalues with {} matrices".format(n))
    plt.xlabel('Eigenvalue')
    plt.ylabel('Frequency')
    plt.hist(max_eval_list, normed=False, bins=30)
    plt.show()

    plt.title("Distribution of minimum eigenvalues with {} matrices".format(n))
    plt.xlabel('Eigenvalue')
    plt.ylabel('Frequency')
    plt.hist(min_eval_list, normed=False, bins=30)
    plt.show()
    '''
    
    while True:
        more_info = input('\nThere are {} random matrices. Type a number in range [0,{}] '\
                          "to display more info about that matrix. Enter 'exit' to exit \n".format(n,n-1))
        if more_info == 'exit':
            sys.exit(0)            
        display_info(matrix_list[int(more_info)])        
    
def get_info(A):
    evals, evecs = np.linalg.eig(A)    
    
    info = {}
    info['max'] = max(evals) # why discrete? 
    info['min'] = min(evals)

    # maps eval to frequency
    algebraic_multiplicities = defaultdict(int)
    # maps eval to associated evecs
    associated_evecs = defaultdict(list)
    
    for e_val in evals:
        algebraic_multiplicities[e_val] += 1
        associated_evecs[e_val].append(e_val)
    info['algebraic_multiplicities'] = dict(algebraic_multiplicities)
    info['associated_evecs'] = dict(associated_evecs)
               
    return info
    
def display_info(A):
    ''' Print multiplicities, max/min evals
    '''
    info = get_info(A)
    print('\nThe matrix is:\n')
    print(A)
    print('\nThere are {} distinct evals'.format(len(info['algebraic_multiplicities'])))
    print('The largest eval is {}'.format(info['max']))
    print('The smallest eval is {}'.format(info['min']))

    for e_val, freq in info['algebraic_multiplicities'].items():        
        print('The algebraic multiplicitiy of eval {} is {}'.format(e_val, freq))

    for e_val, associated_evecs in info['associated_evecs'].items():
        print('The geometric multiplicitiy of eval {} is {}'.format(e_val, len(associated_evecs)))

if __name__ == '__main__':
    main()
