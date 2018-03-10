import numpy as np
import random
import pdb # todo remove
import matplotlib.pyplot as plt
import os

import frogworld

    
def main():
    np.set_printoptions(precision=1)
    num_pads = 12
    num_frogs = 100

    q2 = (5, 100, 10, 'q2') # 5 pads, 100 frogs, 10 iterations
    q3 = (10, 100, 20, 'q3') # 10 pads, 100 frogs, 20 iterations
    lake_q2 = frogworld.Lake(*q2)
    lake_q3 = frogworld.Lake(*q3)
    
if __name__ == "__main__":
    main()
