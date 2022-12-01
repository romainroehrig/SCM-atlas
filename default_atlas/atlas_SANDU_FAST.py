#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

from collections import OrderedDict

import atlas1d
from atlas1d.Dataset import Dataset

import atlas_SANDU

####################################
# References for SANDU/FAST atlas
####################################

dir_references = os.getenv('SCM_REFERENCES')

subcase = 'FAST'

tmp = OrderedDict([
       ('SAM',    {'ncfile': os.path.join(dir_references, 'SANDU/SANDU_{0}_LES_SAM_RR_new.nc'.format(subcase))   , 'line': 'k'}),
       ('DALES',  {'ncfile': os.path.join(dir_references, 'SANDU/SANDU_{0}_LES_DALES_RR_new.nc'.format(subcase)) , 'line': 'b--'}),
       ('DHARMA', {'ncfile': os.path.join(dir_references, 'SANDU/SANDU_{0}_LES_DHARMA_RR_new.nc'.format(subcase)), 'line': 'b-.'}),
       ('UCLA',   {'ncfile': os.path.join(dir_references, 'SANDU/SANDU_{0}_LES_UCLA_RR_new.nc'.format(subcase))  , 'line': 'g--'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='SANDU',subcase=subcase,ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

########################################
# Configuration file for SANDU/FAST atlas
########################################

diagnostics = atlas_SANDU.diagnostics
