

## Assignment2.py
### Info Dictionary
The info dictionary has 4 keys.

* info[__max__]: stores the maximum eigenvalue from our list of eigenvalues. We use the default Python (max) function to get this, which supposedly only looks at the Real part of a complex number.    

* info[__min__]: Ditto, but with min()   

* info[__algebraic_multiplicities__]: a dictionary that maps each eigenvalue to the number of times (int) we've seen that eigenvalue. In all the matrices we've tried so far, this has been 1 (unique eigenvalues). This corresponds to the algebraic multiplicity of the eigenvalue.    

* info[__associated_evecs__]: a dictionary that maps each eigenvalue to a list of corresponding eigenvectors. In all the matrices we've tried so far, the list has len()==1. This means in all the matrices we've tested so far, each eigenvalue corresponds to a unique eigenvector. The length of this list (the number of corresponding eigenvectors for this eigenvalue) corresponds to the geometric multiplicity of the eigenvalue.

* __Default Dictionary__: This is not a key in our info dictionary, but we used it to compute the previous two keys (algebraic_multiplicities and associated_evecs). A default dictionary is a like a regular python dictionary, but every key in the dictionary is initialized to some value that you specify. We use defaultdict(list) and defaultdict(int), which initialize every bucket in the dictionary with a list and (int) 0 respectively. This allows you to do things like someintdefaultdict[randomkey] += 1, or somelistdefaultdict[randomkey].append(25) without having to check if the key is defined and initialize something there if it isn't. Very useful.    



MatPlotLib Code for Later Ref
```
plt.title("Distribution of maximum eigenvalues with {} matrices".format(n))
plt.xlabel('Eigenvalue')
plt.ylabel('Frequency')
plt.hist(max_eval_list, normed=False, bins=30)
plt.show()

plt.title("Distribution of minimum eigenvalues with {} matrices".format(n))
plt.xlabel('Eigenvalue')
plt.ylabel('Frequency')
plt.hist(min_eval_list, normed=False, bins=30)
plt.show()
```

