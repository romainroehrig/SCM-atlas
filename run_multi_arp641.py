#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os, sys
sys.path = ['./utils/','./config/'] + sys.path

from collections import OrderedDict

from Model import Model
from Simulation import Simulation
from MultiAtlas import MultiAtlas

dir_atlas = os.path.dirname(os.path.realpath(__file__)) + '/MesAtlas/'

cases = ['ARMCU',]
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
model2 = Model(name='arp641',binVersion='arp641',levgrid='L91',tstep=300)
model3 = Model(name='arp641-60s',binVersion='arp641',levgrid='L91',tstep=60)
model4 = Model(name='arp641-60s-L115',binVersion='arp641',levgrid='L115_ARMCU',tstep=60)
model5 = Model(name='arp641-60s-L138',binVersion='arp641',levgrid='L138_ARMCU',tstep=60)

print 'Initialize simulations'
simulations = OrderedDict()
for case in cases:
    simulations[case] = OrderedDict()
    for subcase in subcases[case]:
        simulations[case][subcase] = [
                Simulation(name='V631', model= model1, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V631/arp631d_CMIP6_300s/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase),line='r'),
                Simulation(name='V641', model= model2, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V641/arp641_CMIP6_300s/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase),line='b'),
                Simulation(name='V641-NOPBLE', model= model2, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V641/arp641_CMIP6_300s_nolpble/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase),line='g'),
                Simulation(name='V641-NOPBLE-60s', model= model3, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V641/arp641_CMIP6_60s_nolpble/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase),line='magenta'),
                Simulation(name='V641-NOPBLE-60s-L115', model= model4, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V641/arp641_CMIP6_60s_L115_nolpble/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase),line='cyan'),
                Simulation(name='V641-NOPBLE-60s-L138', model= model5, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V641/arp641_CMIP6_60s_L138_nolpble/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,subcase),line='orange'),
                                    ]
print 'Initialize Atlas'
atlas = MultiAtlas('V641',simulations=simulations,root_dir=dir_atlas)
#atlas.info()


print 'Running'
# (Re)Run a subset of atlas cases
#atlas.run(cases=['IHOP',])
# Run atlas for all cases
atlas.run()

# Prepare pdf files assembling atlas diagnostics
print 'Preparing pdf files for each case'
atlas.topdf()

# Prepare html interface for atlas of all cases
print 'Preparing html interface'
atlas.tohtml()
