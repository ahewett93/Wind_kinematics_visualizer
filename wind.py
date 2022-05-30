import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import matplotlib
matplotlib.use('Qt5Agg')

'''
This program was written by Alex Hewett during a dynamic meteorology course at the University of Washington.

The program is an educational tool intended to enhance understanding of divergence, vorticity, and deformation.

The program should be run as a script and the user may adjust the winds, divergence, vorticity, and deformation using the provided sliders.
'''

# Set the spatial and wind grids
x = np.arange(-10, 11, 1)
y = np.arange(-10, 11, 1)
xg, yg = np.meshgrid(x,y)
u_m = np.ones([21, 21])
v_m = np.ones([21, 21])

# Inital parameters for the wind
u_0 = 0
v_0 = 0
div = 0
vort = 0
d1 = 0
d2 = 0
# Define the kinematic equations
u = u_0*u_m + div*.5*xg - vort*.5*yg + d1*.5*xg + d2*.5*yg
v = v_0*u_m + div*.5*yg + vort*.5*xg - d1*.5*yg + d2*.5*xg

# Set the inital plot
fig, ax = plt.subplots(figsize=(9, 9))
plt.subplots_adjust(bottom=0.4)
ax.quiver(xg, yg, u, v)
ax.grid()
ax.set_title("Horizontal Wind Field", fontsize=24)

# Define the slider axes
axu_0 = plt.axes([0.25, 0.3, 0.65, 0.03])
axv_0 = plt.axes([0.25, 0.25, 0.65, 0.03])
axdiv = plt.axes([0.25, 0.2, 0.65, 0.03])
axvort = plt.axes([0.25, 0.15, 0.65, 0.03])
axd1 = plt.axes([0.25, 0.1, 0.65, 0.03])
axd2 = plt.axes([0.25, 0.05, 0.65, 0.03])

# Set the sliders
_u_0 = Slider(axu_0, 'u_0', -50, 50, valinit=0, valstep=1)
_u_0.label.set_size(22)
_v_0 = Slider(axv_0, 'v_0', -50, 50, valinit=0, valstep=1)
_v_0.label.set_size(22)
_div = Slider(axdiv, 'divergence', -20, 20, valinit=0, valstep=2)
_div.label.set_size(22)
_vort = Slider(axvort, 'vorticity', -20, 20, valinit=0, valstep=2)
_vort.label.set_size(22)
_d1 = Slider(axd1, 'd1', -20, 20, valinit=0, valstep=2)
_d1.label.set_size(22)
_d2 = Slider(axd2, 'd2', -20, 20, valinit=0, valstep=2)
_d2.label.set_size(22)

def update(val):
    '''
    Updates the quiver plot with the slider values for the wind paramaters
    '''
    u_0 = _u_0.val
    v_0 = _v_0.val
    div = _div.val
    vort = _vort.val
    d1 = _d1.val
    d2 = _d2.val
    # Compute the horizontal winds
    u = u_0*u_m + div*.5*xg - vort*.5*yg + d1*.5*xg + d2*.5*yg
    v = v_0*u_m + div*.5*yg + vort*.5*xg - d1*.5*yg + d2*.5*xg
    # clear the figure and plot new wind field
    ax.clear()
    ax.quiver(xg, yg, u, v)
    ax.grid()
    ax.set_title("Horizontal Wind Field", fontsize=24)

# Call the update function whenever a slider moves    
_u_0.on_changed(update)
_v_0.on_changed(update)
_div.on_changed(update)
_vort.on_changed(update)
_d1.on_changed(update)
_d2.on_changed(update)

plt.show()