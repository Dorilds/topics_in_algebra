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
        
        pdb.set_trace()

    def dict_dist(self, d):
        return [(key, len(d[key])) for key in self.pads_dict]
        
    def increment_time(self):
        ''' Make all the frogs jump '''
        updated_pads = self.initialize_pads_dict(len(self.pads_dict), 0)
        for pad, frogs_list in self.pads_dict.items():
            for frog in frogs_list:
                next_pad = self.get_next_pad(pad)
                updated_pads[next_pad].append(frog)

        pdb.set_trace()
        self.pads_dict = updated_pads
        
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

    def get_next_pad(self, pad_name):
        ''' Given the name of the current pad (i.e. 'pad3'), uses transition matrix to return 
        next pad name (i.e. 'pad2' or 'pad3' or 'pad4')'''
        pad_num = int(pad_name[3:]) # convert padnam (i.e. 'pad123') to number (i.e 123)
        
        row = self.transition_matrix[pad_num]
        probability_total = np.zeros_like(row)

        # ith entry in probability_total holds sum(row[0,i]) (including i)
        for i in range(len(probability_total)):
            if i == 0:
                probability_total[i] = row[i]
                continue
            else:
                probability_total[i] = row[i] + probability_total[i-1]

        # Return jth index with prob(transition_matrix[j])
        rand_prob = random.random()
        for i in range(len(probability_total)):
            if rand_prob < probability_total[i]:
                return 'pad{}'.format(i)
        pdb.set_trace()
        raise Exception('disaster')
    
def main():
    np.set_printoptions(precision=1)
    num_pads = 12
    num_frogs = 100

    lake = Lake(num_pads, num_frogs)
    
if __name__ == "__main__":
    main()
