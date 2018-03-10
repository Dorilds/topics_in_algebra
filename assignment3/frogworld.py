import numpy as np
import random
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
        
        self.print_initial_stage(num_frogs, wpath) # Print initial stage of frogs/lilypads, pre-jumps

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
            self.save_distribution_table(current_distribution, i+1, num_frogs, wpath, i+1)
            print('\n')

        print('NET FLOW')
        print(net_flow)
        self.write_flow(net_flow)
        
        e_vals = sorted(self.get_evals(self.transition_matrix), reverse=True)
        print('\nEigenvalues!')    
        [print(e_val) for e_val in e_vals]
        print('\n')

        self.write_evals(e_vals)

    def save_distribution_table(self, d, num_jumps, num_frogs, wpath, idx):
        ''' Creates latex table of distribution '''
        table_name = 'Table of Number of Frogs per Lilypad after Jump \\#{}'.format(idx)
        s1 = '\\begin{table}[h!] \n \\begin{center} \n '    
        s2 = '\\caption{0} \n'.format('{' + table_name + '}')
        
        s3 = '\\label{tab:table1} \n \\begin{tabular}{l|l} % align left \n \\textbf{LilyPad \\#}' +\
             ' & \\textbf{Number of Frogs}\\\ \n \hline \n'

        table_rows = ''
        for key, value in sorted(d.items(), key=lambda x: int(x[0][3:])):
            table_row = '{} & {} \\\ \n'.format(key, value)
            table_rows += table_row

        table_rows = table_rows[:-4] + '\n'

        s4 = '\\end{tabular} \n \\end{center} \n \\end{table}'
        
        f = open('{}/latex_tables.txt'.format(wpath), 'a+')
        f.write(s1 + s2 + s3 + table_rows + s4)
        f.write('\n\n')
        f.close()
        
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
        return self.mean_squared_error(current_distribution, prev_distribution, num_pads, num_frogs)

    def mean_squared_error(self, current_distribution, prev_distribution, num_pads, num_frogs):
        pads_list = list(current_distribution.keys())
        total_error = 0
        equilibrium_target = num_frogs / num_pads
        for pad in pads_list:
            pad_net_change = abs((current_distribution[pad] - equilibrium_target)**2)
            total_error += pad_net_change
        return total_error
        
        
    def print_initial_stage(self, num_frogs, wpath):
        # Print initial stage
        print('Initial Stage:')
        distribution = self.dict_dist(self.pads_dict)
        self.pretty_print_dict(distribution)
        self.save_histogram_image(distribution, 0, num_frogs, wpath)
        self.save_distribution_table(distribution, 0, num_frogs, wpath, 0)
        print('\n')


    def write_flow(self, flow_list):
        f = open('{}/flow.txt'.format(self.write_path), 'w')
        f.write('Avg Change in # frogs/lilypad over 10 iterations\n')
        for idx, flow in enumerate(flow_list): 
            f.write('avg change {}->{}: {}\n'.format(idx, idx+1, flow))

        f.write('\nIn plaintext: \n')
        for flow in flow_list: 
            f.write('{}\n'.format(flow))
        f.close()
        
    def write_evals(self, e_vals):
        f = open('{}/evals.txt'.format(self.write_path), 'w')
        f.write('Sorted evals for A\n')
        for e_val in e_vals:
            f.write(str(e_val) + '\n')
        f.close()
        
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
