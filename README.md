

## Assignment2.py
### Info Dictionary
The info dictinoary has 4 keys.
    * **max**: stores the maximum eigenvalue from our list of eigenvalues. We use the default Python (max) function to get this, which supposedly only looks at the Real part of a complex number.
    
    * **min**: Ditto, but with min()
    
    * **Default Dictionary**: This is not a key in our info dictionary, but the next two keys (algebraic_multiplicities and associated_evecs) are objects of these types. A default dictionary is a like a regular python dictionary, but every key in the dictionary is initialized to some value that you specify. We use defaultdict(list) and defaultdict(int), which initialize every bucket in the dictionary with a list and (int) 0 respectively. This allows you to do things like someintdefaultdict[randomkey] += 1, or somelistdefaultdict[randomkey].append(25) without having to check if the key is defined and initialize something there if it isn't. Very useful.
    
    * **algebraic_multiplicities**: This is a defaultdict(int) that maps each eigenvalue to the number of times we've seen that eigenvalue. In all the matrices we've tried so far, this has been 1 (unique eigenvalues). This corresponds to the algebraic multiplicity of the eigenvalue.
    
    * **associated_evecs**: This is a defaultdict(list) that maps each eigenvalue to a list of corresponding eigenvectors. In all the matrices we've tried so far, the list has len()==1. This means in all the matrices we've tested so far, each eigenvalue corresponds to a unique eigenvector. This value also corresponds to the geometric multiplicity of the eigenvalue. 
