import numpy as np
import random
import utils
import pdb # todo remove
import matplotlib.pyplot as plt
import os

class Frog:
    def __init__(self, frog_number):
        self.frog_number = frog_number
        
class Lake:
    def __init__(self, num_pads, num_frogs, num_iterations, wpath):
        self.pads_dict = self.initialize_pads_dict(num_pads, num_frogs)
        self.transition_matrix = self.initialize_transition_matrix(num_pads)
        self.write_path = wpath
        
        utils.print_initial_stage(num_frogs, wpath) # Print initial stage of frogs/lilypads, pre-jumps

        if not os.path.exists(wpath):
            os.makedirs(wapth)
            
        if os.path.exists(wpath + '/latex_tables.txt'):
            os.remove(wpath + '/latex_tables.txt')

        net_flow = []
        current_distribution = self.dict_dist(self.pads_dict)
        for i in range(num_iterations):
            print('After {} jumps:'.format(i+1))
            prev_distribution = current_distribution
            self.increment_time()
            current_distribution = self.dict_dist(self.pads_dict)
            net_flow.append(self.get_net_flow(current_distribution, prev_distribution, i, num_pads, num_frogs))
            self.pretty_print_dict(current_distribution)
            self.save_histogram_image(current_distribution, i+1, num_frogs, wpath)
            utils.save_distribution_table(current_distribution, i+1, num_frogs, wpath, i+1)
            print('\n')

        print('NET FLOW')
        print(net_flow)
        utils.write_flow(net_flow)
        
        e_vals = sorted(self.get_evals(self.transition_matrix), reverse=True)
        print('\nEigenvalues!')    
        [print(e_val) for e_val in e_vals]
        print('\n')

        utils.write_evals(e_vals)
        
    def get_net_flow(self, current_distribution, prev_distribution, i, num_pads, num_frogs):
        ''' Get '''
        pads_list = list(current_distribution.keys())
        total_net_change = 0
        for pad in pads_list:
            pad_net_change = abs(current_distribution[pad] - prev_distribution[pad])
            total_net_change += pad_net_change
            
        '''
        denom = [pad for pad,_ in current_distribution.items() if current_distribution[pad]!=0]
        denom += [pad for pad,_ in prev_distribution.items() if prev_distribution[pad]!=0]
        denom = len(denom)
        return total_net_change / denom'''

        #return total_net_change / len(pads_list)
        return utils.mean_squared_error(current_distribution, prev_distribution, num_pads, num_frogs)                

        
    def get_evals(self, A):
        e_vals, _ = np.linalg.eig(A)
        return e_vals
    
    def save_histogram_image(self, d, num_jumps, num_frogs, wpath):

        plt.title("Frog Distribution After {} jumps".format(num_jumps))
        plt.xlabel('Lilypads')
        plt.ylabel('Number of Frogs')
        plt.ylim((0, num_frogs))
        # plt.bar(d.keys(), d.values(), color='b')

        plt.bar(range(len(d)), d.values(), align='center')
        plt.xticks(range(len(d)), d.keys())
        plt.savefig('{}/{}.png'.format(wpath, num_jumps), bbox_inches='tight')
        plt.gcf().clear()
        
    def pretty_print_dict(self, d):
        for key, value in sorted(d.items(), key=lambda x: int(x[0][3:])):
            print("{} : {}".format(key, value))
            
    def dict_dist(self, d):
        tuple_list = [(key, len(d[key])) for key in self.pads_dict]
        d = {}
        # convert tuple list to dict
        for pad, num_frogs in tuple_list:
            d[pad] = num_frogs
        return d
        
    def increment_time(self):
        ''' Make all the frogs jump '''
        updated_pads = self.initialize_pads_dict(len(self.pads_dict), 0)
        for pad, frogs_list in self.pads_dict.items():
            for frog in frogs_list:
                next_pad = self.get_ext_pad(pad)
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

        if num_frogs == None: # for flux dict
            return pads
        
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
