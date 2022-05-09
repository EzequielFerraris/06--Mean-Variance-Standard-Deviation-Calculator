import numpy as np

def calculate(list):
    try:
        arr1 = (np.asarray(list)).reshape(3,3)
      
    except ValueError:
        raise ValueError("List must contain nine numbers.")

    final_dict = {
        'mean': [np.mean(arr1, axis = 0).tolist(), np.mean(arr1, axis = 1).tolist(), np.mean(arr1, axis = None).tolist()], 
        'variance': [np.var(arr1, axis = 0).tolist(), np.var(arr1, axis = 1).tolist(), np.var(arr1, axis = None).tolist()],
        'standard deviation': [np.std(arr1, axis = 0).tolist(), np.std(arr1, axis = 1).tolist(), np.std(arr1, axis = None).tolist()],
        'max': [np.amax(arr1, axis = 0).tolist(), np.amax(arr1, axis = 1).tolist(), np.amax(arr1, axis = None).tolist()],
        'min': [np.amin(arr1, axis = 0).tolist(), np.amin(arr1, axis = 1).tolist(), np.amin(arr1, axis = None).tolist()],
        'sum': [np.sum(arr1, axis = 0).tolist(), np.sum(arr1, axis = 1).tolist(), np.sum(arr1, axis = None).tolist()]
        }


    return final_dict
