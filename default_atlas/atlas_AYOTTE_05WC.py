#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

from collections import OrderedDict

import atlas1d
from atlas1d.Dataset import Dataset

import atlas_AYOTTE

####################################
# References for AYOTTE/05WC atlas
####################################

dir_references = os.getenv('SCM_REFERENCES')

subcase = '05WC'

tmp = OrderedDict([
       ('LES'     ,  {'ncfile': os.path.join(dir_references, 'AYOTTE/AYOTTE{0}_LES_MESONH_RR.nc'.format(subcase))     , 'line': 'k'}),
       ('LES_csam',  {'ncfile': os.path.join(dir_references, 'AYOTTE/AYOTTE{0}_LES_MESONH_RR_csam.nc'.format(subcase)), 'line': 'k.'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='AYOTTE',subcase=subcase,ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

########################################
# Configuration file for AYOTTE/05WC atlas
########################################

diagnostics = atlas_AYOTTE.diagnostics
