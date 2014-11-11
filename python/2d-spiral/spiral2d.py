import matplotlib.pyplot as plt
import numpy as np
 
theta = np.arange(0., 2., 1./180.)*np.pi
 
plt.polar(20*theta, theta/30)
#plt.polar(theta, [1.4]*len(theta))
 
plt.show()