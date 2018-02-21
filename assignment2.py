import numpy as np
import pdb # todo remove

def create_random_5x5():
    # return np.random.random_sample((5,5))
    return np.random.randint(10, size=(5,5)) # todo what's a good range?
            
def main():
    # create 100 random matrices
    matrix_list = [create_random_5x5() for i in range(100)]
    display_info(matrix_list[0])

    for i, matrix in enumerate(matrix_list):
        info = get_info(matrix)
        print(i)
        if info['algebraic_multiplicity'] != info['geometric_multiplicity']:
            pdb.set_trace()

def get_info(A):
    evals, evecs = np.linalg.eig(A)

    info = {}
    info['max'] = max(evals)
    info['min'] = min(evals)
    info['algebraic_multiplicity'] = len(set([str(x) for x in evals]))
    info['geometric_multiplicity'] = len(set([''.join(str(list(evecs[:,i]))) for i in range(evecs.shape[1])]))
    return info
    
def display_info(A):
    ''' Print multiplicities, max/min evals
    '''
    info = get_info(A)
    print('There are {} distinct evals'.format(info['algebraic_multiplicity']))
    print('The largest eval is {}'.format(info['max']))
    print('The largest eval is {}'.format(info['min']))
    print('The algebraic multiplicitiy: {}'.format(info['algebraic_multiplicity']))
    print('The geometric multiplicitiy: {}'.format(info['geometric_multiplicity']))

if __name__ == '__main__':
    main()
