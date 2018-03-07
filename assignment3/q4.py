import numpy as np
import os
import matplotlib.pyplot as plt

def initialize_transition_matrix(num_pads):
    ''' Initialize nxn transition matrix '''
    transition_matrix = np.zeros((num_pads, num_pads))
    for row_idx in range(num_pads):
        transition_matrix[row_idx][row_idx-1] = 1/3
        transition_matrix[row_idx][row_idx] = 1/3
        transition_matrix[row_idx][(row_idx+1) % num_pads] = 1/3 # %num_pads for wraparound
    return transition_matrix

def write_evals(e_vals, write_path, i):
    f = open('{}/{}.txt'.format(writepath, i), 'w')
    for e_val in e_vals:
        f.write(str(e_val) + '\n')
    f.close()

def write_eval_dict(d):
    f = open('q4/2nd_max_evals.txt', 'w')
    f.write('N and 2nd highest eval\n')
    for key, val in d.items():
        f.write('N:{} {}\n'.format(key, np.around(val, 3)))
        
def plot_2nd_evals(d):
    plt.title('2nd Largest Eigenvalue vs N')
    plt.xlabel('N')
    plt.ylabel('2nd Largest Eigenvalue')
    plt.ylim((0,1))
    plt.bar(range(len(d)), d.values(), align='center')
    plt.xticks(range(len(d)), d.keys())
    plt.savefig('q4/2nd_max_evals.png', bbox_inches='tight')
    plt.gcf().clear()    

def get_evals(A):
    e_vals, _ = np.linalg.eig(A)
    return e_vals
    
def main():

    second_max_evals = {}
    for n in range(20):
        A = initialize_transition_matrix(n)
        e_vals = sorted(get_evals(A), reverse=True)
        if len(e_vals) < 2:
            continue # no 2nd largest e_val if there is only 1 eval
        second_max_eval = e_vals[1]
        print(second_max_eval)
        second_max_evals[n] = second_max_eval

    if not os.path.exists('q4'):
        os.makedirs('q4')
        
    write_eval_dict(second_max_evals)
    plot_2nd_evals(second_max_evals)

    
if __name__ == "__main__":
    main()

