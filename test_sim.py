#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os, sys
sys.path = ['./utils/','./config/'] + sys.path

from Simulation import *

discover()

stop

for name in ['CMIP6','CMIP6.LPBLE']:
    for case,subcase in [('ARMCU','REF'), ('RICO','REF')]:
        print name,case,subcase
        sim = Simulation(name,case,subcase,tstep=300,level='L91',binVersion='arp631.diag')
        sim.add2known()

print_known_simulations()

save_all(overwrite=True)
