#We must import matplotlib.pylab to plot curves, we can name it mppl
#for the sake of simplicity
import matplotlib.pylab as mppl
import os

#Using any function we define f(x), we can use this module to plot it

def f(x):
    return x**2 + 3*x - 4

'''Here we are creating variables for use later in this file'''

start = 0               #Where the plot begins
stop = 10               #Where the plot ends
points = 9              #How many points there will be between
                        #start and stop
x_label = "x-axis"      #Text displayed on X axis
y_label = "y-axis"      #Text displayed on Y axis
legend = ["Red","Blue"] #Text displayed in "Legend" area respectively
title = "Title"         #Text displayed in "Title" area

rows = 2                #Number of rows in subplot
columns = 1             #Number of columns in subplot

filename = "curve_plot.PNG" #The name of the file we will create

#We can create a list to determine the scale of the graph
#in the format [x-min,x-max,y-min,y-max]

axis = [0,10,0,150]

x = mppl.linspace(start,stop,points)    #We apply the previous
                                        #variables to create an
                                        #array of desired parameters

y = mppl.zeros(len(x))      #We create an empty array of the same
                            #dimensions as x

for i in range(len(x)):     #We fill up array y with the values
    y[i] = f(x[i])          #returned by f(x)

mppl.plot(x,y,"r-")         #Preparing the plot, the third argument
                            #is divided into a letter and either a
                            #'-' or a 'o' which represent a line
                            #or a dot plot, respectively. r is for
                            #red, b is for blue

#Using the 'mppl.hold(on)' command will allow you to create two plots
#in one, whereas using 'mppl.hold(off)' will create a separate plot

mppl.hold("on")         #Continue plotting in same chart
mppl.plot(x,y*2,"bo")

#We can also simply merge the two mppl.plot() arguments, and they
#will fulfill the same function as the previous code.

mppl.hold("off")                #Stop plotting in previous chart
mppl.plot(x,y,"r-",x,y*2,"bo")  #This will replace the first figure
                                #with an identical copy,  but
                                #created with less code

#Decoration commands must go between mppl.plot() and mppl.show() or
#between mppl.plot() and mppl.savefig(), based on whether you want
#to display or save the plot.

mppl.xlabel(x_label)        #Labels the X axis
mppl.ylabel(y_label)        #Labels the Y axis
mppl.legend(legend, loc = 'best')         #Displays a legend in the best location
mppl.axis(axis)             #Determines the plot dimensions
mppl.title(title)           #Displays a title at top of plot

#We can create subdivisions in our charts using mppl.subplot()

mppl.figure()           #Create a new chart window

mppl.subplot(rows,columns,1)
mppl.plot(x,y,"r-")
mppl.subplot(rows,columns,2)
mppl.plot(x,y*2,"bo")

mppl.savefig(filename)      #This will save the last image
mppl.show()                 #Display the plot

os.remove(filename)         #This will remove the saved image

'''HINT: use "semilogy" instead of "plot" for a logarithmic scale'''
