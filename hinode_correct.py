import numpy as np 
from astropy.io import fits 
import sys 

cube_name = sys.argv[1]
output_cube_name = sys.argv[2]

stokes = fits.open(cube_name)[0].data

stokesI = np.copy(stokes[:,:,0,:])
stokesI *= 2
negative = np.where(stokesI < 0.0)
stokesI[negative] += 65536
stokes[:,:,0,:] = stokesI


xxx = fits.PrimaryHDU(stokes)
xxx.writeto(output_cube_name,overwrite=True)