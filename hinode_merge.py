import numpy as np 
from astropy.io import fits 

import os
import sys

number = int(sys.argv[1])

filenames = []

for file in sorted(os.listdir (".")):
	if file.endswith(".fits"):
		print file
		filenames.append(file)
print len(filenames)

#filenames = filenames[:number]

#print filenames
SLITSIZE = 1024
print filenames[0]
stokes = fits.open(filenames[0])[0].data
stokes = stokes.reshape(1,4,SLITSIZE,112)

filenames=filenames[1:]
for name in filenames:
	stokes_temp = fits.open(name)[0].data
	stokes_temp = stokes_temp.reshape(1,4,SLITSIZE,112)
	stokes = np.concatenate((stokes,stokes_temp),axis=0)

stokes = stokes.transpose(2,0,1,3)
print stokes.shape

output = sys.argv[2]
hdu = fits.PrimaryHDU(stokes)
hdu.header = fits.open(name)[0].header
hdu.writeto(output)



	
