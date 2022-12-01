#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

from collections import OrderedDict

import atlas1d
from atlas1d.Model import Model
from atlas1d.Simulation import Simulation

dir_musc = '/Users/romain/MUSC/V2.1.mac'

dir_atlas = '/Users/romain/Atlas1D/V1.0/MyAtlas/'
name_atlas = 'CMIP6'

cases = ['ARMCU','RICO','SANDU']
subcases = OrderedDict([
        ('RICO' , ['SHORT',]),
        ('ARMCU', ['REF',]),
        ('SANDU', ['REF','SLOW','FAST']),
        ])

model = Model(name='arp631diag_CMIP6',binVersion='arp631diag',levgrid='L91',tstep=900)

simulations = OrderedDict()
for case in cases:
    simulations[case] = OrderedDict()
    for subcase in subcases[case]:
        simulations[case][subcase] = [
                Simulation(name='CMIP6',model=model,case=case,subcase=subcase,line='r',
                    ncfile=os.path.join(dir_musc,'simulations/V631/arp631_diag_CMIP6',case,subcase,'Output/netcdf/Out_klevel.nc')),
                        ]
