
# coding: utf-8

# ## *__Importing Packages__*
# 

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.patheffects as path_effects


# ## __Constants__

# In[8]:


f0 = 41.96
t0 = 10.88
tr = np.full((25,),8.03)
td = np.full((25,),1.21)
t = np.linspace(1,25, 25, endpoint=True)


# In[9]:


func = f0 * (np.exp((t-t0)/tr)+np.exp((t0-t)/td))**-1


# ## *Plotting the figure*

# In[31]:


#configuring figure and plot type

plt.figure(figsize=(18,12))
plt.xscale("linear")
plt.yscale("linear")

#labeling plot
plt.title("Exponential Fit", fontsize = 26, fontweight = "semibold")
plt.xlabel("Time, (t) ", fontsize = 23,fontweight = "light")
plt.ylabel("Energy ", fontsize = 23,fontweight = "light")

#configuring axes

ax = plt.gca()
ax.spines["top"].set_linewidth(1.2)
ax.spines["right"].set_lw(1.2)
ax.spines["left"].set_lw(1.2)
ax.tick_params(length = 8)

#adding text to plot

formula = r'$ \mathregular{F_0} \times \left (\mathregular{e^\frac{t-t_0}{t_r}} + \mathregular{e^\frac{t_0-t}{t_d}} \right)$'


plt.text(1,21.6,formula + "\n"+ '$\mathregular{F_0} = 41.96$' + '\n'+'$\mathregular{t_0} = 10.88$' +'\n'+'$\mathregular{t_r} = 8.03$' +'\n'+ '$\mathregular{t_d} = 1.21$',  fontsize = 24, bbox = {"facecolor": "#dbba4c", "alpha": 0.8, "boxstyle": 'round','path_effects': [path_effects.withSimplePatchShadow()]})

#plotting and saving
plt.plot(t,func, c = "#16af38", lw = 3, ls = "--")
plt.savefig("C:/Users/user/Desktop/Mher/Py codes/Exponential Fit.pdf", dpi = 200)
plt.show()

