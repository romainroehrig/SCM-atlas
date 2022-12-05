#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

"""
Atlas for SCM Simulations
------------------------------------------------------------------

"""

import os, sys

__all__ = []

__version__ = '1.0'

__license__ = 'CeCILL-C'

__authors__ = ['Romain Roehrig']

__contributors__ = []

_dir_Atlas1D = os.path.dirname(os.path.abspath(__file__))

# Default directory for atlas
_dir_home = os.getenv('HOME')
_default_dirout = '{0}/MyAtlas1D'.format(_dir_home)

# Config files for atlas
# config files will be first search in _dir_atlas_config_default
# and then in user-defined ATLAS_CONFIG (as an environment variable)
_dir_atlas_config_default = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../default_atlas')
_dir_atlas_config = os.getenv('ATLAS_CONFIG')
sys.path = [_dir_atlas_config, _dir_atlas_config_default] + sys.path


# COMPONENTS (modules) #
#from .Model import Model
#from .Simulation import Simulation
#from .MultiAtlas import MultiAtlas
#from .Atlas import Atlas

