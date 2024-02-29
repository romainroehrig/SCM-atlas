#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

from collections import OrderedDict

from datetime import datetime, timedelta
from matplotlib import cm # for colormaps

import atlas1d
from atlas1d.Dataset import Dataset

dir_references = os.getenv('SCM_REFERENCES')

####################################
# References for AYOTTE/00SC atlas
####################################

tmp = OrderedDict([
       ('MO'     ,  {'ncfile': os.path.join(dir_references, 'GABLS1/files/MO_1m_allvar.nc'), 'line': 'k'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='GABLS1',subcase='REF',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for GABLS1 atlas
####################################

tmin = datetime(2000,1,1,10)
tmax = datetime(2000,1,1,19)

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
        'dtlabel'  : '1h'                   ,
        'xname'    : 'Hours since beginning',
        'variables': OrderedDict([
            ('theta', {'levels': list(range(260,275,1)), 'extend':'both'}),
            ('u',     {'levels': list(range(-1,9,1))   , 'extend':'both'}),
            ('v',     {'levels': list(range(-3,3,1))   , 'extend':'both'}),
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
            ('shf',   {'ymin':-40., 'ymax':  400.}),
            ('ustar', {'ymin':  0., 'ymax':    1.}),
            ('tsurf', {'ymin':260., 'ymax':  270.}),
        ]),
    }), # end TS_surface         
    #######################
    ("hour7-8_basic",{
        'head'     : 'Basic 7-8h'             ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=7),
        'tmax'     : tmin + timedelta(hours=8),
        'ymin'     : 0.                       ,
        'ymax'     : 400                      ,
        'yname'    : 'altitude (m)'           ,
        'levunits' : 'm'                      ,
        'rtitle'   : '7-8 hour'               ,        
        'variables': OrderedDict([
            ('u',        {'xmin':   -1. , 'xmax':  10. , 'init':True }),
            ('v',        {'xmin':   -3. , 'xmax':   3. , 'init':True }),
            ('theta',    {'xmin':  260. , 'xmax': 275. , 'init':True }),
        ]),
    }), # end hour7-8_basic   
    #######################
    ("hour8-9_basic",{
        'head'     : 'Basic 8-9h'             ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=8),
        'tmax'     : tmin + timedelta(hours=9),
        'ymin'     : 0.                       ,
        'ymax'     : 400                      ,
        'yname'    : 'altitude (m)'           ,
        'levunits' : 'm'                      ,
        'rtitle'   : '8-9 hour'               ,        
        'variables': OrderedDict([
            ('u',        {'xmin':   -1. , 'xmax':  10. , 'init':True }),
            ('v',        {'xmin':   -3. , 'xmax':   3. , 'init':True }),
            ('theta',    {'xmin':  260. , 'xmax': 275. , 'init':True }),
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
            ('u',     {'xmin':  -1., 'xmax':   17.}),
            ('v',     {'xmin':  -5., 'xmax':    5.}),
            ('theta', {'xmin': 260., 'xmax':  450.}),
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
            ('u',     {'xmin':  -1., 'xmax':   17.}),
            ('v',     {'xmin':  -5., 'xmax':    5.}),
            ('theta', {'xmin': 295., 'xmax':  320.}),
            ('qv',    {'xmin':  -1., 'xmax':    5.}),
            ('ql',    {'xmin':  -1., 'xmax':   20.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
            ('tke',   {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
