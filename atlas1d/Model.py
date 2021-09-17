#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

import logging
logger = logging.getLogger(__name__)

_dir_path = os.path.dirname(os.path.realpath(__file__))
_known_models = {}

class Model:

    def __init__(self,name=None,tstep=None,levgrid=None,
            binVersion=None,namATM=None,namSFX=None,MUSC=True):

        self.id = '{0}/{1}/{2}'.format(binVersion,tstep,levgrid)
        self.name = name
        self.tstep = tstep
        self.levgrid = levgrid
        self.binVersion = binVersion
        self.namATM = namATM
        self.namSFX = namSFX
        self.MUSC = MUSC

    def info(self):

        print('*** Model Configuration {0} ***'.format(self.name))
        print('Binaries version:', self.binVersion)
        print('timestep: {0} seconds'.format(self.tstep))
        print('Vertical discretization:', self.levgrid)
        print('Atmospheric namelist:', self.namATM)
        print('SURFEX namelist:', self.namSFX)
        print('MUSC simulation:', self.MUSC)

    def add2known(self,overwrite=False):

        if self.name in _known_models.keys():
            if overwrite:
                logger.warning('Model configuration {0} is already known'.format(self.name))
                logger.warning('it is overwritten')
                _known_models[self.name] = self
            else:
                logger.error('Model configuration {0} is already known'.format(self.name))
                logger.error('You can overwrite it using overwrite argument')
                raise ValueError
        else:
            _known_models[self.name] = self

def print_known_models():

    for mod in sorted(_known_models.keys()):
        _known_models[mod].info()

def save_all(overwrite=False):

    fileout = "{0}/known_models.json".format(_dir_path)
    if not(overwrite):
        if os.path.exists(fileout):
            logger.error("Can't overwrite existing json file containing known models")
            raise ValueError

    data2save = {}
    for mod in _known_models.keys():
        data2save[mod] = {'name':       _known_models[mod].name      ,
                          'tstep':      _known_models[mod].tstep     ,
                          'levgrid':    _known_models[mod].levgrid   ,
                          'binVersion': _known_models[mod].binVersion,
                          'namATM':     _known_models[mod].namATM    ,
                          'namSFX':     _known_models[mod].namSFX    ,
                          'MUSC':       _known_models[mod].MUSC      ,
                          }

    with open(fileout, 'w') as outfile:
        json.dump(data2save, outfile, indent=4, sort_keys=True)  

def load_all(overwrite=False):

    filein = "{0}/known_models.json".format(_dir_path)
    with open(filein) as json_file:
        data = json.load(json_file)
        for name in data.keys():
            logger.info(name)
            mod = Model(**data[name])
            mod.add2known(overwrite=overwrite)

def get_model(name):

    return _known_models[name]
