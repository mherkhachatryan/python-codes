from  sympy import *
from sympy.abc import *
import math
import numpy as np
import time
import sys
import pandas as pd

############                                                     ############

#######      Calculating Definite Integral of a given function using trapezium method      #######


#########                                                   ##############     



cuts = 100 #is number of cuts

########################## DataFrame object of aveliable differantiable functions

all_functions = {"Trigonometric": ["sin", "cos",'tan','cot','sec','csec','sinc'],
                    "Trigonometric Inverses": ["asin", "acos",'atan','acot','asec','acsec'," "],
                    'Hyperbolic Functions': [ 'sinh', 'cosh', 'tanh', 'coth'," "," "," "],
                    'Hyperbolic Inverses':['asinh','acosh','atanh','acoth','asech','acsch'," "],
                    "Exponential": ["exp", 'log','ln',"log(base,x)", ' ', " "," "],
                    "Roots":["root","sqrt",'cbrt',' '," "," "," "],
                    "Powers": ["x**n (n is all real numbers)"," "," "," "," "," "," "],
                    "Combinatorical": ['factorial'," "," "," "," "," "," "]}
df = pd.DataFrame(all_functions,index = [" "," "," "," "," "," "," "])
df.columns.name = "Funcion'c classes"
df.index.name = "Functions"
df = df.T 
###############################################


###Defining a function for chechking if user input contains constant numbers
def my_float(s):
    constants = {"pi": 3.14159, "e": 2.71928,'phi':1.61803,'euler': 0.577216, "catalan": 0.915966, 
                 "apery": 1.20206,"khinchin": 2.68545,"glaisher": 1.28243,"mertens":  0.261497,"twinprime": 0.660162}
    if s in constants:
        return constants[s]
    else:
        return float(s)


#####Defining functions which will compute integral using trapezium method

##### Trapezium method fomrula -- Integral(f(x),a,b) = (a-b)/n * ( (y_0+y_n)/2 + y_1+y_2+...+ y_(n-1) )







def integral():
    print("Enter Function to integrate: ", end=" ") 
    function = sympify(input()) #converting string input to sympy expression
    print("Enter lower bound: ", end = " ")
    lower = my_float(input()) #lower bound of definite integral
    print("Enter upper bound: ", end = " ")
    upper = my_float(input()) # upper bound of definite integral
    
    xi = np.linspace(lower,upper,cuts+1) #cutting X axis to n+1 parts, for x0=a<x1<x2<...xi<x(i+1)<...<xn=b
    
    ####### y_i = function(x_i) ########inserting "x"s in function and computing y values, for using trapezium method formula
    ylist = [] 
    for i in range(len(xi)):
        ys = function.subs(x,xi[i]) 
        ylist.append(ys)


    sum2 = 0 #second part of trapezium method sum
    for j in range(1,cuts):
        sum2 = sum2 + ylist[j]
    sum1 = (ylist[0]+ylist[cuts])/2 #first part of trapezium method sum
    result = (upper-lower)*(sum1+sum2)/cuts  #result of an integral
    ####computing error of an integral 
    derivative = diff(function,x,2) #2nd differential of function at given point 
    derresult = derivative.subs(x,(lower-upper)/2) #result of derivative of 
    error = abs((upper-lower)**3*derresult/(12*cuts**12)) #error of definite integral 

    dots = "Integrating....\n"
####typing ^^^ this line alternatly 
    for l in dots:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.045)

    equals = "================\n\n"
 ####typing ^^^ this line alternatly    
    for l in equals:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.045)
    
    #raise this error when bounds give infinity result
    if result == math.inf or result == -math.inf:
        print("Bounds are false")
    else:
        ###printing integral result
        print("Derfinite integral of " + str(function) +" from " +str(lower)+" to "+ str(upper)+" = "+ "%.5f +- %e" %(result, error)+"\n")

            ######## typing equlas alternatly
        for l in equals:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.055)

   
    

try:   ### Trye integral() function if errors are occuring execute excepts
    integral()
    
except TypeError:   ##execute this when TypeError occured , i.e. function typed incorrectly
    print("The Function You have entered does not exist or is not differentiable\nPlease consider that independent variable must be \'x\'!\nTo see list of all differentiable functions please type \"Functions\". \n")
    function_input = input()
    function_list = ["Functions", "Function","functions",'function',"FUNCTIONS",'FUNCTIONS']

    if function_input  in function_list:   #if user input is correct print out DataFrame of aveliable functions, and excecute integral()
        print(df, end = "\n\n")
        integral()
        
    else:  #if user input is incorrect return statement below, which will wait to user input print out function's list and excecute integral()
        print("Please Type \'Functions\' correctly")
        function_input = input()
        print(df, end = "\n\n")
        integral()
except SympifyError:
    print("\nExpression You have entered is not a fully written function or not written correctly.\n")
    integral()
except ValueError:
    print("\nBounds must be numbers.\n")
    integral()
