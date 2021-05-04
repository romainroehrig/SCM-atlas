#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os, sys
sys.path = ['./utils/','./config/'] + sys.path

from collections import OrderedDict

from Model import Model
from Simulation import Simulation
from MultiAtlas import MultiAtlas

dir_atlas = os.path.dirname(os.path.realpath(__file__)) + '/MesAtlas/'

cases = ['GABLS1','AYOTTE','IHOP','BOMEX','RICO','ARMCU','SANDU','ASTEX']
subcases = OrderedDict([
        ('GABLS1',['REF']),
        ('AYOTTE',['00SC','00WC','03SC','05SC','05WC','24SC','24SC']),
        ('IHOP',  ['REF',]),
        ('BOMEX', ['REF',]),
        ('RICO' , ['REF',]),
        ('ARMCU', ['REF',]),
        ('SANDU', ['REF','SLOW','FAST']),
        ('ASTEX', ['EUCLIPSE',]),
        ])

print 'Initialize model'
model = Model(name='arp631.diag',binVersion='arp631.diag',levgrid='L91',tstep=300)
model2 = Model(name='arp631.GABLS4.OA',binVersion='arp631.GABLS4.OA',levgrid='L91',tstep=300)

print 'Initialize simulations'
simulations = OrderedDict()
for case in cases:
    simulations[case] = OrderedDict()
    for subcase in subcases[case]:
        if case == 'GABLS1':
            simulations[case][subcase] = [
                    Simulation(name='CMIP6',      model=model2,case=case,subcase=subcase,line='r'),
                                         ]
        else:
            simulations[case][subcase] = [
                    Simulation(name='CMIP6',      model=model,case=case,subcase=subcase,line='r'),
#                    Simulation(name='CMIP6.LPBLE',model=model,case=case,subcase=subcase,line='b'),
                                         ]
print 'Initialize Atlas'
atlas = MultiAtlas('CMIP6',simulations=simulations,root_dir=dir_atlas)
#atlas.info()


print 'Running'
# (Re)Run a subset of atlas cases
#atlas.run(cases=['GABLS1',])
# Run atlas for all cases
#atlas.run()

# Prepare pdf files assembling atlas diagnostics
print 'Preparing pdf files for each case'
atlas.topdf()

# Prepare html interface for atlas of all cases
#print 'Preparing html interface'
#atlas.tohtml()
