#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

import logging
logger = logging.getLogger(__name__)

import json

_dir_path = os.path.dirname(os.path.realpath(__file__))

_lines = ['k','k.','k--','k-.']

_known_datasets = {}

class Dataset:

    def __init__(self,name=None,
                 case=None,subcase=None,
                 ncfile=None,comment=None,
                 coefs={},varnames={},
                 line=None):

        if name  is None or\
           case  is None or subcase    is None:
            logger.error('name, case and subcase must be defined')
            raise ValueError

        self.id = '{0}/{1}/{2}'.format(name,case,subcase)
        self.name = name
        self.case = case
        self.ncfile = ncfile
        self.subcase = subcase        
        self.comment = comment
        self.varnames = varnames
        self.coefs = coefs

        if line is None:
            self.line = _lines.pop()
        else:
            self.line = line

    def is_valid(self):

        return not(self.ncfile is None) and os.path.exists(self.ncfile)

    def info(self):

        print('--- Dataset {0} ---'.format(self.name))
        print('Case: {0}/{1}'.format(self.case,self.subcase))
        print('ncfile: ', self.ncfile)
        print('Comment:', self.comment)
        print('varnames:', self.varnames)
        print('coefs:', self.coefs)
        print("line for plots: '{0}'".format(self.line))

    def add2known(self,overwrite=False):

        if self.id in _known_datasets.keys():
            if overwrite:
                logger.warning('Dataset {0} is already known'.format(self.name))
                logger.warning('it is overwritten')
                _known_datasets[self.id] = self
            else:
                logger.error('Dataset {0} is already known'.format(self.name))
                logger.error('You can overwrite it using overwrite argument')
                raise ValueError
        else:
            _known_datasets[self.id] = self


def print_known_datasets():

    for dat in sorted(_known_datasets.keys()):
        _known_datasets[dat].info()

def save_all(overwrite=False):

    fileout = "{0}/known_datasets.json".format(_dir_path)
    if not(overwrite):
        if os.path.exists(fileout):
            logger.error("Can't overwrite existing json file containing known datasets")
            raise ValueError

    data2save = {}
    for dat in _known_datasets.keys():
        data2save[dat] = {'name':       _known_datasets[dat].name      ,
                          'case':       _known_datasets[dat].case      ,
                          'subcase':    _known_datasets[dat].subcase   ,                
                          'comment':    _known_datasets[dat].comment   ,
                          'ncfile':     _known_datasets[dat].ncfile    ,
                          'varnames':   _known_datasets[dat].varnames  ,
                          'coefs':      _known_datasets[dat].coefs     ,
                          }

    with open(fileout, 'w') as outfile:
        json.dump(data2save, outfile, indent=4, sort_keys=True)

def load_all(overwrite=False):

    filein = "{0}/known_datasets.json".format(_dir_path)
    with open(filein) as json_file:
        data = json.load(json_file)
        for dat in data.keys():
            logger.info(name)
            dat = Dataset(**data[name])
            dat.add2known(overwrite=overwrite)


