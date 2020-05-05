
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import matplotlib.pyplot as plt
import numpy as np


# In[9]:


np.random.seed(4563)  
y = np.random.binomial(100,0.5, 1000000)# 10**6 coin tosses of fair coin(probability of success is 50%)  to get 100 heads 

#costimize figure and axes

binhist =plt.figure(figsize=(18,12))
ax = plt.gca()
ax.spines["left"].set_linewidth(4)
ax.spines["bottom"].set_linewidth(4)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

#customizing label tick sizes
xlabel = np.arange(0,100,3) #arangin x label, for numbers of getting heads
plt.xticks(xlabel)
ax.set_xticklabels(xlabel,fontsize = 15)
ax.set_yticklabels(np.arange(0,0.25,0.01), fontsize= 15)

#building histrogam

plt.hist(y, bins =26, histtype="bar",color="#2813dd")

#labelinx axes
plt.ylabel("Probability", fontsize = 23)
plt.xlabel("Number of successes( getting Heads)", fontsize = 23)
plt.title(r'$ \mathregular{Binomial\ distribution\ of\ coin\ tosses\ |\ n = 100,\ p = 0.5,}\ k= 10^{6}$', fontsize = 25,color = "black",verticalalignment = "top" )

#adding a text to plot
text = ' Binomial Distribution Formula '
formula = r'$ P = \binom {n}{k}\mathregular{p^{k}}\mathregular{(1-p)^{n-k}}$'
k, n, p = "k = number of trials", "n = number of successes", 'p =propability of successes in one trial'
plt.text(24,113000, text +'\n'+'\n'+ formula+"\n" + n+'\n'+ k+'\n'+p, fontsize = 15, bbox = {'facecolor' : "#edd431", 'alpha' : 0.6, "boxstyle": "round" })

#saving and showing plot
plt.savefig(fname = "C:/Users/user/Desktop/Mher/Py codes/bindist.pdf",dpi = 400 )
plt.show()


# In[25]:


plot

