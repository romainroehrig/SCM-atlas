# -*- coding:UTF-8 -*-

import sys
sys.path = ['./','../utils/'] + sys.path

from collections import OrderedDict

import cdtime
from matplotlib import cm # for colormaps

from Dataset import Dataset

####################################
# Configuration file for SANDU atlas
####################################

tmin = cdtime.comptime(2006,7,15,18)
tmax = cdtime.comptime(2006,7,18,18)

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
            ('u', {'levels': [i*0.5 for i in range(-11,3)], 'extend':'both'}),
            ('v', {'levels': [i*0.5 for i in range(-12,1)], 'extend':'both'}),
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
            ('theta', {'levels': range(290,306,1), 'extend':'both'                 }),
            ('qv'   , {'levels': range(0,14,1)   , 'extend':'max', 'cmap': cm.RdBu }),
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
        'xname'    : '15-18 July 2006 (UTC)',
        'variables': OrderedDict([
            ('rneb', {'levels': [0,1,5] + range(10,100,10) + [95,100],                 'firstwhite':True, 'cmap': cm.RdBu }),
            ('ql'  , {'levels': range(0,451,30)                      , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qr'  , {'levels': [0.5*i for i in range(0,11)]         , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
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
            ('cc',  {'ymin':  0., 'ymax':  105.}),
            ('zcb', {'ymin':  0., 'ymax': 1000.}),
            ('zct', {'ymin':  0., 'ymax': 3000.}),
            ('lwp', {'ymin':  0., 'ymax':  200.}),            
            ('rwp', {'ymin':  0., 'ymax': 1000.}),            
        ]),
    }), # end TS_cloud  
    #######################
    ("hour23-24_basic",{
        'head'     : 'Basic 23-24h'          ,
        'type'     : 'plotAvgP'              ,
        'tmin'     : tmin.add(23,cdtime.Hour),
        'tmax'     : tmin.add(24,cdtime.Hour),  
        'ymin'     : 0.                      ,
        'ymax'     : 4.                      ,
        'yname'    : 'altitude (km)'         ,
        'levunits' : 'km'                    ,
        'rtitle'   : '23-24 hour'            ,        
        'variables': OrderedDict([
            ('u',        {'xmin':   -5.  , 'xmax':   1. , 'init':True }),
            ('v',        {'xmin':  - 8.  , 'xmax':   0. , 'init':True }),
            ('theta',    {'xmin':  285.  , 'xmax': 320. , 'init':True }),
            ('qv',       {'xmin':    0.  , 'xmax':  15. , 'init':True }),
            ('rneb',     {'xmin':    0.  , 'xmax': 105.               }),
            ('ql',       {'xmin':    0.  , 'xmax': 600.               }),
            ('qr',       {'xmin':    0.  , 'xmax':   5.               }), 
        ]),
    }), # end hour23-24_basic   
    #######################
    ("hour47-48_basic",{
        'head'     : 'Basic 47-48h'           ,
        'type'     : 'plotAvgP'              ,
        'tmin'     : tmin.add(47,cdtime.Hour) ,
        'tmax'     : tmin.add(48,cdtime.Hour),  
        'ymin'     : 0.                      ,
        'ymax'     : 4.                      ,
        'yname'    : 'altitude (km)'         ,
        'levunits' : 'km'                    ,
        'rtitle'   : '47-48 hour'             ,        
        'variables': OrderedDict([
            ('u',        {'xmin':   -5.  , 'xmax':   1. , 'init':True }),
            ('v',        {'xmin':   -8.  , 'xmax':   0. , 'init':True }),
            ('theta',    {'xmin':  285.  , 'xmax': 320. , 'init':True }),
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
        'xname'    : '15-18 July 2006 (UTC)',
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
        'head'     : 'Convection 23-24h'      ,
        'type'     : 'plotAvgP'             ,
        'tmin'     : tmin.add(23,cdtime.Hour),
        'tmax'     : tmin.add(24,cdtime.Hour),  
        'ymin'     : 0.                     ,
        'ymax'     : 4.                     ,
        'yname'    : 'altitude (km)'        ,
        'levunits' : 'km'                   ,
        'rtitle'   : '23-24 hour'             ,        
        'variables': OrderedDict([
            ('w_up',     {'xmin':    0.  , 'xmax':   4.               }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.               }),
            ('Mf',       {'xmin':    0.  , 'xmax':   0.3, 'lev':'zh'  }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.               }),
            ('B_up',     {'xmin':   -0.02, 'xmax':   0.02             }),
            ('eps_u',    {'xmin':   -0.5 , 'xmax':   5.               }),
            ('det_u',    {'xmin':   -0.5 , 'xmax':   5.               }),            
        ]),
    }), # end hour23-24_conv
    #######################
    ("hour47-48_conv",{
        'head'     : 'Convection 47-48h'      ,
        'type'     : 'plotAvgP'              ,
        'tmin'     : tmin.add(47,cdtime.Hour) ,
        'tmax'     : tmin.add(48,cdtime.Hour),  
        'ymin'     : 0.                      ,
        'ymax'     : 4.                      ,
        'yname'    : 'altitude (km)'         ,
        'levunits' : 'km'                    ,
        'rtitle'   : '47-48 hour'             ,        
        'variables': OrderedDict([
            ('w_up',     {'xmin':    0.  , 'xmax':   4.               }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.               }),
            ('Mf',       {'xmin':    0.  , 'xmax':   0.3, 'lev':'zh'  }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.               }),
            ('B_up',     {'xmin':   -0.02, 'xmax':   0.02             }),
            ('eps_u',    {'xmin':   -0.5 , 'xmax':   5.               }),
            ('det_u',    {'xmin':   -0.5 , 'xmax':   5.               }),            
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
            ('u',     {'xmin': -10., 'xmax':   10.}),
            ('v',     {'xmin': -10., 'xmax':   10.}),
            ('theta', {'xmin': 285., 'xmax':  400.}),
            ('qv',    {'xmin':   0., 'xmax':   12.}),
            ('ql',    {'xmin':  -1., 'xmax':  800.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
            ('tke',   {'xmin':  -1., 'xmax':    1., 'lev':'zh'}),
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
            ('v',     {'xmin': -10., 'xmax':   10.}),
            ('theta', {'xmin': 285., 'xmax':  320.}),
            ('qv',    {'xmin':  -1., 'xmax':   12.}),
            ('ql',    {'xmin':  -1., 'xmax':  800.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
            ('tke',   {'xmin':  -1., 'xmax':    1., 'lev':'zh'}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
