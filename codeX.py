import numpy as np
#X = [ [1,2,3],4, np.array([5,6])]
#X = [ [1,2,3],4]
X = [ [1,2,3],4, np.array([5,6]),'Khalid']
print('Input = ',X)

def flatten (X):
    Y = []
    for sublist in X:
        if type(sublist) ==  np.ndarray :
           sublist = sublist.tolist()

        if isinstance(sublist, list) or isinstance(sublist, str):
           for item in sublist:
               Y.append(item)
        else: #elif isinstance(sublist,int):
            Y.append(sublist)
    return Y


print('Output = ',flatten (X))

#--------------------------------------------------------
#Input =  [[1, 2, 3], 4, array([5, 6]), 'Khalid']
#Output =  [1, 2, 3, 4, 5, 6, 'K', 'h', 'a', 'l', 'i', 'd']