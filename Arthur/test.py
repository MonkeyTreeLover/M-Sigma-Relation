import os
import sys

import csv 
import astropy

from astropy.io import fits
from astropy.table import Table
from astropy.io import ascii

import numpy as np

File = "m-sig_table_con_tc.csv"
data = ascii.read(File) 
#print(data[0])


data_10 = data[:10]
print(data_10[-1])
data_10.add_row(data[11])
print(data_10[-1])