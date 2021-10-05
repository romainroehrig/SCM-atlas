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
# References for ASTEX/EUCLIPSE atlas
####################################

subcase = 'EUCLIPSE'

tmp = OrderedDict([
       ('SAM'      , {'ncfile': os.path.join(dir_references, 'ASTEX/ASTEX_{0}_LES_SAM_RR.nc'.format(subcase)      , 'line': 'k'  }),
       ('UCLA'     , {'ncfile': os.path.join(dir_references, 'ASTEX/ASTEX_{0}_LES_UCLA_RR.nc'.format(subcase)     , 'line': 'b--'}),
       ('DALES'    , {'ncfile': os.path.join(dir_references, 'ASTEX/ASTEX_{0}_LES_DALES_RR.nc'.format(subcase)    , 'line': 'b-.'}),
       ('DHARMA'   , {'ncfile': os.path.join(dir_references, 'ASTEX/ASTEX_{0}_LES_DHARMA_RR.nc'.format(subcase)   , 'line': 'g--'}),
       ('MetOffice', {'ncfile': os.path.join(dir_references, 'ASTEX/ASTEX_{0}_LES_MetOffice_RR.nc'.format(subcase), 'line': 'g-.'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='ASTEX',subcase=subcase,ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

########################################
# Configuration file for SANDU/FAST atlas
########################################

tmin = datetime(1992,6,13,0)
tmax = datetime(1992,6,14,16)

diagnostics = OrderedDict([
    ("2D_dyn",{
        'head'     : 'Dynamics (2D)'     ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,
        'ymin'     :    0.               ,
        'ymax'     :    4.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '13-14 June 1992 (UTC)',
        'variables': OrderedDict([
            ('u', {'levels': [i*0.5 for i in range(-10,1)], 'extend':'both'}),
            ('v', {'levels': list(range(-12,1))           , 'extend':'both'}),
        ]),
    }), # end 2D_dyn
    #######################
    ("2D_thermo",{
        'head'     : 'Thermo (2D)'       ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :    4.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '13-14 June 1992 (UTC)',
        'variables': OrderedDict([
            ('theta', {'levels': list(range(285,306,1)), 'extend':'both'                 }),
            ('qv'   , {'levels': list(range(0,14,1))   , 'extend':'max', 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_thermo
    #######################
    ("TS_surface",{
        'head'     : 'Surface (TS)'      ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '6h'                ,
        'xname'    : '13-14 June 1992 (UTC)',
        'variables': OrderedDict([
            ('shf',   {'ymin':-10., 'ymax':   40.}),
            ('lhf',   {'ymin':  0., 'ymax':  200.}),
            ('ustar', {'ymin':  0., 'ymax':    1.}),
            ('tsurf', {'ymin':280., 'ymax':  320.}),
            ('rain',  {'ymin':  0., 'ymax':    3.}),
        ]),
    }), # end TS_surface         
    #######################
    ("2D_cloud",{
        'head'     : 'Clouds (2D)'       ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :    4.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '13-14 June 1992 (UTC)',
        'variables': OrderedDict([
            ('rneb', {'levels': [0,1,5] + list(range(10,100,10)) + [95,100],                 'firstwhite':True, 'cmap': cm.RdBu }),
            ('ql'  , {'levels': list(range(0,601,50))                      , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qr'  , {'levels': [0,1]+list(range(1,31,2))                  , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_cloud
    #######################
    ("TS_cloud",{
        'head'     : 'Clouds (TS)'       ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '6h'                ,
        'xname'    : '13-14 June 1992 (UTC)',
        'variables': OrderedDict([
            ('cc',  {'ymin':  0., 'ymax':  105.}),
            ('zcb', {'ymin':  0., 'ymax': 1000.}),
            ('zct', {'ymin':  0., 'ymax': 3000.}),
            ('lwp', {'ymin':  0., 'ymax':  300.}),            
            ('rwp', {'ymin':  0., 'ymax':   40.}),            
        ]),
    }), # end TS_cloud  
    #######################
    ("hour23-24_basic",{
        'head'     : 'Basic 23-24h'            ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=23),
        'tmax'     : tmin + timedelta(hours=24),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '23-24 hour'              ,        
        'variables': OrderedDict([
            ('u',        {'xmin':   -5.  , 'xmax':   5. , 'init':True }),
            ('v',        {'xmin':  -12.  , 'xmax':   0. , 'init':True }),
            ('theta',    {'xmin':  285.  , 'xmax': 310. , 'init':True }),
            ('qv',       {'xmin':    0.  , 'xmax':  15. , 'init':True }),
            ('rneb',     {'xmin':    0.  , 'xmax': 105.               }),
            ('ql',       {'xmin':    0.  , 'xmax': 500.               }),
            ('qr',       {'xmin':    0.  , 'xmax':  10.               }), 
        ]),
    }), # end hour23-24_basic   
    #######################
    ("hour39-40_basic",{
        'head'     : 'Basic 39-40h'            ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=39),
        'tmax'     : tmin + timedelta(hours=40),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '39-40 hour'              ,        
        'variables': OrderedDict([
            ('u',        {'xmin':   -5.  , 'xmax':   5. , 'init':True }),
            ('v',        {'xmin':  -12.  , 'xmax':   0. , 'init':True }),
            ('theta',    {'xmin':  285.  , 'xmax': 310. , 'init':True }),
            ('qv',       {'xmin':    0.  , 'xmax':  15. , 'init':True }),
            ('rneb',     {'xmin':    0.  , 'xmax': 105.               }),
            ('ql',       {'xmin':    0.  , 'xmax': 600.               }),
            ('qr',       {'xmin':    0.  , 'xmax':   5.               }),
        ]),
    }), # end hour47-48_basic    
    #######################
    ("2D_conv",{
        'head'     : 'Convection (2D)'   ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :    4.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '13-14 June 1992 (UTC)',
        'variables': OrderedDict([
            ('w_up',     {'levels': [i*0.2 for i in range(0,16,1)]              , 'extend':'max', 'firstwhite':True }),
            ('alpha_up', {'levels': [0,0.01,0.1,1]+[i*2. for i in range(1,16,1)], 'extend':'max', 'firstwhite':True }),
            ('Mf',       {'levels': [0,0.001]+[i*0.01 for i in range(1,16,1)]   , 'extend':'max', 'firstwhite':True }),
            ('dTv_up',   {'levels': [i*0.1 for i in range(-7,8,1)]              , 'extend':'both'                   }),
            ('B_up',     {'levels': [i*0.005 for i in range(-7,8,1)]            , 'extend':'both'                   }),
            ('eps_u',    {'levels': [i*0.5 for i in range(0,15,1)]              , 'extend':'both'                   }),
            ('det_u',    {'levels': [i*0.5 for i in range(0,15,1)]              , 'extend':'both'                   }),
        ]),
    }), # end 2D_conv
    #######################
    ("hour23-24_conv",{
        'head'     : 'Convection 23-24h'       ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=23),
        'tmax'     : tmin + timedelta(hours=24),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '23-24 hour'              ,        
        'variables': OrderedDict([
            ('w_up',     {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('Mf',       {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('B_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('eps_u',    {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_u',    {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour23-24_conv
    #######################
    ("hour39-40_conv",{
        'head'     : 'Convection 39-40h'       ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=39),
        'tmax'     : tmin + timedelta(hours=40),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '39-40 hour'              ,        
        'variables': OrderedDict([
            ('w_up',     {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('Mf',       {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('B_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('eps_u',    {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_u',    {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour39-40_conv  
    #######################
    ("init",{
        'head'     : 'Init'         ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 20.            ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('u',     {'xmin':  -5., 'xmax':    5.}),
            ('v',     {'xmin': -20., 'xmax':   20.}),
            ('theta', {'xmin': 280., 'xmax':  400.}),
            ('qv',    {'xmin':   0., 'xmax':   18.}),
            ('ql',    {'xmin':  -1., 'xmax':  800.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
            ('tke',   {'xmin':  -1., 'xmax':    2.}),
        ]),
    }), # end init 
    #######################
    ("initLL",{
        'head'     : 'Init (zoom)'  ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 4.             ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('u',     {'xmin':  -5., 'xmax':    5.}),
            ('v',     {'xmin': -20., 'xmax':   20.}),
            ('theta', {'xmin': 285., 'xmax':  315.}),
            ('qv',    {'xmin':   0., 'xmax':   18.}),
            ('ql',    {'xmin':  -1., 'xmax':  800.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
            ('tke',   {'xmin':  -1., 'xmax':    2.}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
