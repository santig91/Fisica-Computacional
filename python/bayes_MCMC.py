import numpy as np
import math, random
import matplotlib.pyplot as plt



obs_data=np.loadtxt("obs_data.dat")
x_obs=obs_data[:,0]
y_obs=obs_data[:,1]


def likelihood(y_obs, y_model):
    chi_squared=sum((y_obs-y_model)**2)
    return math.exp(-chi_squared)

def my_model(x_obs, m, b):
    return x_obs*m+b

m_walk=np.empty((0))
b_walk=np.empty((0))

m_walk=np.append(m_walk, random.random())
b_walk=np.append(b_walk, random.random())

n_iterations=20000
for i in range(n_iterations):
    m_prime=np.random.normal(m_walk[i], 0.1)
    b_prime=np.random.normal(b_walk[i], 0.1)

    y_init=my_model(x_obs, m_walk[i], b_walk[i])
    y_prime=my_model(x_obs, m_prime, b_prime)

    alpha=likelihood(y_obs, y_prime)/likelihood(y_obs,y_init)
    if(alpha>=1.0):
        m_walk=np.append(m_walk,m_prime)
        b_walk=np.append(b_walk,b_prime)
    else:
        beta=random.random()
        if(beta<=alpha):
             m_walk=np.append(m_walk,m_prime)
             b_walk=np.append(b_walk,b_prime)
        else:
            m_walk=np.append(m_walk,m_walk[i])
            b_walk=np.append(b_walk,b_walk[i])

average_m=np.average(m_walk)
average_b=np.average(b_walk)

best_y=my_model(x_obs, average_m, average_b)
plt.scatter(x_obs,y_obs)
plt.plot(x_obs,best_y)
plt.show()

