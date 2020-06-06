#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os, sys
sys.path = ['./utils/','./config/'] + sys.path

from collections import OrderedDict

from Model import Model
from Simulation import Simulation
from Atlas import Atlas

#import config_ARMCU as config
import config_RICO as config

dir_path = os.path.dirname(os.path.realpath(__file__))

model = Model(name='arp631.diag',binVersion='arp631.diag',levgrid='L91',tstep=300)

#simulations = [
#              Simulation(name='CMIP6',      model=model,case='ARMCU',subcase='REF',line='r'),
#              Simulation(name='CMIP6.LPBLE',model=model,case='ARMCU',subcase='REF',line='b'),
#              ]

#atlas = Atlas('test2',references=config.references,simulations=simulations,root_dir=dir_path)
#atlas.init_from_dict(config.diagnostics)
#atlas.info(references=True,simulations=True,groups=True)
#atlas.run()
#atlas.topdf()
#atlas.tohtml()

simulations = [
              Simulation(name='CMIP6',      model=model,case='RICO',subcase='REF',line='r'),
              Simulation(name='CMIP6.LPBLE',model=model,case='RICO',subcase='REF',line='b'),
              ]

atlas = Atlas('test3',references=config.references,simulations=simulations,root_dir=dir_path)
atlas.init_from_dict(config.diagnostics)
#atlas.info(references=True,simulations=True,groups=True)
atlas.run()
atlas.topdf()
atlas.tohtml()
