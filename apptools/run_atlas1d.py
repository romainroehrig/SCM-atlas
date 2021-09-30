#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os
import argparse
import importlib

import warnings
warnings.filterwarnings("ignore")
import logging
logging.basicConfig(format='%(asctime)s - %(name)30s - %(levelname)s - %(message)s', level=logging.INFO)
#logging.basicConfig(format='%(asctime)s - %(name)30s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

from collections import OrderedDict

import atlas1d
from atlas1d.Simulation import Simulation
from atlas1d.MultiAtlas import MultiAtlas

if __name__ == '__main__':

    # Definition of arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-config", help="config file", type=str, required=True)
    parser.add_argument("--pdf", help="PDF files for each case/subcase is produced",    dest='pdf', action="store_true")
    parser.add_argument("--no-run", help="No run of the atlas. Suppose it has already been run",    dest='norun', action="store_true")
    parser.add_argument("-v", help="Active verbosity",    dest='verbose', action="store_true")

    # Getting arguments
    args = parser.parse_args()
    config_file = args.config

    lpdf = args.pdf
    lrun = not(args.norun)
    lverbose = args.verbose

    # check existence of config_file and then import it
    if not(os.path.isfile(config_file)):
        raise ValueError("The configuration file {0} does not exist".format(config_file))

    configloc = config_file.split('/')[-1]
    configloc = configloc.replace('.','_')[:-3] # a module cannot have dots in its name

    try:
        os.remove('./{0}.py'.format(configloc))
    except OSError:
        pass
    except:
        raise

    os.symlink(config_file,"./{0}.py".format(configloc))
    
    CM = importlib.import_module(configloc)

    dir_atlas = CM.dir_atlas
    name_atlas = CM.name_atlas
    cases = CM.cases
    subcases = CM.subcases
    simulations = CM.simulations

    logger.info('Initialize Atlas')
    atlas = MultiAtlas(name_atlas,simulations=simulations,root_dir=dir_atlas)
    if lverbose:
        atlas.info()

    logger.info('Running multi-atlas')
    # (Re)Run a subset of atlas cases
    #atlas.run(cases=['GABLS1',])
    # Run atlas for all cases
    if lrun:
        atlas.run()

    # Prepare pdf files assembling atlas diagnostics
    if lpdf:
        logger.info('Preparing pdf files for each atlas case')
        atlas.topdf()

    # Prepare html interface for atlas of all cases
    logging.info('Preparing html interface')
    atlas.tohtml()
    logging.info('Atlas ready at {0}/index.html'.format(atlas.html_dir))

    os.remove("./{0}.py".format(configloc))
