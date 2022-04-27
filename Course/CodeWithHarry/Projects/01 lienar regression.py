import matplotlib as mpl
import numpy as np
from sklearn import datasets, linear_model

# load and create dataset from diabetes database
diabetes = datasets.load_diabetes()
# check datasets
# print top 5 rows of diabetes dataset
print(diabetes.data[:5])    
# key values
print(diabetes.keys())
'''
['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module']
'''
# show description value
print(diabetes.DESCR)
'''

'''
