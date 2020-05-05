import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import matplotlib as mlp
mlp.style.use('default')

# constants

"""
'power_*'s are constants referring to PowerLaw
'broken_*'s are constants referring to BrokenPowerLaw
'power2_*'s are constants referring to PowerLaw2
'broken2_*'s are constants referring to BrokenPowerLaw2
'smooth_*'s are constants referring to SmoothBrokenLaw
'logparabola_*'s are constants referring to LogParabola
'expcut_*'s are constants referring to ExpCutoff
'bplex_*'s are constants referring to BPLExpCutoff
'pls_*'s are constants referring to PLSuperExpCutoff
'pls2_*'s are constants referring to PLSuperExpCutoff2
'gauss_*'s are constants referring to Gaussian
'band_'*s are constants referring to BandFunction
 """

# powerlaw constants
power_prefactor = 10 ** -9
power_index = -2.1
power_scale = 100

# brokenpowerlaw constants
broken_prefactor = 10 ** -9
broken_index1 = -1.8
broken_index2 = -2.3
break_breakvalue = 10 ** 3

# powerlaw2 constants
power2_integral = 10 ** -4
power2_index = -2
power2_lower = 20
power2_upper = 2 * 10 ** 5

# brokenpowerlaw2 constants
broken2_integral = 10 ** -4
broken2_index1 = -1.8
broken2_index2 = -2.3
broken2_breakvalue = 1000
broken2_lower = 20
broken2_upper = 2 * 10 ** 5

# smoothbrokenpowerlaw constants
smooth_prefactor = 10 ** -6
smooth_index1 = -2.0
smooth_scale = 100
smooth_index2 = -2
smooth_breakvalue = 10 ** 3
smooth_beta = 0.2

# logparabola constants
logparabola_norm = 10 ** -9
logparabola_alpha = 1
logparabola_beta = 2
logparabola_Eb = 300

# expcutoff constants
expcut_prefactor = 50 * 10 ** -9
expcut_index = -2.1
expcut_scale = 100
expcut_break = 10
expcut_p1 = 100
expcut_p2 = 0
expcut_p3 = 0

# bplexpcutoff constants
bplex_prefactor = 10 ** -9
bplex_index1 = -2.1
bplex_index2 = -2.1
bplex_break = 1000
bplex_abs = 10
bplex_p1 = 100 * 1000

# plsuperexpcutoff
pls_prefactor = 10 ** -7
pls_index1 = -1.7
pls_scale = 200
pls_cutoff = 3000
pls_index2 = 1.5

# plsuperexpcutoff2
pls2_prefactor = 10.976 * 10 ** -11
pls2_index1 = 1.436
pls2_scale = 1000
pls2_expfact = 0.001
pls2_index2 = 1

# constantvalue
constant_value = 1

# gaussian constants
gauss_prefactor = 10 ** -9
gauss_mean = 7 * 10 ** 4
gauss_sigma = 10 ** 3

# bandfunction constants
band_norm = 10 ** -9
band_alpha = -1.8
band_beta = -2.5
band_ep = 0.1

# Energy Values

E = np.logspace(1, 5, num=100)


###########################

# Functions

# PowerLaw
def powerlaw(e):
    return power_prefactor * (e / power_scale) ** power_index


# BrokenPowerLaw
brokenpowerlaw = np.array([broken_prefactor * (
        e / break_breakvalue) ** broken_index2 if e < break_breakvalue else broken_prefactor * (
        e / break_breakvalue) ** broken_index1 for e in E])


# PowerLaw2
def powerlaw2(e):
    return (power2_integral * (power2_index + 1) * e ** power2_index) / (power2_upper ** (power2_index + 1) -
                                                                         power2_lower ** (power2_index + 1))


# BrokenPowerLaw2

# Broken2's Prefactor function
def broken2_N0(e):
    if broken2_upper < broken2_breakvalue:
        integrand = (e / broken2_breakvalue) ** broken2_index1
        integral = integrate.cumtrapz(integrand, e, initial=e[0])
        """ 
        integrate.cumtrapz() Cumulatively integrates integrand(e) function, integrates function and then inserts e
        values and gets integrand(e) values
        """
        upper_bound_index = np.abs(e - broken2_upper).argmin()  # takes index of upper bound of a definite integral
        lower_bound_index = np.abs(e - broken2_lower).argmin()  # takes index of lower bound of a definite integral
        """
        np.abs(e-bound) is subtracts all values of an array to get values close to 0
        argmin() takes index of a minimum value of an array, so it means which index is closer to bound index
        """
        definite_integral = integral[upper_bound_index] - integral[lower_bound_index]  # calculating definite integral
        free_param = broken2_integral * definite_integral ** (-1)

    elif broken2_lower > broken2_breakvalue:
        integrand = (e / broken2_breakvalue) ** broken2_index2
        integral = integrate.cumtrapz(integrand, e, initial=e[0])
        upper_bound_index = np.abs(e - broken2_upper).argmin()
        lower_bound_index = np.abs(e - broken2_lower).argmin()
        definite_integral = integral[upper_bound_index] - integral[lower_bound_index]
        free_param = broken2_integral * definite_integral ** (-1)

    else:
        integrand1 = (e / broken2_breakvalue) ** broken2_index1
        integrand2 = (e / broken2_breakvalue) ** broken2_index2
        integral1 = integrate.cumtrapz(integrand1, e, initial=e[0])
        integral2 = integrate.cumtrapz(integrand2, e, initial=e[0])
        upper_bound_index1 = np.abs(e - broken2_breakvalue).argmin()
        lower_bound_index1 = np.abs(e - broken2_lower).argmin()
        upper_bound_index2 = np.abs(e - broken2_upper).argmin()
        lower_bound_index2 = np.abs(e - broken2_breakvalue).argmin()
        definite_integral1 = integral1[upper_bound_index1] - integral1[lower_bound_index1]
        definite_integral2 = integral2[upper_bound_index2] - integral2[lower_bound_index2]
        free_param = broken2_integral * (definite_integral1 + definite_integral2) ** (-1)

    return free_param


# BrokenPowerLaw2 function
def broken2(e):
    broken2_val = broken2_N0(e) * np.array([(x / broken2_breakvalue) ** broken2_index1 if x < broken2_breakvalue else
                                            (x / broken2_breakvalue) ** broken2_index2 for x in e])
    return broken2_val


# SmoothBrokenPowerLaw
def smooth(e):
    return smooth_prefactor * (e / smooth_scale) ** smooth_index1 * (1 + (e / smooth_breakvalue) **
                                                                     (
                                                                             smooth_index1 - smooth_index2) / smooth_beta) ** -smooth_beta


# LogParabola
def logparabola(e):
    return logparabola_norm * (e / logparabola_Eb) ** -(logparabola_alpha +
                                                        logparabola_beta * np.log(e / logparabola_Eb))


# ExpCutoff
expcut = np.array([(e / expcut_scale) ** expcut_index if e < expcut_break else
                   (e / expcut_scale) ** expcut_index * np.exp(- (
                           (e - expcut_break) / expcut_p1 + expcut_p2 * np.log(e / expcut_break) +
                           expcut_p3 * np.log(e / expcut_break) ** 2)) for e in E])

# BPLExpCutoff
"""Preconditions are for giving Python map fucntion a condition, it's function which conditions in BPLEx"""
bplex_precond1 = lambda x: x < bplex_break and x < bplex_abs
bplex_precond2 = lambda x: bplex_break < x < bplex_abs
bplex_precond3 = lambda x: bplex_break > x > bplex_abs
bplex_precond4 = lambda x: x > bplex_break and x > bplex_abs

"""This gives list of True and False conditions, which are conditions using furthermore  """
bplex_cond1 = list(map(bplex_precond1, E))
bplex_cond2 = list(map(bplex_precond2, E))
bplex_cond3 = list(map(bplex_precond3, E))
bplex_cond4 = list(map(bplex_precond4, E))

"""Those are functions that must be returned"""
bplex_func1 = lambda e: bplex_prefactor * (e / bplex_break) ** bplex_index1
bplex_func2 = lambda e: bplex_prefactor * (e / bplex_break) ** bplex_index2
bplex_func3 = lambda e: bplex_prefactor * (e / bplex_break) ** bplex_index1 * np.exp(-(e - bplex_abs) / bplex_index1)
bplex_func4 = lambda e: bplex_prefactor * (e / bplex_break) ** bplex_index2 * np.exp(-(e - bplex_abs) / bplex_index1)

"""picewise takes conditions and gives outputs above defined functions"""
bplex = np.piecewise(E, [bplex_cond1, bplex_cond2, bplex_cond3, bplex_cond4],
                     [bplex_func1, bplex_func2, bplex_func3, bplex_func4])


# PLSuperExpCutoff
def pls(e):
    return pls_prefactor * (e / pls_scale) ** pls_index1 * np.exp(-(e / pls_cutoff) ** pls_index2)


# PLSuperExpCutoff2
def pls2(e):
    return pls2_prefactor * (e / pls2_scale) ** pls2_index1 * np.exp(-pls2_expfact * e ** pls2_index2)


# ConstantValue
def constant(e):
    return np.full(np.shape(e), constant_value)


# Gaussian
def gaussian(e):
    return gauss_prefactor / (gauss_sigma * np.sqrt(2 * np.pi)) * np.exp(
        -(e - gauss_mean) ** 2 / (2 * gauss_sigma ** 2))


# BandFunction
band = np.array([band_norm * (e / 0.1) ** band_alpha * np.exp(-(e / band_ep) / (band_alpha + 2))
                 if e < band_ep * (band_alpha - band_beta) / (band_alpha + 2) else
                 band_norm * (e / 0.1) ** band_beta * ((band_ep / 0.1) * (band_alpha - band_beta) / (band_alpha + 2))
                 ** (band_alpha - band_beta) * np.exp(band_beta - band_alpha) for e in E])

# plotting
fig, ax = plt.subplots(figsize=(16, 8))
fontdict = {"fontsize": 22}

ax.plot(E, powerlaw(E), 'r', label="powerlaw")
ax.plot(E, brokenpowerlaw, 'b', label="brokenpowerlaw")
ax.plot(E, powerlaw2(E), 'g', label="powerlaw2")
ax.plot(E, broken2(E), "#51b3ff", label='brokenpowerlaw2')
ax.plot(E, smooth(E), "gray", label="smoothbrokenpowerlaw")
ax.plot(E, logparabola(E), "black", label="logparabola")
ax.plot(E, expcut, color='#f442d9', label="expcutoff")
ax.plot(E, bplex, color="#f47741", label="bplexpcutoff")
ax.plot(E, pls(E), color='#0950c1', label="plsuperexpcutoff")
ax.plot(E, pls2(E), color="#3e0de0", label="plsuperexpcutoff2")
ax.plot(E, constant(E), color="#c1b109", label='constantvalue')
ax.plot(E, gaussian(E), color="#f47742", label="gaussian")
ax.plot(E, band, color="#a9f441", label="bandfunction")

ax.set_xlabel("E, [eV]", fontdict=fontdict)
ax.set_ylabel(r"$\frac{ dN}{dE}$", fontdict=fontdict)
ax.set_xscale("log")
ax.set_yscale("log")
ax.tick_params(labelsize=15)
ax.set_title("Spectral Models", fontdict=fontdict)
ax.legend()

plt.savefig("/home/mher/Spectral_Models.pdf")
plt.show()

