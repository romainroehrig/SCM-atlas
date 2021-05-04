#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os, sys
sys.path = ['./utils/','./config/'] + sys.path

from collections import OrderedDict

from Model import Model
from Simulation import Simulation
from MultiAtlas import MultiAtlas

dir_atlas = os.path.dirname(os.path.realpath(__file__)) + '/MesAtlas/'

cases = ['GABLS1','AYOTTE','IHOP','BOMEX','RICO','ARMCU','SANDU']
#cases = ['SANDU']
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

#print 'Initialize model'
model1 = Model(name='arp631',binVersion='arp631d',levgrid='L91',tstep=300)

print 'Initialize simulations'
simulations = OrderedDict()
for case in cases:
    simulations[case] = OrderedDict()
    for subcase in subcases[case]:
        if case == 'GABLS1':
            simulations[case][subcase] = [
                    Simulation(name='V631', model= model1, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V631/arp631-GABLS4-OA_CMIP6_300s/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase),line='r'),
                    Simulation(name='V631_defv1', model= model1, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V631_defv1/defv1_arp631-GABLS4-OA_CMIP6_300s/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase),line='b'),
                    ]
        else:
            simulations[case][subcase] = [
                    Simulation(name='V631', model= model1, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V631/arp631d_CMIP6_300s/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase),line='r'),
                    Simulation(name='V631_defv1', model= model1, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V631_defv1/defv1_arp631d_CMIP6_300s/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase),line='b'),
                    ]

print 'Initialize Atlas'
atlas = MultiAtlas('V631_defv1',simulations=simulations,root_dir=dir_atlas)
#atlas.info()


print 'Running'
# (Re)Run a subset of atlas cases
atlas.run(cases=['BOMEX',])
# Run atlas for all cases
#atlas.run()

# Prepare pdf files assembling atlas diagnostics
print 'Preparing pdf files for each case'
atlas.topdf()

# Prepare html interface for atlas of all cases
print 'Preparing html interface'
atlas.tohtml()
