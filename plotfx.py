# Fiona O'Riordan, 17 March 2019, Module 52445, Problem Set, Question 10
# Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].
# Adapted from:
# http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
# https://www.montereyinstitute.org/courses/DevelopmentalMath/TEXTGROUP-15-19_RESOURCE/U17_L2_T2_text_final.html
# https://matplotlib.org/users/pyplot_tutorial.html
# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.arange.html
# https://stackoverflow.com/questions/44041021/how-to-plot-y-1-x-as-a-single-graph
# To Do/try (time permitting):
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

import numpy as np
import matplotlib.pyplot as plt

# Create a function that reads the value of x and returns x squared
def f(x):
    return x*x

# Create a function that reads in the value of x and returns 2 to the power of x
def f2(x):
    return 2**x
# create a range with interval starting at and including the
# the default value of 0, stopping at 5 but not including 5,
# use default 1 as the distance between each interval 
x = np.arange(5)

# plt.subplot(212)
plt.plot(x,f(x), f2(x))
# x axis is from 0 to 5, y axis is from 0 to 18 with intervals of 1
plt.axis([0, 5, 0, 18], 1)
# label the y axis
plt.xlabel('x axis')
# label the x axis
plt.ylabel('y axis')
# create a graph title
plt.title('Problem Set Q10 Graph2')
# create a legend on the graph
plt.legend(['X squared', '2^​x'])

# display the graph
plt.show()
