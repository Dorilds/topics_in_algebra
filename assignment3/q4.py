import numpy as np

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
    f.write('N and 2nd highest eval')
    for key, val in d.items():
        f.write('{N:} {}'.format(key, val))
        
def plot_2nd_evals(d):
    if not os.path.exists('q4'):
         os.makedirs('q4')
         
    plt.title('2nd Highest Eval vs N')
    plt.xlabel('N')
    plt.ylabel('Eval Value')
    plt.bar(range(len(d)), d.values(), align='center')
    plt.xticks(range(len(d)), d.keys())
    plt.savefig('q4/2nd_max_evals.png', bbox_inches='tight')
    plt.gcf().clear()    

def get_evals(A):
    e_vals, _ = np.linalg.eig(A)
    return e_vals
    
def main():
    2nd_max_evals = {}
    for n in range(3, 30):
        A = initialize_transition_matrix(n)
        e_vals = sorted(self.get_evals(self.transition_matrix), reverse=True)
        if len(e_vals) < 2:
            print("MISSED ONE")
            continue
        2nd_max_eval = e_vals[1]
        print(2nd_max_eval)

    write_eval_dict(2nd_max_evals)
    plot_2nd_evals(2nd_max_evals)

'''
if __name__ == "__main__":
    test()
    main()

'''