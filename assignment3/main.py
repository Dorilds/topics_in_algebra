import numpy as np
import random
import pdb # todo remove
import matplotlib.pyplot as plt
import os

class Frog:
    def __init__(self, frog_number):
        self.frog_number = frog_number
        
class Lake:
    def __init__(self, num_pads, num_frogs, num_iterations, name):
        self.pads_dict = self.initialize_pads_dict(num_pads, num_frogs)
        self.transition_matrix = self.initialize_transition_matrix(num_pads)
        self.write_path = name
        # TODO: make distribution a dictionary (pretty print)
        # TODO: keep track of distribution and print. keep track of time. graph results.
        # TODO: table after each of the first 10 turns with N=5 (10 turns), N=10 (20 turns). 100 frogs
        # TODO: measurement of equilibrium. TRACE frog path? net flow across nodes.
        # TODO: keep gif and link
        # TODO: create utils file
        # TODO: clean up constructor
        # TODO: change name to self.write_path

        # Print initial stage
        print('Initial Stage:')
        distribution = self.dict_dist(self.pads_dict)
        self.pretty_print_dict(distribution)
        self.save_histogram_image(distribution, 0, num_frogs, name)
        print('\n')

        if not os.path.exists(name):
            os.makedirs(name)
            
        for i in range(num_iterations):
            print('After {} jumps:'.format(i+1))
            self.increment_time()
            distribution = self.dict_dist(self.pads_dict)
            self.pretty_print_dict(distribution)
            self.save_histogram_image(distribution, i+1, num_frogs, name)
            print('\n')

        e_vals = sorted(self.get_evals(self.transition_matrix), reverse=True)
        print('\nEigenvalues!')    
        [print(e_val) for e_val in e_vals]
        print('\n')

        self.write_evals(e_vals)
    
    def write_evals(self, e_vals):
        f = open('{}/evals.txt'.format(self.write_path), 'w')
        for e_val in e_vals:
            f.write(str(e_val) + '\n')
        f.close()
        
    def get_evals(self, A):
        e_vals, _ = np.linalg.eig(A)
        return e_vals
    
    def save_histogram_image(self, d, num_jumps, num_frogs, name):
        # make histogram
        # save to name/{name}

        plt.title("Frog Distribution After {} jumps".format(num_jumps))
        plt.xlabel('Lilypads')
        plt.ylabel('Number of Frogs')
        plt.ylim((0, num_frogs))
        # plt.bar(d.keys(), d.values(), color='b')

        plt.bar(range(len(d)), d.values(), align='center')
        plt.xticks(range(len(d)), d.keys())
        plt.savefig('{}/{}.png'.format(name, num_jumps), bbox_inches='tight')
        plt.gcf().clear()
        
    def pretty_print_dict(self, d):
        for key, value in sorted(d.items(), key=lambda x: int(x[0][3:])):
            print("{} : {}".format(key, value))
            
    def dict_dist(self, d):
        tuple_list = [(key, len(d[key])) for key in self.pads_dict]
        d = {}
        for pad, num_frogs in tuple_list:
            d[pad] = num_frogs
        return d
        
    def increment_time(self):
        ''' Make all the frogs jump '''
        updated_pads = self.initialize_pads_dict(len(self.pads_dict), 0)
        for pad, frogs_list in self.pads_dict.items():
            for frog in frogs_list:
                next_pad = self.get_next_pad(pad)
                updated_pads[next_pad].append(frog)

        # Update pads dictionary
        for key, value in self.pads_dict.items():            
            self.pads_dict[key] = updated_pads[key][:]
        
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

    q2 = (5, 100, 10, 'q2') # 5 pads, 100 frogs, 10 iterations
    q3 = (10, 100, 20, 'q3') # 10 pads, 100 frogs, 20 iterations
    lake_q2 = Lake(*q2)
    lake_q3 = Lake(*q3)
    
if __name__ == "__main__":
    main()
