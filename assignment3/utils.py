import numpy as np
import random
import pdb # todo remove
import matplotlib.pyplot as plt
import os

        
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
        
