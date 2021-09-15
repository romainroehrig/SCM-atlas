# -*- coding:UTF-8 -*-

import sys
sys.path = ['./','../utils/'] + sys.path

from collections import OrderedDict

from Dataset import Dataset

import config_SANDU as config

####################################
# References for SANDU/FAST atlas
####################################

subcase = 'FAST'

tmp = OrderedDict([
       ('SAM',    {'ncfile': '/Users/romain/data/LES/SANDU/SANDU_{0}_LES_SAM_RR.nc'.format(subcase)   , 'line': 'k'}),
       ('DALES',  {'ncfile': '/Users/romain/data/LES/SANDU/SANDU_{0}_LES_DALES_RR.nc'.format(subcase) , 'line': 'b--'}),
       ('DHARMA', {'ncfile': '/Users/romain/data/LES/SANDU/SANDU_{0}_LES_DHARMA_RR.nc'.format(subcase), 'line': 'b-.'}),
       ('UCLA',   {'ncfile': '/Users/romain/data/LES/SANDU/SANDU_{0}_LES_UCLA_RR.nc'.format(subcase)  , 'line': 'g--'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='SANDU',subcase=subcase,ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

########################################
# Configuration file for SANDU/FAST atlas
########################################

diagnostics = config.diagnostics
