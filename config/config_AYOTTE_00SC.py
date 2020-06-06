# -*- coding:UTF-8 -*-

import sys
sys.path = ['./','../utils/'] + sys.path

from collections import OrderedDict

import cdtime
from matplotlib import cm # for colormaps

from Dataset import Dataset

import config_AYOTTE as config

####################################
# References for AYOTTE/00SC atlas
####################################

subcase = '00SC'

tmp = OrderedDict([
       ('LES'     ,  {'ncfile': '/Users/romainroehrig/data/LES/AYOTTE/AYOTTE{0}_LES_MESONH_RR.nc'.format(subcase)     , 'line': 'k'}),
       ('LES_csam',  {'ncfile': '/Users/romainroehrig/data/LES/AYOTTE/AYOTTE{0}_LES_MESONH_RR_csam.nc'.format(subcase), 'line': 'k.'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='AYOTTE',subcase=subcase,ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

########################################
# Configuration file for AYOTTE/00SC atlas
########################################

diagnostics = config.diagnostics
