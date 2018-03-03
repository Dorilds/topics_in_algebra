import numpy as np
import pdb # todo remove

class Frog:
    def __init__(self, frog_number):
        self.frog_number = frog_number
        
class Lake:
    def __init__(self, num_pads, num_frogs):
        self.pads_dict = self.initialize_pads_dict(num_pads, num_frogs)
        self.transition_matrix = self.initialize_transition_matrix(num_pads)
        pdb.set_trace()

    def initialize_transition_matrix(self, num_pads):
        ''' Initialize nxn transition matrix '''
        transition_matrix = np.zeros((num_pads, num_pads))
        for row_idx in range(num_pads):
            transition_matrix[row_idx][row_idx-1] = 1/3
            transition_matrix[row_idx][row_idx] = 1/3
            transition_matrix[row_idx][(row_idx+1) % num_pads] = 1/3 # %num_pads for wraparound
        return transition_matrix
    
    def initialize_pads_dict(self, num_pads, num_frogs):
        pads = {}
        for i in range(num_pads):
            pads['pad{}'.format(i)] = []
        return pads
        
def main():
    np.set_printoptions(precision=1)
    num_pads = 12
    num_frogs = 100
    lake = Lake(num_pads, num_frogs)
    
if __name__ == "__main__":
    main()
