
import numpy as np
def calculate(x):
    x = np.array(x)
    if len(x) < 9:
        raise ValueError("List must contain nine numbers.")
    
    mat = x.reshape(3,3)

    return{
        'mean': [mat.mean(axis=0).tolist(), mat.mean(axis=1).tolist(), x.mean().tolist()],
        'variance': [mat.var(axis=0).tolist(), mat.var(axis=1).tolist(), x.var().tolist()],
        'standard deviation': [mat.std(axis=0).tolist(), mat.std(axis=1).tolist(), x.std().tolist()],
        'max': [mat.max(axis=0).tolist(), mat.max(axis=1).tolist(), x.max().tolist()],
        'min': [mat.min(axis=0).tolist(), mat.min(axis=1).tolist(), x.min().tolist()],
        'sum': [mat.sum(axis=0).tolist(), mat.sum(axis=1).tolist(), x.sum().tolist()]
        }