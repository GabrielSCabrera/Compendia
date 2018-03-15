import matplotlib.pylab as mp
import numpy as np
import os

'''We must create a series of images for our gif'''

t_intervals = 60

x_vals = np.linspace(-6,6,1001)
t_vals = np.linspace(-1,1,t_intervals+1)

def f(x,t):
    return np.exp(-1*((x-(3*t))**2))*(np.sin(3*np.pi*(x-t)))

for i in range(0,t_intervals+1):
    mp.plot(x_vals,f(x_vals,t_vals[i]))
    mp.xlabel("x")
    mp.legend(["f(x,%.3f)"%(t_vals[i])])
    mp.title("Wavepacket Visualization")
    mp.savefig("wave%02d.png"%(i))
    mp.figure()

'''The following will combine all images named frame*.png,
where the * represents any number, into a gif animation'''

os.system('convert -delay 6 wave*.png wave.gif')

'''The following will remove the individual images for neatness'''

for i in range(0,t_intervals+1):
	filename = "wave%02d.png"%(i)
	os.remove(str(filename))
