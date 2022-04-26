import numpy as np 

def calculate(list):

     if len(list) >= 9:

          arr = np.array(list)

          arr = arr.reshape(3, 3)

          print(arr)

          mean = [arr.mean(axis=0), arr. mean(axis=1), arr.flatten().mean()]

          print(mean)

          

          variance = [arr.var(axis=0), arr. var(axis=1), arr.flatten().var()]

          print(variance)

          

          standard_deviation = [arr.std(axis=0), arr.std(axis=1), arr.flatten().std()]

          print(standard_deviation)

          

          max = [arr.max(axis=0), arr. max(axis=1), arr.flatten().max()]

          print(max)

          

          min = [arr.min(axis=0), arr. min(axis=1), arr.flatten().min()]

          print(min)

          

          sum = [arr.sum(axis=0), arr.sum(axis=1), arr.flatten().sum()]

          print(sum)

          

          calculations = {

  'mean': mean,

  'variance': variance,

  'standard deviation': standard_deviation,

  'max': max,

  'min': min, 

  'sum': sum

  }

          print(calculations)

          return calculations

     else:

          return raise ValueError('List must contain nine numbers.')

         

calculate([0,1,2,3,4,5,6,7,8])

