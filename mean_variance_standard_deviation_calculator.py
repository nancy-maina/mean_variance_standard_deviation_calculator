import numpy as np

def calculate(list):
  
  list = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# Raising a ValueError Exception when values are less than 9

  if (list.size) < 9:
       raise ValueError("List must contain nine numbers.")
    
#converting the list into a 3x3 matrix
  list = np.reshape(list, (3,3))
  
  
 #returning a dictionary  to contain the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix
  mean1 = np.mean(list, axis = 0)
  mean2 = np.mean(list, axis = 1)
  mean_flattened = np.mean(list.flatten())
  
  var1 = np.var(list, axis = 0)
  var2 = np.var(list, axis = 1)
  var_flattened = np.var(list.flatten())

  std1 = np.std(list, axis = 0)
  std2 = np.std(list, axis = 1)
  std_flattened = np.std(list.flatten())

  max1 = np.max(list, axis = 0)
  max2 = np.max(list, axis = 1)
  max_flattened = np.max(list.flatten())

  min1 = np.min(list, axis = 0)
  min2 = np.min(list, axis = 1)
  min_flattened = np.min(list.flatten())

  sum1 = np.sum(list, axis = 0)
  sum2 = np.sum(list, axis = 1)
  sum_flattened = np.sum(list.flatten())


  thisdict = {

  'mean': [mean1, mean2, mean_flattened],
  'variance': [var1, var2, var_flattened],
  'standard deviation': [std1, std2, std_flattened],
  'max': [max1, max2, max_flattened],
  'min': [min1, min2, min_flattened],
  'sum': [sum1, sum2, sum_flattened]
  }
  print(thisdict)

  

calculate(list)

  


  




