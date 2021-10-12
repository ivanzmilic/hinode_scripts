import numpy as np 
from astropy.io import fits 
import sys 

cube_name = sys.argv[1]
output_cube_name = sys.argv[2]
SPBSHFT = int(sys.argv[3])

stokes = fits.open(cube_name)[0].data
stokes = stokes.astype('double')


stokesI = np.copy(stokes[:,:,0,:])
if (SPBSHFT > 0):
	stokesI *= 2
negative = np.where(stokesI < 0.0)
stokesI[negative] += 65536.
stokes[:,:,0,:] = stokesI

if (SPBSHFT > 1):
	stokes[:,:,3,:] *= 2

if (SPBSHFT > 2):
	stokes[:,:,1,:] *= 2
	stokes[:,:,2,:] *= 2



xxx = fits.PrimaryHDU(stokes)
xxx.writeto(output_cube_name,overwrite=True)