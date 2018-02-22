import numpy as np
from collections import defaultdict
import sys
import pdb
import matplotlib.pyplot as plt

def create_random_5x5():
    ''' Return 5x5 matrix with random numbers pulled from discrete uniform distribution
    '''
    # return 10*np.random.random_sample((5,5)) # continuous distribution
    return np.random.randint(10, size=(5,5))  # discrete distribution
            
def main():

    n = int(input('How many random matrices would you like to create?\n'))

    # create a list of n 5x5 random matrices
    matrix_list = [create_random_5x5() for i in range(n)]

    # For every matrix in our matrix list
    for i, matrix in enumerate(matrix_list):
        # Call get_info(), which returns a python dictionary called info.
        # It has the keys max, min, algebraic_multiplicities, associated_evecs
        # Read more about each of the keys in the readme
        # GoTo: https://github.com/WilliamCarlos/topics_in_algebra
        info = get_info(matrix)

        # For each e_val we have
        for e_val in info['algebraic_multiplicities']:
            geometric_multiplicity = len(info['associated_evecs'][e_val])
            # check if the alg-multiplicity equals geo-multiplicity
            if info['algebraic_multiplicities'][e_val] != geometric_multiplicity:
                print('The {}th matrix is not diagonalizable! This is a first.'.format(i))
                pdb.set_trace()
            # check if our e_vals or e_vecs are non_unique. AKA non-one alg/geo multiplicity
            if info['algebraic_multiplicities'][e_val] > 1 or  geometric_multiplicity > 1:
                print('Greater than 1 alg/geo multiplicity! This is a first')
                pdb.set_trace()

    # If we haven't triggered the two if statements above, we know all the matrices
    # We have tried so far have been diagonalizable. Further, the alg/geo multiplicity
    # for all the e_vals in the matrices is 1. 
    print('\n****************************************************************************'\
          '\nAll {} randomly created matrices are diagonalizable (algebraic multiplicity' \
          ' is equal to the geometric multiplicity for all eigenvalues). \n' \
          '****************************************************************************'.format(n))

    # User Interaction Loop. Option to display more info about any matrix in our matrix_list.
    while True:
        more_info = input('\nThere are {} random matrices. Type a number in range [0,{}] '\
                          "to display more info about that matrix. Enter 'exit' to exit \n".format(n,n-1))
        if more_info == 'exit':
            sys.exit(0)            
        display_info(matrix_list[int(more_info)])        
    
def get_info(A):
    ''' Returns info dictionary w/ 4 keys. Keys described in readme.md
    '''
    # get evals, evecs of the matrix numpy numpy
    # evals is a column vector. evecs is a 5x5 matrix, with each column being an evec.
    # So the ith eval is evals[i] and the corresponding evec for that eval is evecs[:i]
    # Numpy indexing is always matrix[row][col]
    evals, evecs = np.linalg.eig(A)    
    
    info = {}
    info['max'] = max(evals) 
    info['min'] = min(evals)

    # initialize dictionary that will map eval to # times we have seen that eval
    algebraic_multiplicities = defaultdict(int)    
    # initialize dictionary that will map eval a list of corresponding evecs
    associated_evecs = defaultdict(list)

    # populate both dictionaries
    for e_val in evals:
        algebraic_multiplicities[e_val] += 1
        associated_evecs[e_val].append(e_val)

    # type-cast back into regular dictionaries before adding to info dictionary
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



