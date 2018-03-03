import numpy as np
import random
import pdb # todo remove

class Frog:
    def __init__(self, frog_number):
        self.frog_number = frog_number
        
class Lake:
    def __init__(self, num_pads, num_frogs):
        self.pads_dict = self.initialize_pads_dict(num_pads, num_frogs)
        self.transition_matrix = self.initialize_transition_matrix(num_pads)

        from collections import defaultdict
        d = defaultdict(int)
        
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
        ''' Initialize pads dict and populate with frogs all on pad 0'''
        pads = {}
        for i in range(num_pads):
            pads['pad{}'.format(i)] = []

        for i in range(num_frogs):
            pads['pad0'].append(Frog(i))
        return pads

    def get_next_pad(self, current_pad):
        ''' Given the index of the current pad, uses transition matrix to return next pad'''
        row = self.transition_matrix[current_pad]
        probability_total = np.zeros_like(row)
        for i in range(len(probability_total)):
            if i == 0:
                probability_total[i] = row[i]
                continue
            else:
                probability_total[i] = row[i] + probability_total[i-1]
        rand_prob = random.random()
        for i in range(len(probability_total)):
            if rand_prob < probability_total[i]:
                return i            
        pdb.set_trace()
        raise Exception('disaster')
    
def main():
    np.set_printoptions(precision=1)
    num_pads = 12
    num_frogs = 100

    lake = Lake(num_pads, num_frogs)
    
if __name__ == "__main__":
    main()
