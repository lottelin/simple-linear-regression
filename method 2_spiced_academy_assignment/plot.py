import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from scipy import stats

#task 1: read the x/y data points from csv file
filename = 'datapoints.csv'
rawdata = pd.read_csv(filename)
display(rawdata)

#task 2: create a scatterplot of the data & save as a png
plt.plot(rawdata['x'], rawdata['y'],'o')
plt.savefig('output.png')

#task 3: set the slope intercept form to y=10x + 0
#slope_a = 10
#intercept_b = 0
#can't use map because map only accept function with 1 argument.
def slope_intercept(x, slope_a, intercept_b):
    return slope_a * x + intercept_b

def cal_ypredict(x_values, slope_a, intercept_b):
    predict_y_list = []
    for x in x_values:
        predict_y = slope_intercept(x, slope_a, intercept_b)
        predict_y_list.append(predict_y)
    return predict_y_list 

result = cal_ypredict(rawdata['x'], 10,0)





#task 4: Calculate the Mean Squared Error (MSE) of predict_y and real_y(ytrue) 
def mse_cal(predict_y, real_y):
    difference_list = []
    for idx, y in enumerate(predict_y):
        difference = (y - real_y[idx])**2
        difference_list.append(difference)
    return np.mean(difference_list)

#global level
mse = mse_cal(result, rawdata['y'])
print(mse)

#use built-in module to double check result
mse2 = mean_squared_error(result, rawdata['y'])
print(mse2)




#task 5: Find a value for a that gives the lowest possible MSE and do implementation.
#when a gets bigger, the slope gets steeper, the mse also gets larger.

def find_mse(times):
    a = 10.0
    best_a = 10.0
    best_mse = mse
    for lp in range(times):
        new_result = cal_ypredict(rawdata['x'], a ,0)
        new_mse = mse_cal(new_result, rawdata['y'])
        if new_mse < best_mse:
            best_a = a
            best_mse = new_mse
        a += 0.1
    return best_a, best_mse

print(find_mse(100))





#Task 6: Also modify b in the above procedure.
#to find the better mse within different a values. 
def better_mse(a_lp_times, b_lp_start, b_lp_end):
    a = 10.0
    best_a = 10.0
    b = 0
    best_b = b
    best_mse = mse
    for lp in range(a_lp_times):
        for b in range(b_lp_start, b_lp_end):
            new_result = cal_ypredict(rawdata['x'], a ,b)
            new_mse = mse_cal(new_result, rawdata['y'])
            if new_mse < best_mse:
                best_a = a
                best_b = b
                best_mse = new_mse
        a += 0.1
        b += 1
    return best_a, best_mse, best_b
print(better_mse(100, -2, 2))





#task 7:
"""answer: 
In general:
1. Have clear programming logic.
2. Improve the efficiency
- use less of loops or iterations , less resources , no primitive operations , less time and space consumption.

For this assignment:
Decrease the a value to have the slope to be placed closer to the scatterplots in order to find the better mse.
"""

#extra study - to find the optimist results:
#from scipy import stats
slope, intercept, r, p, std_err = stats.linregress(rawdata['x'], rawdata['y'])
print(stats.linregress(rawdata['x'], rawdata['y']))
