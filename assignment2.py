import numpy as np
from collections import defaultdict
import pdb # todo remove

def create_random_5x5():
    # return np.random.random_sample((5,5))
    return np.random.randint(10, size=(5,5)) # todo what's a good range?
            
def main():
    # create 100 random matrices
    matrix_list = [create_random_5x5() for i in range(10000)]
    # display_info(matrix_list[0]) TODO

    for i, matrix in enumerate(matrix_list):
        info = get_info(matrix)
        print(i)
        for e_val in info['algebraic_multiplicities']:
            geometric_multiplicity = len(info['associated_evecs'][e_val])
            if info['algebraic_multiplicities'][e_val] != geometric_multiplicity:
                pdb.set_trace()

def get_info(A):
    evals, evecs = np.linalg.eig(A)    
    
    info = {}
    info['max'] = max(evals) # TODO does max/min work on complex? 
    info['min'] = min(evals)

    # maps eval to frequency 
    eval_count = defaultdict(int)
    # maps eval to associated evecs
    associated_evecs = defaultdict(list)
    
    for e_val in evals:
        eval_count[e_val] += 1
        associated_evecs[e_val].append(e_val)
    info['algebraic_multiplicities'] = dict(eval_count)
    info['associated_evecs'] = dict(associated_evecs)
               
    return info
    
def display_info(A):
    ''' Print multiplicities, max/min evals
    '''
    info = get_info(A)
    print('There are {} distinct evals'.format(info['algebraic_multiplicities']))
    print('The largest eval is {}'.format(info['max']))
    print('The smallest eval is {}'.format(info['min']))

    for e_val, freq in info['algebraic_multiplicities']:        
        print('The algebraic multiplicitiy of eval {} is {}'.format(e_val, freq))

    for e_val, associated_evecs in info['associated_evecs']:
        print('The geometric multiplicitiy of {} is {}'.format(e_val, len(associated_evecs)))

if __name__ == '__main__':
    main()
