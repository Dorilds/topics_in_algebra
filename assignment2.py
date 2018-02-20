import numpy as np
import pdb # todo remove

def create_random_5x5():
    return np.random.random_sample((5,5))
    

        
def main():
    # create 100 random matrices
    matrix_list = [create_random_5x5() for i in range(100)]
    pdb.set_trace()

if __name__ == '__main__':
    main()
