#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

from collections import OrderedDict

import atlas1d
from atlas1d.Model import Model
from atlas1d.Simulation import Simulation


dir_atlas = '/Users/romain/Atlas1D/V1.0/MesAtlas/'
name_atlas = 'CMIP6'

#cases = ['GABLS1','AYOTTE','IHOP','BOMEX','RICO','ARMCU','SANDU','ASTEX']
#cases = ['ARMCU', 'RICO', 'SANDU']
cases = ['ARMCU']
subcases = OrderedDict([
        ('GABLS1',['REF']),
        ('AYOTTE',['00SC','00WC','03SC','05SC','05WC','24SC','24SC']),
        ('IHOP',  ['REF',]),
        ('BOMEX', ['REF',]),
        ('RICO' , ['SHORT',]),
        ('ARMCU', ['REF',]),
        ('SANDU', ['REF','SLOW','FAST']),
        ('ASTEX', ['EUCLIPSE',]),
        ])

model = Model(name='arp631.diag_CMIP6',binVersion='arp631.diag',levgrid='L91',tstep=900)

simulations = OrderedDict()
for case in cases:
    simulations[case] = OrderedDict()
    for subcase in subcases[case]:
#        if case == 'GABLS1':
#            simulations[case][subcase] = [
#                    Simulation(name='CMIP6',      model=model2,case=case,subcase=subcase,line='r'),
#                                         ]
#        else:
            simulations[case][subcase] = [
                    Simulation(name='CMIP6',model=model,case=case,subcase=subcase,line='r',ncfile='/Users/romain/MUSC/V2.1.mac/simulations/V631/arp631_diag_CMIP6/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase)),
                                         ]
