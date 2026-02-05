import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    
    calculations = {
  'mean': [],
  'variance': [],
  'standard deviation': [],
  'max': [],
  'min': [],
  'sum': []
}
    matrix = np.array(list).reshape(3,3)

    calculations['mean'].append(matrix.mean(axis=0).tolist())
    calculations['mean'].append(matrix.mean(axis=1).tolist())
    calculations['mean'].append(float(matrix.mean()))
    calculations['variance'].append(matrix.var(axis=0).tolist())
    calculations['variance'].append(matrix.var(axis=1).tolist())
    calculations['variance'].append(float(matrix.var()))
    calculations['standard deviation'].append(matrix.std(axis=0).tolist())
    calculations['standard deviation'].append(matrix.std(axis=1).tolist())
    calculations['standard deviation'].append(float(matrix.std()))
    calculations['max'].append(matrix.max(axis=0).tolist())
    calculations['max'].append(matrix.max(axis=1).tolist())
    calculations['max'].append(int(matrix.max()))
    calculations['min'].append(matrix.min(axis=0).tolist())
    calculations['min'].append(matrix.min(axis=1).tolist())
    calculations['min'].append(int(matrix.min()))
    calculations['sum'].append(matrix.sum(axis=0).tolist())
    calculations['sum'].append(matrix.sum(axis=1).tolist())
    calculations['sum'].append(int(matrix.sum()))
    # print(calculations)
    return calculations

calculate([0,1,2,3,4,5,6,7,8])