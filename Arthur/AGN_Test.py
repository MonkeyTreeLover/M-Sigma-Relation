from astroquery.vizier import Vizier
import numpy as np
from astropy.table import Table, vstack
from astropy.io import fits

#https://wwwmpa.mpa-garching.mpg.de/SDSS/DR4/Data/agncatalogue.html
"""
Column 1 	Plate ID 	
Column 2 	Mean Julian Date 	
Column 3 	Fiber ID 	
Column 4 	Right Ascencion in desimal degrees 	
Column 5 	Declination in desimal degrees 	
Column 6 	Redshift 	
Column 7 	The logarithm of the [O III] 5007 luminosity 	Solar luminosities
Column 8 	The logarithm of the extinction corrected [O III] 5007 luminosity 	Solar luminosities
Column 9 	log [O III]5007/Hbeta 	
Column 10 	log [NII]/Halpha 	
Column 11 	Log (Stellar Mass) described here 	Solar masses
Column 12 	Log Stellar Surface Mass Density 	Solar masses/kpc^2
Column 13 	The concentration index (R90/R50) 	
Column 14 	D_n(4000) (corrected for [Ne III]3869 contamination) 	
Column 15 	Hdelta_A, emission corrected 	Ångström
Column 16 	Velocity dispersion 	km/s
"""

"""
vizier = Vizier()

vizier(catalog="AGN").get_catalog_metadata()
catalog_list = Vizier.find_catalogs('galaxies active')

for k, v in catalog_list.items():

    print(k, ":", v.description)
"""

fileName = "agn.dat_dr4_release.v2"
collums = ("Plate ID", "Mean Julian Date", "Fiber ID", "RA", "DEC",	"z",
           "Log l", "log extinction", "Log [O III]5007/Hbeta",	
           "log [NII]/Halpha", "Log M", "Log Stellar Surface Mass Density", 
           "R90/R50", "D_n(4000)", "Hdelta_A", "sigma")

with open(fileName, "r") as file:
    data = file.readlines()#.split("\n")
    
data = [' '.join(i.split()) for i in data]
data = [i.split(" ") for i in data] 

data = np.array(data, dtype=float)

table = Table(data, names=collums)

# Speichern als FITS-Datei
table.write('star_data.fits', format='fits', overwrite=True)