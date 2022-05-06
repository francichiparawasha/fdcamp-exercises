
#import numpy as np
def calculate(x):
    if x.ndim() < 9:
        raise ValueError("List must contain nine numbers.")
    elif x.ndim()==9:
        print('x')
    else:
        print('Using only the first nine numbers')
        x =np.x[0:8]
    
    mat = x.reshape(3,3)

    return{
        'mean': [mat.mean(axis=0), mat.mean(axis=1), x.mean()],
        'variance': [mat.var(axis=0), mat.var(axis=1), x.var()],
        'standard deviation': [mat.std(axis=0), mat.std(axis=1), x.std()],
        'max': [mat.max(axis=0), mat.max(axis=1), x.max()],
        'min': [mat.min(axis=0), mat.min(axis=1), x.min()],
        'sum': [mat.sum(axis=0), mat.sum(axis=1), x.sum()]
        }


calculate([0,1,2,3,4,5,6,7,8])