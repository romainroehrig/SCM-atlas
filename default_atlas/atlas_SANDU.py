#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

from collections import OrderedDict

from datetime import datetime, timedelta
from matplotlib import cm # for colormaps

####################################
# Configuration file for SANDU atlas
####################################

tmin = datetime(2006,7,15,18)
tmax = datetime(2006,7,18,18)

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
        'xname'    : '15-18 July 2006 (UTC)',
        'variables': OrderedDict([
            ('ua', {'levels': [i*0.5 for i in range(-11,3)], 'extend':'both'}),
            ('va', {'levels': [i*0.5 for i in range(-12,1)], 'extend':'both'}),
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
        'xname'    : '15-18 July 2006 (UTC)',
        'variables': OrderedDict([
            ('theta', {'levels': list(range(290,306,1)), 'extend':'both'                 }),
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
        'xname'    : '15-18 July 2006 (UTC)',
        'variables': OrderedDict([
            ('hfss',  {'ymin':-10., 'ymax':   40.}),
            ('hfls',  {'ymin':  0., 'ymax':  200.}),
            ('ustar', {'ymin':  0., 'ymax':    1.}),
            ('ts',    {'ymin':280., 'ymax':  320.}),
            ('pr',    {'ymin':  0., 'ymax':    3.}),
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
        'xname'    : '15-18 July 2006 (UTC)',
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
        'xname'    : '15-18 July 2006 (UTC)',
        'variables': OrderedDict([
            ('clt', {'ymin':  0., 'ymax':  105.}),
            ('zcb', {'ymin':  0., 'ymax': 1000.}),
            ('zct', {'ymin':  0., 'ymax': 3000.}),
            ('lwp', {'ymin':  0., 'ymax':  200.}),            
            ('rwp', {'ymin':  0., 'ymax': 1000.}),            
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
            ('ua',    {'xmin':   -5.  , 'xmax':   1. , 'init':True }),
            ('va',    {'xmin':  - 8.  , 'xmax':   0. , 'init':True }),
            ('theta', {'xmin':  285.  , 'xmax': 320. , 'init':True }),
            ('qv',    {'xmin':    0.  , 'xmax':  15. , 'init':True }),
            ('cl',    {'xmin':    0.  , 'xmax': 105.               }),
            ('ql',    {'xmin':    0.  , 'xmax': 600.               }),
            ('qr',    {'xmin':    0.  , 'xmax':   5.               }), 
        ]),
    }), # end hour23-24_basic   
    #######################
    ("hour47-48_basic",{
        'head'     : 'Basic 47-48h'            ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=47),
        'tmax'     : tmin + timedelta(hours=48),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '47-48 hour'              ,        
        'variables': OrderedDict([
            ('ua',    {'xmin':   -5.  , 'xmax':   1. , 'init':True }),
            ('va',    {'xmin':   -8.  , 'xmax':   0. , 'init':True }),
            ('theta', {'xmin':  285.  , 'xmax': 320. , 'init':True }),
            ('qv',    {'xmin':    0.  , 'xmax':  15. , 'init':True }),
            ('cl',    {'xmin':    0.  , 'xmax': 105.               }),
            ('ql',    {'xmin':    0.  , 'xmax': 600.               }),
            ('qr',    {'xmin':    0.  , 'xmax':   5.               }),
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
        'xname'    : '15-18 July 2006 (UTC)',
        'variables': OrderedDict([
            ('wa_up',    {'levels': [i*0.2 for i in range(0,16,1)]              , 'extend':'max', 'firstwhite':True }),
            ('alpha_up', {'levels': [0,0.01,0.1,1]+[i*2. for i in range(1,16,1)], 'extend':'max', 'firstwhite':True }),
            ('mf_up',    {'levels': [0,0.001]+[i*0.01 for i in range(1,16,1)]   , 'extend':'max', 'firstwhite':True }),
            ('dTv_up',   {'levels': [i*0.1 for i in range(-7,8,1)]              , 'extend':'both'                   }),
            ('b_up',     {'levels': [i*0.005 for i in range(-7,8,1)]            , 'extend':'both'                   }),
            ('ent_up',   {'levels': [i*0.5 for i in range(0,15,1)]              , 'extend':'both'                   }),
            ('det_up',   {'levels': [i*0.5 for i in range(0,15,1)]              , 'extend':'both'                   }),
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
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour23-24_conv
    #######################
    ("hour47-48_conv",{
        'head'     : 'Convection 47-48h'       ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=47),
        'tmax'     : tmin + timedelta(hours=48),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '47-48 hour'              ,        
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour47-48_conv  
    #######################
    ("init",{
        'head'     : 'Init'         ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 20.            ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('ua',    {'xmin': -10., 'xmax':   10.}),
            ('va',    {'xmin': -10., 'xmax':   10.}),
            ('theta', {'xmin': 285., 'xmax':  400.}),
            ('qv',    {'xmin':   0., 'xmax':   12.}),
            ('ql',    {'xmin':  -1., 'xmax':  800.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
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
            ('ua',    {'xmin':  -5., 'xmax':    5.}),
            ('va',    {'xmin': -10., 'xmax':   10.}),
            ('theta', {'xmin': 285., 'xmax':  320.}),
            ('qv',    {'xmin':  -1., 'xmax':   12.}),
            ('ql',    {'xmin':  -1., 'xmax':  800.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
            ('tke',   {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
