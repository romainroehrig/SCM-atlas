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
# References for ARMCU atlas
####################################

tmp = OrderedDict([
       ('LES',      {'ncfile': os.path.join(dir_references, 'RICO/RICO_SHORT_MESONH_RR.nc'),      'line': 'k'}),
       ('LES_core', {'ncfile': os.path.join(dir_references, 'RICO/RICO_SHORT_MESONH_RR_core.nc'), 'line': 'g.'}),
       ('LES_csam', {'ncfile': os.path.join(dir_references, 'RICO/RICO_SHORT_MESONH_RR_csam.nc'), 'line': 'k.'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='RICO',subcase='SHORT',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for ARMCU atlas
####################################

tmin = datetime(2004,12,16,0)
tmax = datetime(2004,12,17,0)

diagnostics = OrderedDict([
    ("2D_dyn",{
        'head'     : 'Dynamics (2D)'         ,
        'type'     : 'plot2D'                ,
        'tmin'     : tmin                    ,
        'tmax'     : tmax                    ,
        'ymin'     :    0.                   ,
        'ymax'     :    4.                   ,
        'yname'    : 'altitude (km)'         ,
        'levunits' : 'km'                    ,
        'dtlabel'  : '2h'                    ,
        'xname'    : '16 December 2004 (UTC)',
        'variables': OrderedDict([
            ('ua', {'levels': list(range(-12,1,1))         , 'extend':'both'}),
            ('va', {'levels': [i*0.5 for i in range(-13,1)], 'extend':'both'}),
        ]),
    }), # end 2D_dyn
    #######################
    ("2D_thermo",{
        'head'     : 'Thermo (2D)'           ,
        'type'     : 'plot2D'                ,
        'tmin'     : tmin                    ,
        'tmax'     : tmax                    ,
        'ymin'     :    0.                   ,
        'ymax'     :    4.                   ,
        'yname'    : 'altitude (km)'         ,
        'levunits' : 'km'                    ,
        'dtlabel'  : '2h'                    ,
        'xname'    : '16 December 2004 (UTC)',
        'variables': OrderedDict([
            ('theta', {'levels': list(range(297,315,1))  , 'extend':'both'                 }),
            ('qv'   , {'levels': [0,]+list(range(3,17,1)), 'extend':'max', 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_thermo
    #######################
    ("TS_surface",{
        'head'     : 'Surface (TS)'          ,
        'type'     : 'plotTS'                ,
        'tmin'     : tmin                    ,
        'tmax'     : tmax                    ,
        'dtlabel'  : '2h'                    ,
        'xname'    : '16 December 2004 (UTC)',
        'variables': OrderedDict([
            ('hfss' ,   {'ymin':-10., 'ymax':   30. }),
            ('hfls' ,   {'ymin':  0., 'ymax':  250. }),
            ('ustar', {'ymin':  0., 'ymax':    0.5}),
            ('ts'   , {'ymin':280., 'ymax':  320. }),
            ('pr'   ,  {'ymin':  0., 'ymax':    2. }),
        ]),
    }), # end TS_surface         
    #######################
    ("2D_cloud",{
        'head'     : 'Clouds (2D)'           ,
        'type'     : 'plot2D'                ,
        'tmin'     : tmin                    ,
        'tmax'     : tmax                    ,
        'ymin'     :    0.                   ,
        'ymax'     :    4.                   ,
        'yname'    : 'altitude (km)'         ,
        'levunits' : 'km'                    ,
        'dtlabel'  : '2h'                    ,
        'xname'    : '16 December 2004 (UTC)',
        'variables': OrderedDict([
            ('cl', {'levels': list(range(0,16,1))           , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('ql', {'levels': list(range(0,21,1))           , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qr', {'levels': [i*0.2 for i in range(0,21,1)], 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_cloud
    #######################
    ("TS_cloud",{
        'head'     : 'Clouds (TS)'           ,
        'type'     : 'plotTS'                ,
        'tmin'     : tmin                    ,
        'tmax'     : tmax                    ,        
        'dtlabel'  : '2h'                    ,
        'xname'    : '16 December 2004 (UTC)',
        'variables': OrderedDict([
            ('clt', {'ymin':  0., 'ymax':  105.}),
            ('zcb', {'ymin':  0., 'ymax': 1000.}),
            ('zct', {'ymin':  0., 'ymax': 4000.}),
            ('lwp', {'ymin':  0., 'ymax':   60.}),            
            ('rwp', {'ymin':  0., 'ymax':   20.}),            
        ]),
    }), # end TS_cloud  
    #######################
    ("hour8-12_basic",{
        'head'     : 'Basic 8-12h'             ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=8) ,
        'tmax'     : tmin + timedelta(hours=12),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '8-12 hour'               ,        
        'variables': OrderedDict([
            ('ua'   , {'xmin':  -12.  , 'xmax':   0. , 'init':True }),
            ('va'   , {'xmin':  -10.  , 'xmax':   0. , 'init':True }),
            ('theta', {'xmin':  295.  , 'xmax': 320. , 'init':True }),
            ('qv'   , {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl'   , {'xmin':    0.  , 'xmax':  20.               }),
            ('ql'   , {'xmin':    0.  , 'xmax':  20.               }),
            ('qr'   , {'xmin':    0.  , 'xmax':   5.               }),
        ]),
    }), # end hour8-12_basic   
    #######################
    ("hour20-24_basic",{
        'head'     : 'Basic 20-24h'            ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=20),
        'tmax'     : tmin + timedelta(hours=24),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '20-24 hour'              ,        
        'variables': OrderedDict([
            ('ua'   , {'xmin':  -12.  , 'xmax':   0. , 'init':True }),
            ('va'   , {'xmin':  -12.  , 'xmax':   0. , 'init':True }),
            ('theta', {'xmin':  295.  , 'xmax': 320. , 'init':True }),
            ('qv'   , {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl'   , {'xmin':    0.  , 'xmax':  20.               }),
            ('ql'   , {'xmin':    0.  , 'xmax':  20.               }),
            ('qr'   , {'xmin':    0.  , 'xmax':   5.               }),
        ]),
    }), # end hour9-10_basic    
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
        'dtlabel'  : '2h'                ,
        'xname'    : '16 December 2004 (UTC)',
        'variables': OrderedDict([
            ('wa_up'   , {'levels': [i*0.2 for i in range(0,16,1)]              , 'extend':'max', 'firstwhite':True }),
            ('alpha_up', {'levels': [0,0.01,0.1,1]+[i*2. for i in range(1,16,1)], 'extend':'max', 'firstwhite':True }),
            ('mf_up'   , {'levels': [0,0.001]+[i*0.01 for i in range(1,19,1)]   , 'extend':'max', 'firstwhite':True }),
            ('dTv_up'  , {'levels': [i*0.1 for i in range(-7,8,1)]              , 'extend':'both'                   }),
            ('b_up'    , {'levels': [i*0.005 for i in range(-7,8,1)]            , 'extend':'both'                   }),
            ('ent_up'  , {'levels': [i*0.5 for i in range(0,15,1)]              , 'extend':'both'                   }),
            ('det_up'  , {'levels': [i*0.5 for i in range(0,15,1)]              , 'extend':'both'                   }),
        ]),
    }), # end 2D_conv
    #######################
    ("hour8-12_conv",{
        'head'     : 'Convection 8-12h'        ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=8) ,
        'tmax'     : tmin + timedelta(hours=12),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '8-12 hour'               ,        
        'variables': OrderedDict([
            ('wa_up'   , {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up'   , {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up'  , {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up'    , {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up'  , {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up'  , {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour8-12_conv
    #######################
    ("hour20-24_conv",{
        'head'     : 'Convection 20-24h'       ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=20),
        'tmax'     : tmin + timedelta(hours=24),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '20-24 hour'              ,        
        'variables': OrderedDict([
            ('wa_up'   , {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up'   , {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up'  , {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up'    , {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up'  , {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up'  , {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour20-24_conv  
    #######################
    ("init",{
        'head'     : 'Init'         ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 20.            ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('ua'   , {'xmin': -12., 'xmax':   35.}),
            ('va'   , {'xmin': -10., 'xmax':   10.}),
            ('theta', {'xmin': 295., 'xmax':  400.}),
            ('qv'   , {'xmin':  -1., 'xmax':   18.}),
            ('ql'   , {'xmin':  -1., 'xmax':   20.}),
            ('qi'   , {'xmin':  -1., 'xmax':   20.}),
            ('tke'  , {'xmin':  -1., 'xmax':    1.}),
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
            ('ua'   , {'xmin': -12., 'xmax':   12.}),
            ('va'   , {'xmin': -10., 'xmax':   10.}),
            ('theta', {'xmin': 295., 'xmax':  325.}),
            ('qv'   , {'xmin':  -1., 'xmax':   18.}),
            ('ql'   , {'xmin':  -1., 'xmax':  200.}),
            ('qi'   , {'xmin':  -1., 'xmax':   20.}),
            ('tke'  , {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
