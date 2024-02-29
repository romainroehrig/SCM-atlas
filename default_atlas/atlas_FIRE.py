#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

from collections import OrderedDict

from datetime import datetime, timedelta
import numpy as np
from matplotlib import cm # for colormaps

import atlas1d
from atlas1d.Dataset import Dataset

dir_references = os.getenv('SCM_REFERENCES')

####################################
# References for FIRE atlas
####################################

tmp = OrderedDict([
       ('LES',{'ncfile': os.path.join(dir_references, 'FIRE/FIRE_LES_MESONH_RR.nc'),  'line': 'k'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='FIRE',subcase='REF',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for SANDU atlas
####################################

tmin = datetime(1987,7,14,8)
tmax = tmin + timedelta(hours=37)

diagnostics = OrderedDict([
    ("2D_dyn",{
        'head'     : 'Dynamics (2D)'     ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,
        'ymin'     :    0.               ,
        'ymax'     : 1500.               ,
        'yname'    : 'altitude (m)'     ,
        'levunits' : 'm'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '14-15 July 1987 (UTC)',
        'variables': OrderedDict([
            ('ua', {'levels': np.arange(2,5.2,0.2)  , 'extend':'both'}),
            ('va', {'levels': np.arange(-5,-2.9,0.2), 'extend':'both'}),
        ]),
    }), # end 2D_dyn
    #######################
    ("2D_thermo",{
        'head'     : 'Thermo (2D)'       ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     : 1500.               ,
        'yname'    : 'altitude (m)'     ,
        'levunits' : 'm'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '14-15 July 1987 (UTC)',
        'variables': OrderedDict([
            ('thetal', {'levels': np.arange(285,301,1), 'extend':'both'                 }),
            ('qt'   ,  {'levels': np.arange(0,11,1)   , 'extend':'max', 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_thermo
    #######################
    ("TS_surface",{
        'head'     : 'Surface (TS)'      ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '6h'                ,
        'xname'    : '14-15 July 1987 (UTC)',
        'variables': OrderedDict([
            ('hfss',  {'ymin': -5., 'ymax':   20.}),
            ('hfls',  {'ymin':  0., 'ymax':   50.}),
            ('ustar', {'ymin':  0., 'ymax':    0.5}),
            ('ts',    {'ymin':285., 'ymax':  295.}),
            ('pr',    {'ymin':  0., 'ymax':    5.}),
        ]),
    }), # end TS_surface         
    #######################
    ("2D_cloud",{
        'head'     : 'Clouds (2D)'       ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     : 1500.               ,
        'yname'    : 'altitude (m)'     ,
        'levunits' : 'm'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '14-15 July 1987 (UTC)',
        'variables': OrderedDict([
            ('cl', {'levels': [0,1,5] + list(range(10,100,10)) + [95,100],                 'firstwhite':True, 'cmap': cm.RdBu }),
            ('ql', {'levels': list(range(0,451,30))                      , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qr', {'levels': [0.5*i for i in range(0,11)]               , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_cloud
    #######################
    ("TS_cloud",{
        'head'     : 'Clouds (TS)'       ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '6h'                ,
        'xname'    : '14-15 July 1987 (UTC)',
        'variables': OrderedDict([
            ('clt', {'ymin':  0., 'ymax':  105.}),
            ('zcb', {'ymin':  0., 'ymax':  500.}),
            ('zct', {'ymin':  0., 'ymax': 3000.}),
            ('lwp', {'ymin':  0., 'ymax':  200.}),            
            ('rwp', {'ymin':  0., 'ymax': 1000.}),            
        ]),
    }), # end TS_cloud  
    #######################
    ("hour11-12_basic",{
        'head'     : 'Basic 11-12h'            ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=11),
        'tmax'     : tmin + timedelta(hours=12),
        'ymin'     : 0.                        ,
        'ymax'     : 1500.                        ,
        'yname'    : 'altitude (m)'           ,
        'levunits' : 'm'                      ,
        'rtitle'   : '11-12 hour'              ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':    0.  , 'xmax':   5. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':  -2. , 'init':True }),
            ('thetal', {'xmin':  285.  , 'xmax': 310. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  12. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax': 105.               }),
            ('ql',     {'xmin':    0.  , 'xmax': 600.               }),
            ('qr',     {'xmin':    0.  , 'xmax':   5.               }), 
        ]),
    }), # end hour11-12_basic   
    #######################
    ("hour23-24_basic",{
        'head'     : 'Basic 23-24h'            ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=23),
        'tmax'     : tmin + timedelta(hours=24),
        'ymin'     : 0.                        ,
        'ymax'     : 1500.                        ,
        'yname'    : 'altitude (m)'           ,
        'levunits' : 'm'                      ,
        'rtitle'   : '23-24 hour'              ,        
        'variables': OrderedDict([
            ('ua',    {'xmin':    0.  , 'xmax':   5. , 'init':True }),
            ('va',    {'xmin':   -6.  , 'xmax':  -2. , 'init':True }),
            ('theta', {'xmin':  285.  , 'xmax': 310. , 'init':True }),
            ('qv',    {'xmin':    0.  , 'xmax':  12. , 'init':True }),
            ('cl',    {'xmin':    0.  , 'xmax': 105.               }),
            ('ql',    {'xmin':    0.  , 'xmax': 600.               }),
            ('qr',    {'xmin':    0.  , 'xmax':   5.               }),
        ]),
    }), # end hour23-24_basic    
    #######################
    ("2D_conv",{
        'head'     : 'Convection (2D)'   ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     : 1500.               ,
        'yname'    : 'altitude (m)'     ,
        'levunits' : 'm'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '14-15 July 1987 (UTC)',
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
    ("hour11-12_conv",{
        'head'     : 'Convection 11-12h'       ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=11),
        'tmax'     : tmin + timedelta(hours=12),
        'ymin'     : 0.                        ,
        'ymax'     : 1500.                        ,
        'yname'    : 'altitude (m)'           ,
        'levunits' : 'm'                      ,
        'rtitle'   : '11-12 hour'              ,        
        'variables': OrderedDict([
            ('w_up',     {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('Mf',       {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('B_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('eps_u',    {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_u',    {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour11-12_conv
    #######################
    ("hour23-24_conv",{
        'head'     : 'Convection 23-24h'       ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=23),
        'tmax'     : tmin + timedelta(hours=24),
        'ymin'     : 0.                        ,
        'ymax'     : 1500.                        ,
        'yname'    : 'altitude (m)'           ,
        'levunits' : 'm'                      ,
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
    ("init",{
        'head'     : 'Init'         ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 20.            ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('ua',     {'xmin': -10., 'xmax':   10.}),
            ('va',     {'xmin': -10., 'xmax':   10.}),
            ('thetal', {'xmin': 285., 'xmax':  400.}),
            ('qt',     {'xmin':   0., 'xmax':   12.}),
            ('ql',     {'xmin':  -1., 'xmax':  800.}),
            ('qi',     {'xmin':  -1., 'xmax':   20.}),
            ('tke',    {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end init 
    #######################
    ("initLL",{
        'head'     : 'Init (zoom)'  ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 1500.             ,
        'yname'    : 'altitude (m)',
        'levunits' : 'm'           ,
        'variables': OrderedDict([
            ('ua',     {'xmin':  -5., 'xmax':    5.}),
            ('va',     {'xmin': -10., 'xmax':   10.}),
            ('thetal', {'xmin': 285., 'xmax':  320.}),
            ('qt',     {'xmin':  -1., 'xmax':   12.}),
            ('ql',     {'xmin':  -1., 'xmax':  800.}),
            ('qi',     {'xmin':  -1., 'xmax':   20.}),
            ('tke',    {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
