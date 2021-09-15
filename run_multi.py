#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os, sys
sys.path = ['./utils/','./config/'] + sys.path

import warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(format='%(asctime)s - %(name)30s - %(levelname)s - %(message)s', level=logging.INFO)
#logging.basicConfig(format='%(asctime)s - %(name)30s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

from collections import OrderedDict

from Model import Model
from Simulation import Simulation
from MultiAtlas import MultiAtlas

dir_atlas = os.path.dirname(os.path.realpath(__file__)) + '/MesAtlas/'

#cases = ['GABLS1','AYOTTE','IHOP','BOMEX','RICO','ARMCU','SANDU','ASTEX']
cases = ['ARMCU', 'RICO', 'SANDU']
cases = ['ARMCU','RICO']
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

logger.info('Initialize model')
model = Model(name='arp631.diag_CMIP6',binVersion='arp631.diag',levgrid='L91',tstep=900)
#model2 = Model(name='arp631.GABLS4.OA',binVersion='arp631.GABLS4.OA',levgrid='L91',tstep=300)

logger.info('Initialize simulations')
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
logger.info('Initialize Atlas')
atlas = MultiAtlas('CMIP6',simulations=simulations,root_dir=dir_atlas)
#atlas.info()


logger.info('Running multi-atlas')
# (Re)Run a subset of atlas cases
#atlas.run(cases=['GABLS1',])
# Run atlas for all cases
atlas.run()

# Prepare pdf files assembling atlas diagnostics
logger.info('Preparing pdf files for each atlas case')
#atlas.topdf()

# Prepare html interface for atlas of all cases
logging.info('Preparing html interface')
atlas.tohtml()
