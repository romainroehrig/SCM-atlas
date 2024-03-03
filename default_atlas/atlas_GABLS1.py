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
       ('MO-1m'  ,  {'ncfile': os.path.join(dir_references, 'GABLS1/files/MO_1m_allvar.nc'),   'line': 'k'}),
       ('IMUK-1m',  {'ncfile': os.path.join(dir_references, 'GABLS1/files/IMUK_1m_allvar.nc'), 'line': 'k'}),
       ('MO-2m'  ,  {'ncfile': os.path.join(dir_references, 'GABLS1/files/MO_2m_allvar.nc'),   'line': 'grey'}),
       ('IMUK-2m',  {'ncfile': os.path.join(dir_references, 'GABLS1/files/IMUK_2m_allvar.nc'), 'line': 'grey'}),
       ('CORA-2m',  {'ncfile': os.path.join(dir_references, 'GABLS1/files/CORA_2m_allvar.nc'), 'line': 'grey'}),
       ('NCAR-2m',  {'ncfile': os.path.join(dir_references, 'GABLS1/files/NCAR_2m_allvar.nc'), 'line': 'grey'}),
       ('UIB-2m' ,  {'ncfile': os.path.join(dir_references, 'GABLS1/files/UIB_2m_allvar.nc'),  'line': 'grey'}),
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
            ('theta',     {'levels': list(range(260,275,1)), 'extend':'both'}),
            ('windspeed', {'levels': list(range(-1,9,1))   , 'extend':'both'}),
            ('ua',        {'levels': list(range(-1,9,1))   , 'extend':'both'}),
            ('va',        {'levels': list(range(-3,3,1))   , 'extend':'both'}),
            ('qv',        {'levels': list(range(0,10,1))   , 'extend':'max'}),
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
            ('hfss',  {'ymin':-25., 'ymax':    0.}),
            ('hfls',  {'ymin':-40., 'ymax':   40.}),
            ('ustar', {'ymin':  0., 'ymax':    0.6}),
            ('ts',    {'ymin':262., 'ymax':  268.}),
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
            ('windspeed', {'xmin':    0. , 'xmax':  12. , 'init':True }),
            ('ua',        {'xmin':    0. , 'xmax':  12. , 'init':True }),
            ('va',        {'xmin':   -5. , 'xmax':   5. , 'init':True }),
            ('theta',     {'xmin':  262. , 'xmax': 270. , 'init':True }),
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
            ('windspeed', {'xmin':    0. , 'xmax':  12. , 'init':True }),
            ('ua',        {'xmin':    0. , 'xmax':  12. , 'init':True }),
            ('va',        {'xmin':   -5. , 'xmax':   5. , 'init':True }),
            ('theta',     {'xmin':  262. , 'xmax': 270. , 'init':True }),
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
            ('windspeed', {'xmin':   0., 'xmax':   12.}),
            ('ua',        {'xmin':   0., 'xmax':   12.}),
            ('va',        {'xmin':  -5., 'xmax':    5.}),
            ('theta',     {'xmin': 260., 'xmax':  450.}),
            ('qv',        {'xmin':  -1., 'xmax':    5.}),
            ('ql',        {'xmin':  -1., 'xmax':   20.}),
            ('qi',        {'xmin':  -1., 'xmax':   20.}),
            ('tke',       {'xmin':  -1., 'xmax':    1.}),
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
            ('windspeed', {'xmin':   0., 'xmax':   12.}),
            ('ua',        {'xmin':   0., 'xmax':   12.}),
            ('va',        {'xmin':  -5., 'xmax':    5.}),
            ('theta',     {'xmin': 295., 'xmax':  320.}),
            ('qv',        {'xmin':  -1., 'xmax':    5.}),
            ('ql',        {'xmin':  -1., 'xmax':   20.}),
            ('qi',        {'xmin':  -1., 'xmax':   20.}),
            ('tke',       {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
