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

        self.print_initial_stage(num_frogs, wpath) # Print initial stage of frogs/lilypads, pre-jumpsn
        # makes wpath folder if not existing. deletes latex_tables.txt if existing
        utils.clean_dir(wpath) # since we append to the bottom of the file instead of overwriting

        net_flow = []
        current_distribution = self.get_pads_distribution_dict(self.pads_dict)
        for i in range(num_iterations):
            print('After {} jumps:'.format(i+1))
            prev_distribution = current_distribution
            self.increment_time()
            current_distribution = self.get_pads_distribution_dict(self.pads_dict)
            net_flow.append(self.get_net_flow(current_distribution, prev_distribution, i, num_pads, num_frogs))
            utils.pretty_print_dict(current_distribution)
            utils.save_histogram_image(current_distribution, i+1, num_frogs, wpath)
            utils.save_distribution_table(current_distribution, i+1, num_frogs, wpath, i+1)
            print('\n')

        print('NET FLOW')
        print(net_flow)
        utils.write_flow(net_flow, wpath)
        
        e_vals = sorted(utils.get_evals(self.transition_matrix), reverse=True)
        print('\nEigenvalues!')    
        [print(e_val) for e_val in e_vals]
        print('\n')

        utils.write_evals(e_vals, wpath)


    def print_initial_stage(self, num_frogs, wpath):
        # Print initial stage
        print('Initial Stage:')
        distribution = self.get_pads_distribution_dict(self.pads_dict)
        utils.pretty_print_dict(distribution)
        utils.save_histogram_image(distribution, 0, num_frogs, wpath)
        utils.save_distribution_table(distribution, 0, num_frogs, wpath, 0)
        print('\n')
        
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
                    
    def increment_time(self):
        ''' Make all the frogs jump '''
        updated_pads = self.initialize_pads_dict(len(self.pads_dict), 0)
        for pad, frogs_list in self.pads_dict.items():
            for frog in frogs_list:
                next_pad = self.get_next_pad(pad)
                updated_pads[next_pad].append(frog)
        self.pads_dict = updated_pads
        
    def initialize_transition_matrix(self, num_pads):
        ''' Initialize nxn transition matrix for Math 57 Problem 5.6.1 Exploration'''
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

        if num_frogs == None: # option used to flux dict, where we want pads w/ no frogs
            return pads
        
        for i in range(num_frogs):
            pads['pad0'].append(Frog(i))
        return pads

    def get_next_pad(self, pad_name):
        ''' Given the name of the current pad (i.e. 'pad3'), uses transition matrix to return 
        next pad name (i.e. 'pad2' or 'pad3' or 'pad4')'''
        pad_num = int(pad_name[3:]) # convert padnam (i.e. 'pad123') to number (i.e 123)

        # row of transition matrix for current pad. probability_vector[newpad] -> P(jump to newpad)
        probability_vector= self.transition_matrix[pad_num]
        probability_total = np.zeros_like(probability_vector)

        # ith entry in probability_total holds sum(probability_vector[0,i]) (including i)
        for i in range(len(probability_total)):
            if i == 0:
                probability_total[i] = probability_vector[i]
                continue
            else:
                probability_total[i] = probability_vector[i] + probability_total[i-1]

        # Return jth index with prob(transition_matrix[j])
        rand_prob = random.random()
        for i in range(len(probability_total)):
            if rand_prob < probability_total[i]:
                return 'pad{}'.format(i)
        pdb.set_trace()
        raise Exception('disaster')

    def get_pads_distribution_dict(self, d):
        ''' Given pads dict, returns dictionariy mapping [padname] -> # frogs on pad '''
        tuple_list = [(key, len(d[key])) for key in self.pads_dict]
        d = {}
        for pad, num_frogs in tuple_list:
            d[pad] = num_frogs
        return d
