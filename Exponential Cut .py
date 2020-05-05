
# coding: utf-8

# ## Importing Packages

# In[19]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mlp
mlp.style.use("ggplot")


# ## Constants

# In[20]:


n_0 = 10**11
k = 100
e = np.linspace(1,10**6,100)
cutoff = 10**4


# ## Ploting the figure

# In[38]:


fig = plt.figure(figsize=(15,12))
#plot alpha = 2.2

ax1 = fig.add_subplot(331)
ax1.plot(e, n_0 *(e/k)**(-2.2),ls = "--", color = "#2413dd",label = "n(e)" )
ax1.plot(e,n_0 *(e/k)**(-2.2)*np.exp(-e/(cutoff)), color = "r",label = "f(e)")
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_title(r'$\alpha = 2.20 $', fontsize = 14)
ax1.set_ylim(10**-45,10**18)
plt.setp(ax1.get_xticklabels(), visible=False)


#plot alpha = 2.92
ax2 = fig.add_subplot(332)
ax2.plot(e, n_0 * (e/k)**(-2.92),ls = "--", color = "#2413dd",label = "n(e)" )
ax2.plot(e,n_0 *(e/k)**(-2.92)*np.exp(-e/(cutoff)), color = "r",label = "f(e)")
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_title("Exponential Cut" +"\n"+r'$\alpha = 2.92 $', fontsize = 14)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
ax2.set_ylim(10**-45,10**18)
#plot alpha = 3.65

ax3 = fig.add_subplot(333)
ax3.plot(e, n_0 * (e/k)**(-3.65),ls = "--", color = "#2413dd",label = "n(e)" )
ax3.plot(e,n_0 *(e/k)**(-3.65)*np.exp(-e/(cutoff)), color = "r",label = "f(e)")
ax3.set_xscale("log")
ax3.set_yscale("log")
ax3.set_title(r'$\alpha = 3.65 $', fontsize = 14)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)
ax3.set_ylim(10**-45,10**18)


#plot alpha = 4.38
ax4 = fig.add_subplot(334)
ax4.plot(e, n_0 * (e/k)**(-4.38),ls = "--", color = "#2413dd",label = "n(e)" )
ax4.plot(e,n_0 *(e/k)**(-4.38)*np.exp(-e/(cutoff)), color = "r",label = "f(e)")
ax4.set_ylabel(r'$ n(e) $'+","+ r'$ f(e) $', fontsize = 20)
ax4.set_xscale("log")
ax4.set_yscale("log")
ax4.set_title(r'$\alpha = 4.38 $', fontsize = 14)
plt.setp(ax4.get_xticklabels(), visible=False)
ax4.set_ylim(10**-45,10**18)

#adding text, constants of formulas 
constants = r'$n_0 = 10^{11} $' +"\n" + r'$ k=100 $' +"\n" + r'$ \alpha $' +" is the title"
boxprop = dict(boxstyle = "round", facecolor = "#ceaf40", alpha = 0.56)
ax4.text(1.432, 4*10**-22, constants, fontsize = 15, bbox = boxprop)

# plot alpha = 5.1

ax5 = fig.add_subplot(335)
ax5.plot(e, n_0 * (e/k)**(-5.1),ls = "--", color = "#2413dd",label = "n(e)" )
ax5.plot(e,n_0 *(e/k)**(-5.1)*np.exp(-e/(cutoff)), color = "r",label = "f(e)")
ax5.set_xscale("log")
ax5.set_yscale("log")
ax5.set_title(r'$\alpha = 5.1 $', fontsize = 14)
ax5.set_ylim(10**-34,10**14)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
ax5.set_ylim(10**-45,10**18)

#plot alpha = 5.82

ax6 = fig.add_subplot(336)
ax6.plot(e, n_0 * (e/k)**(-5.82),ls = "--", color = "#2413dd",label = "n(e)" )
ax6.plot(e,n_0 *(e/k)**(-5.82)*np.exp(-e/(cutoff)), color = "r",label = "f(e)")
ax6.set_xscale("log")
ax6.set_yscale("log")
ax6.set_title(r'$\alpha = 5.82 $', fontsize = 14)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)
ax6.set_ylim(10**-45,10**18)

# plot alpha = 6.55

ax7 = fig.add_subplot(337)
ax7.plot(e, n_0 * (e/k)**(-6.55),ls = "--", color = "#2413dd",label = "n(e)" )
ax7.plot(e,n_0 *(e/k)**(-6.55)*np.exp(-e/(cutoff)), color = "r",label = "f(e)")
ax7.set_xscale("log")
ax7.set_yscale("log")
ax7.set_title(r'$\alpha = 6.55 $', fontsize = 14)
ax7.set_ylim(10**-45,10**18)
#adding text
#find boxprops at ax4 , text section
text = "\n" +"Formulas" + "\n" + r'$n \left( e \right) = n_0 * \left( \frac{e}{k} \right) ^ {-\alpha} $' + "\n" + r'$f \left( e \right) = n_0 * \left( \frac{e}{k} \right) ^ {-\alpha}  *Exp \left( \frac{e}{cutoff} \right) $'
ax7.text(1.432,1*10**-29,text, fontsize =16 , bbox = boxprop)

#plot alpha = 7.28

ax8 = fig.add_subplot(338)
ax8.plot(e, n_0 * (e/k)**(-7.28),ls = "--", color = "#2413dd",label = "n(e)" )
ax8.plot(e,n_0 *(e/k)**(-7.28)*np.exp(-e/(cutoff)), color = "r",label = "f(e)")
ax8.set_xlabel("e", fontsize = 20)
ax8.set_xscale("log")
ax8.set_yscale("log")
ax8.set_title(r'$\alpha = 7.28 $', fontsize = 14)
plt.setp(ax8.get_yticklabels(), visible=False)
ax8.set_ylim(10**-45,10**18)

# plot alpha = 8.0
ax9 = fig.add_subplot(339)
ax9.plot(e, n_0 * (e/k)**(-8),ls = "--", color = "#2413dd",label = "n(e)" )
ax9.plot(e,n_0 *(e/k)**(-8)*np.exp(-e/(cutoff)), color = "r",label = "f(e)")
ax9.set_xscale("log")
ax9.set_yscale("log")
ax9.set_title(r'$\alpha = 8.00 $', fontsize = 14)
plt.setp(ax9.get_yticklabels(), visible=False)
ax9.set_ylim(10**-45,10**18)

plt.legend()
plt.tight_layout(pad = 0.1, h_pad = 0.8, w_pad = -0.2)
plt.savefig("C:/Users/user/Desktop/Mher/Exponential Cut.pdf", dpi =350 )

plt.show()


# #### this is the exponential cut for given formulas,  find them in the plot, all axis have the same scale (logarithmical) and same range _alpha_ varies from 2.2 to 8 
