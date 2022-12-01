#!/usr/bin/env python3
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
# References for BOMEX atlas
####################################

tmp = OrderedDict([
       ('LES',      {'ncfile': os.path.join(dir_references, 'IHOP/IHOP_LES_MESONH_RR.nc'), 'line': 'k'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='IHOP',subcase='REF',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for BOMEX atlas
####################################

tmin = datetime(2002,6,14,12)
tmax = datetime(2002,6,14,19)

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
        'dtlabel'  : '1h'                ,
        'xname'    : '14 June 2002 (UTC)',
        'variables': OrderedDict([
            ('u', {'levels': list(range(-18,19,3)), 'extend':'both'}),
            ('v', {'levels': list(range(-21,4,3)) ,  'extend':'both'}),
        ]),
    }), # end 2D_dyn
    #######################
    ("2D_thermo",{
        'head'     : 'Thermo (2D)'      ,
        'type'     : 'plot2D'           ,
        'tmin'     : tmin               ,
        'tmax'     : tmax               ,        
        'ymin'     :    0.              ,
        'ymax'     :    4.              ,
        'yname'    : 'altitude (km)'    ,
        'levunits' : 'km'               ,
        'dtlabel'  : '1h'               ,
        'xname'    : '14 June 2002 (UTC)',
        'variables': OrderedDict([
            ('theta', {'levels': list(range(296,316,1)), 'extend':'both'                 }),
            ('qv'   , {'levels': list(range(0,12,1))   , 'extend':'max', 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_thermo
    #######################
    ("TS_surface",{
        'head'     : 'Surface (TS)'      ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '1h'                ,
        'xname'    : '14 June 2002 (UTC)',
        'variables': OrderedDict([
            ('shf',   {'ymin':  0., 'ymax':  200.}),
            ('lhf',   {'ymin':  0., 'ymax':  200.}),
            ('ustar', {'ymin':  0., 'ymax':    1.}),
            ('tsurf', {'ymin':280., 'ymax':  320.}),
            ('rain',  {'ymin':  0., 'ymax':    2.}),
        ]),
    }), # end TS_surface         
    #######################
    ("TS_cloud",{
        'head'     : 'Clouds (TS)'       ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '1h'                ,
        'xname'    : '14 June 2002 (UTC)',
        'variables': OrderedDict([
            ('cc',  {'ymin':  0., 'ymax':  105.}),
            ('lwp', {'ymin':  0., 'ymax':  100.}),            
            ('rwp', {'ymin':  0., 'ymax':  100.}),            
        ]),
    }), # end TS_cloud  
    #######################
    ("hour3-4_basic",{
        'head'     : 'Basic 3-4h'             ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=3),
        'tmax'     : tmin + timedelta(hours=4),
        'ymin'     : 0.                       ,
        'ymax'     : 4.                       ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '3-4 hour'               ,        
        'variables': OrderedDict([
            ('u',        {'xmin':  -15.  , 'xmax':  15. , 'init':True }),
            ('v',        {'xmin':  -15.  , 'xmax':  15. , 'init':True }),
            ('theta',    {'xmin':  295.  , 'xmax': 320. , 'init':True }),
            ('qv',       {'xmin':    0.  , 'xmax':  14. , 'init':True }),
        ]),
    }), # end hour3-4_basic   
    #######################
    ("2D_conv",{
        'head'     : 'Convection (2D)'  ,
        'type'     : 'plot2D'           ,
        'tmin'     : tmin               ,
        'tmax'     : tmax               ,        
        'ymin'     :    0.              ,
        'ymax'     :    4.              ,
        'yname'    : 'altitude (km)'    ,
        'levunits' : 'km'               ,
        'dtlabel'  : '1h'               ,
        'xname'    : '14 June 2002 (UTC)',
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
    ("hour3-4_conv",{
        'head'     : 'Convection 3-4h'        ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=3),
        'tmax'     : tmin + timedelta(hours=4),
        'ymin'     : 0.                       ,
        'ymax'     : 4.                       ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '3-4 hour'               ,        
        'variables': OrderedDict([
            ('w_up',     {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  30.  }),
            ('Mf',       {'xmin':    0.  , 'xmax':   0.5 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('B_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('eps_u',    {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_u',    {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour3-4_conv
    #######################
    ("init",{
        'head'     : 'Init'         ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 20.            ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('u',     {'xmin': -20., 'xmax':   20.}),
            ('v',     {'xmin': -15., 'xmax':   15.}),
            ('theta', {'xmin': 295., 'xmax':  400.}),
            ('qv',    {'xmin':  -1., 'xmax':   14.}),
            ('ql',    {'xmin':  -1., 'xmax':   10.}),
            ('qi',    {'xmin':  -1., 'xmax':   10.}),
            ('tke',   {'xmin':  -1., 'xmax':    1.}),
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
            ('u',     {'xmin': -20., 'xmax':   20.}),
            ('v',     {'xmin': -15., 'xmax':   15.}),
            ('theta', {'xmin': 295., 'xmax':  325.}),
            ('qv',    {'xmin':  -1., 'xmax':   14.}),
            ('ql',    {'xmin':  -1., 'xmax':   10.}),
            ('qi',    {'xmin':  -1., 'xmax':   10.}),
            ('tke',   {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
