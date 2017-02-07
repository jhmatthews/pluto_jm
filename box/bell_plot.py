import pyPLUTO as pp
from pylab import *
from pretty import *

def pypluto_loc():
	'''print the location of PyPLUTO'''
	return pp.__file__

def plot_jet():
	set_pretty()
	nlinf = pp.nlast_info()
	D = pp.pload(nlinf['nlast'])
	I = pp.Image()
	I.pldisplay(D, D.rho,x1=D.x1,x2=D.x2,label1='$x$',label2='$y$',
	            title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])

	print (I.pldisplay.__doc__)

	# Code to plot field lines. Requires 2 arrays xarr and yarr as
	# the starting point of integration i.e. x and y co-ordinate of the field point.
	I.myfieldlines(D,linspace(D.x1.min(),D.x1.max(),10),linspace(D.x2.min(),D.x2.min(),10),
               colors='w',ls='-',lw=1.5)

	savefig('jet_final.png') # Only to be saved as either .png or .jpg
	# show()
	# D = pp.pload.ReadGridFile(1)


def plot_box():
	set_pretty()
	nlinf = pp.nlast_info()
	D = pp.pload(nlinf['nlast'])
	I = pp.Image()
	I.pldisplay(D, D.rho,x1=D.x1,x2=D.x2,label1='$x$',label2='$y$',
	            title=r'Density $\rho$ [MHD jet]',cbar=(True,'vertical'),figsize=[7,12])

	print (I.pldisplay.__doc__)

	# Code to plot field lines. Requires 2 arrays xarr and yarr as
	# the starting point of integration i.e. x and y co-ordinate of the field point.
	I.myfieldlines(D,linspace(D.x1.min(),D.x1.max(),10),linspace(D.x2.min(),D.x2.min(),10),
               colors='w',ls='-',lw=1.5)

	savefig('box_final.png') # Only to be saved as either .png or .jpg
	# show()
	# D = pp.pload.ReadGridFile(1)

#if __name__ == "__main__":

	
