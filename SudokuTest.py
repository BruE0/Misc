# only import scipy specific functions, never use "import scipy"
# PROPER USE: "from scipy import XXXXXX"

#import numpy as np
#from scipy import special
#import matplotlib.pyplot as plt

import numpy as np

sudoku = np.array(
        [[1,2,3,6,7,8,9,4,5],
         [5,8,4,2,3,9,7,6,1],
         [9,6,7,1,4,5,3,2,8],
         [3,7,2,4,6,1,5,8,9],
         [6,9,1,5,8,3,2,7,4],
         [4,5,8,7,9,2,6,1,3],
         [8,3,6,9,2,4,1,5,7],
         [2,1,9,8,5,7,4,3,6],
         [7,4,5,3,1,6,8,9,2]])

def sudokutest(test):
    _,count = np.unique(test,return_counts=True)
    if all(np.sum(test,axis=0) == 45) and all(np.sum(test,axis=1) == 45) and all(count == 9):
        for y in [0,3,6]:
            for x in [0,3,6]:
                if ( np.sum(test[y:y+3,x:x+3]) == 45 ):
                    if [y,x] == [6,6]:
                        return True
                else:
                    return False
    return False
                        
print(sudokutest(sudoku))