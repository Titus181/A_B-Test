import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


np.random.seed(42)
control_group = np.random.normal(loc=10,scale=2,size=100)
experiment_group = np.random.normal(loc=12,scale=2,size=100)

control_mean = np.mean(control_group)
experiment_mean = np.mean(experiment_group)
control_std = np.std(control_group)
experiment_std = np.std(experiment_group)

print("Control Group: Mean = {:.2f}, Std = {:.2f}".format(control_mean,control_std))
print("Experiment Group: Mean = {:.2f}, Std = {:.2f}".format(experiment_mean,experiment_std))

t_statistic, p_value = stats.ttest_ind(control_group,experiment_group)

print("t-statisitc:",t_statistic)
print("p-value:",p_value)

alpha = 0.05
if p_value < alpha:
    print("Statistically significant difference detected.")
else:
    print("No Statistically significant difference detected.")

plt.hist(control_group,alpha=0.5,label='Control Group')
plt.hist(experiment_group,alpha=0.5,label='Experiment Group')
plt.legend(loc='upper right')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('A/B Test')
plt.show()