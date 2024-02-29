#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

from collections import OrderedDict

import numpy as np

from datetime import datetime, timedelta
from matplotlib import cm # for colormaps

import atlas1d
from atlas1d.Dataset import Dataset

dir_references = os.getenv('SCM_REFERENCES')

####################################
# References for AYOTTE/00SC atlas
####################################

#tmp = OrderedDict([
#       ('MO'     ,  {'ncfile': os.path.join(dir_references, 'GABLS1/files/MO_1m_allvar.nc'), 'line': 'k'}),
#       ])

references = []
#for ref in tmp.keys():
#    references.append(Dataset(name=ref,case='GABLS1',subcase='REF',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for GABLS1 atlas
####################################

tmin = datetime(2009,12,11,0)
tmax = datetime(2009,12,12,12)

diagnostics = OrderedDict([
    ("2D",{
        'head'     : '2D'                   ,
        'type'     : 'plot2D'               ,
        'tmin'     : tmin                   ,
        'tmax'     : tmax                   ,
        'ymin'     :    0.                  ,
        'ymax'     :    400                 ,
        'yname'    : 'altitude (m)'         ,
        'levunits' : 'm'                    ,
        'dtlabel'  : '3h'                   ,
        'xname'    : 'Hours since beginning',
        'variables': OrderedDict([
            ('theta', {'levels': list(range(270,281,1)), 'extend':'both'}),
            ('ua',    {'levels': np.arange(0,4.5,0.5)  , 'extend':'both'}),
            ('va',    {'levels': np.arange(0,5.5,0.5)  , 'extend':'both'}),
            ('qv',    {'levels': np.arange(0,1.1,0.1)  , 'extend':'max'}),
        ]),
    }), # end 2D
    #######################
    ("TS_surface",{
        'head'     : 'Surface (TS)'         ,
        'type'     : 'plotTS'               ,
        'tmin'     : tmin                   ,
        'tmax'     : tmax                   ,        
        'dtlabel'  : '3h'                   ,
        'xname'    : 'Hours since beginning',
        'variables': OrderedDict([
            ('hfss',  {'ymin':-20., 'ymax':   25.}),
            ('hfls',  {'ymin':-40., 'ymax':   40.}),
            ('hflsn', {'ymin':-40., 'ymax':   40.}),
            ('ustar', {'ymin':  0., 'ymax':    0.3}),
            ('ts',    {'ymin':230., 'ymax':  250.}),
        ]),
    }), # end TS_surface         
    #######################
    ("hour5-6_basic",{
        'head'     : 'Basic 5-6h'             ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=5),
        'tmax'     : tmin + timedelta(hours=6),
        'ymin'     : 0.                       ,
        'ymax'     : 400                      ,
        'yname'    : 'altitude (m)'           ,
        'levunits' : 'm'                      ,
        'rtitle'   : '5-6 hour'               ,        
        'variables': OrderedDict([
            ('ua',    {'xmin':    0. , 'xmax':   4. , 'init':True }),
            ('va',    {'xmin':    0. , 'xmax':   6. , 'init':True }),
            ('theta', {'xmin':  270. , 'xmax': 280. , 'init':True }),
        ]),
    }), # end hour7-8_basic   
    #######################
    ("hour15-16_basic",{
        'head'     : 'Basic 15-16h'            ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=15),
        'tmax'     : tmin + timedelta(hours=16),
        'ymin'     : 0.                        ,
        'ymax'     : 400                       ,
        'yname'    : 'altitude (m)'            ,
        'levunits' : 'm'                       ,
        'rtitle'   : '15-16 hour'                ,        
        'variables': OrderedDict([
            ('ua',    {'xmin':   -4. , 'xmax':   4. , 'init':True }),
            ('va',    {'xmin':    0. , 'xmax':   6. , 'init':True }),
            ('theta', {'xmin':  270. , 'xmax': 280. , 'init':True }),
        ]),
    }), # end hour7-8_basic   
    #######################
    
    ("init",{
        'head'     : 'Init'         ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 20.            ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('ua',    {'xmin':   0., 'xmax':   20.}),
            ('va',    {'xmin':  -1., 'xmax':   20.}),
            ('theta', {'xmin': 270., 'xmax':  450.}),
            ('qv',    {'xmin':  -1., 'xmax':    5.}),
            ('ql',    {'xmin':  -1., 'xmax':   20.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
            ('tke',   {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end init 
    #######################
    ("initLL",{
        'head'     : 'Init (zoom)'  ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 400            ,
        'yname'    : 'altitude (m)' ,
        'levunits' : 'm'            ,
        'variables': OrderedDict([
            ('ua',    {'xmin':   0., 'xmax':   12.}),
            ('va',    {'xmin':   0., 'xmax':    7.}),
            ('theta', {'xmin': 270., 'xmax':  280.}),
            ('qv',    {'xmin':  -1., 'xmax':    5.}),
            ('ql',    {'xmin':  -1., 'xmax':   20.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
            ('tke',   {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
