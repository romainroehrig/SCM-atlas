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
model = Model(name='arp631',binVersion='arp631d',levgrid='L91',tstep=300)
#model2 = Model(name='arp631.GABLS4.OA',binVersion='arp631.GABLS4.OA',levgrid='L91',tstep=300)

print 'Initialize simulations'
simulations = OrderedDict()
for case in cases:
    simulations[case] = OrderedDict()
    for subcase in subcases[case]:
        simulations[case][subcase] = [
                Simulation(name='REF', model= model, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V631/arp631d_CMIP6_300s/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,'REF'),line='r'),
                Simulation(name='MESONH', model= model, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V631/arp631d_CMIP6_300s/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,'MESONH'),line='b'),
                Simulation(name='E3SM', model= model, case=case, subcase=subcase, ncfile='/Users/romainroehrig/MUSC/last/simulations/V631/arp631d_CMIP6_300s/{0}/{1}/Output/netcdf/Out_klevel.nc'.format(case,'E3SM'),line='g'),
                                    ]
print 'Initialize Atlas'
atlas = MultiAtlas('E3SM',simulations=simulations,root_dir=dir_atlas)
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
