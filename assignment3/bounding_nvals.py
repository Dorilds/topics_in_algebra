import math
import numpy as np
import matplotlib.pyplot as plt

epsilon = 0.1

evals = {}
evals['4'] = 0.333
evals['5'] = 0.539
evals['6'] = 0.667
evals['7'] = 0.749
evals['8'] = 0.805
evals['9'] = 0.844
evals['10'] = 0.873
evals['11'] = 0.894
evals['12'] = 0.911
evals['13'] = 0.924
evals['14'] = 0.934
evals['15'] = 0.942
evals['16'] = 0.949
evals['17'] = 0.955
evals['18'] = 0.96
evals['19'] = 0.964


min_n = {}
for key, val in evals.items():
    min_n[key] = math.log(epsilon, 10) / math.log(evals[key], 10)

x_vals = []
min_n_list = []

for i in range(4, 20):
    print(i)
    
for i in range(4, 20):
    x_vals.append(i)
    min_n_list.append(min_n[str(i)])
    print(min_n[str(i)])


'''
plt.plot(x_vals, min_n_list)
plt.savefig('min_n.jpg', bbox_inches='tight')
plt.gcf().clear()
'''
'''
plt.title("Converge Time as a func of N".format(min_n))
plt.xlabel('Matrix Size (N)')
plt.ylabel('Number of Iterations to Converge to Epsilon')

plt.bar(range(len(min_n)), min_n.values(), align='center')
plt.xticks(range(len(min_n)), min_n.keys())
plt.savefig('min_n.jpg', bbox_inches='tight')
plt.gcf().clear()
'''
