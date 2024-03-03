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

tmp = OrderedDict([
       ('Meso-NH' , {'ncfile': os.path.join(dir_references, 'GABLS4/STAGE3-SHORT/GABLS4_STAGE3-SHORT_MESONH_dephycf.nc'),  'line': 'k'}),
       ('CSIRO'   , {'ncfile': os.path.join(dir_references, 'GABLS4/STAGE3-SHORT/GABLS4_STAGE3-SHORT_CSIRO_dephycf.nc'),   'line': 'grey'}),
       ('IMUK'    , {'ncfile': os.path.join(dir_references, 'GABLS4/STAGE3-SHORT/GABLS4_STAGE3-SHORT_IMUK_dephycf.nc'),    'line': 'grey'}),
#       ('DALES'   , {'ncfile': os.path.join(dir_references, 'GABLS4/STAGE3-SHORT/GABLS4_STAGE3-SHORT_DALES_dephycf.nc'),   'line': 'k'}),
       ('UKMO'    , {'ncfile': os.path.join(dir_references, 'GABLS4/STAGE3-SHORT/GABLS4_STAGE3-SHORT_UKMO_dephycf.nc'),    'line': 'grey'}),
       ('MICROHH' , {'ncfile': os.path.join(dir_references, 'GABLS4/STAGE3-SHORT/GABLS4_STAGE3-SHORT_MICROHH_dephycf.nc'), 'line': 'grey'}),
       ('UCONN'   , {'ncfile': os.path.join(dir_references, 'GABLS4/STAGE3-SHORT/GABLS4_STAGE3-SHORT_UCONN_dephycf.nc'),   'line': 'grey'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='GABLS4',subcase='STAGE3-SHORT',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for GABLS1 atlas
####################################

tmin = datetime(2009,12,11,10)
tmax = datetime(2009,12,11,22)

diagnostics = OrderedDict([
    ("2D",{
        'head'     : '2D'                   ,
        'type'     : 'plot2D'               ,
        'tmin'     : tmin                   ,
        'tmax'     : tmax                   ,
        'ymin'     :    0.                  ,
        'ymax'     :    150                 ,
        'yname'    : 'altitude (m)'         ,
        'levunits' : 'm'                    ,
        'dtlabel'  : '3h'                   ,
        'xname'    : 'Hours since beginning',
        'variables': OrderedDict([
            ('theta',     {'levels': list(range(265,280,1)), 'extend':'both'}),
            ('windspeed', {'levels': np.arange(0,6.5,0.5) , 'extend':'both'}),
            ('ua',        {'levels': np.arange(0,3.3,0.3)  , 'extend':'both'}),
            ('va',        {'levels': np.arange(0,6.5,0.5)  , 'extend':'both'}),
            ('qv',        {'levels': np.arange(0,1.1,0.1)  , 'extend':'max'}),
        ]),
    }), # end 2D
    #######################
    ("TS_surface",{
        'head'     : 'Surface (TS)'         ,
        'type'     : 'plotTS'               ,
        'tmin'     : tmin                   ,
        'tmax'     : tmax                   ,        
        'dtlabel'  : '1h'                   ,
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
    ("hour4-5_basic",{
        'head'     : 'Basic 4-5h'             ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=4),
        'tmax'     : tmin + timedelta(hours=5),
        'ymin'     : 0.                       ,
        'ymax'     : 150                      ,
        'yname'    : 'altitude (m)'           ,
        'levunits' : 'm'                      ,
        'rtitle'   : '4-5 hour'               ,        
        'variables': OrderedDict([
            ('windspeed', {'xmin':    0. , 'xmax':   6., 'init':True }),
            ('ua',        {'xmin':    0. , 'xmax':   3., 'init':True }),
            ('va',        {'xmin':    0. , 'xmax':   6., 'init':True }),
            ('theta',     {'xmin':  265. , 'xmax': 280., 'init':True }),
        ]),
    }), # end hour4-5_basic   
    #######################
    ("hour8-9_basic",{
        'head'     : 'Basic 8-9h'             ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=8),
        'tmax'     : tmin + timedelta(hours=9),
        'ymin'     : 0.                       ,
        'ymax'     : 150                      ,
        'yname'    : 'altitude (m)'           ,
        'levunits' : 'm'                      ,
        'rtitle'   : '8-9 hour'               ,        
        'variables': OrderedDict([
            ('windspeed', {'xmin':    0. , 'xmax':   7. , 'init':True }),
            ('ua',        {'xmin':    0. , 'xmax':   4. , 'init':True }),
            ('va',        {'xmin':    0. , 'xmax':   6. , 'init':True }),
            ('theta',     {'xmin':  262. , 'xmax': 280. , 'init':True }),
        ]),
    }), # end hour8-9_basic   
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
        'ymax'     : 150            ,
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
