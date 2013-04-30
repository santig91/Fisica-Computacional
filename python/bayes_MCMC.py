import numpy as np
import math
import matplotlib.pyplot as plt



obs_data=np.loadtxt("obs_data.dat")
x_obs=obs_data[:,0]
y_obs=obs_data[:,1]

plt.scatter(x_obs,y_obs)
plt.savefig("bayes.png")
plt.show()
