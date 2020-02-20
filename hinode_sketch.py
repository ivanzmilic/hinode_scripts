import numpy as np 
import matplotlib.pyplot as plt 
import sys 
from astropy.io import fits 

filename = sys.argv[1]

stokes = fits.open(filename)[0].data

stokes = stokes[:100,:100,:,:]

wvls = [27,30,40]

for l in wvls:
	plt.clf()
	plt.cla()
	plt.imshow(stokes[:,:,0,l])
	plt.tight_layout()
	plt.savefig("image"+str(l)+".png",bbox_inches='tight')

test = 45
slit = np.copy(stokes)
slit[:,:test,:,:] = np.amin(stokes[:,:,0,:])
slit[:,test+1:,:,:] = np.amin(stokes[:,:,0,:])

for l in wvls:
	plt.clf()
	plt.cla()
	plt.imshow(slit[:,:,0,l])
	plt.tight_layout()
	plt.savefig("slit"+str(l)+".png",bbox_inches='tight')

plt.clf()
plt.cla()
plt.imshow(stokes[:,test,0,:])
plt.tight_layout()
plt.savefig("spectrum.png",bbox_inches='tight')

plt.clf()
plt.cla()
plt.plot(stokes[test,test,0,:])
plt.tight_layout()
plt.savefig("spectrum_single.png",bbox_inches='tight')

llambda_hinode = np.linspace(6300.87730065,6303.25996109,112)

stokes = fits.open(filename)[0].data
mean = np.mean(stokes[:,:,0,:],axis=(0,1))

atlas = np.loadtxt("atlas_6300.txt",unpack=True)

#fts = np.loadtxt("/home/milic/scratch/FTS-Atlas/file04",unpack=True)

plt.clf()
plt.cla()
plt.plot(llambda_hinode,mean/np.amax(mean),label='HINODE')
plt.plot(atlas[0],atlas[1]/np.amax(atlas[1]),label='Jungfraujoch atlas')
#plt.plot(fts[0],fts[1]/fts[2],label='FTS atlas')
plt.xlim([6301.0,6303.0])
plt.legend()
plt.tight_layout()
plt.savefig("spectrum_comparison.png",bbox_inches='tight')




