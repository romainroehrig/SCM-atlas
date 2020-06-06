# -*- coding:UTF-8 -*-

import sys
sys.path = ['./','../utils/'] + sys.path

from collections import OrderedDict

import cdtime
from matplotlib import cm # for colormaps

from Dataset import Dataset

####################################
# Configuration file for AYOTTE atlas
####################################

tmin = cdtime.comptime(2009,12,11,0)
tmax = cdtime.comptime(2009,12,11,6)

diagnostics = OrderedDict([
    ("2D",{
        'head'     : '2D'                   ,
        'type'     : 'plot2D'               ,
        'tmin'     : tmin                   ,
        'tmax'     : tmax                   ,
        'ymin'     :    0.                  ,
        'ymax'     :    2.5                 ,
        'yname'    : 'altitude (km)'        ,
        'levunits' : 'km'                   ,
        'dtlabel'  : '1h'                   ,
        'xname'    : 'Hours since beginning',
        'variables': OrderedDict([
            ('theta', {'levels': range(300,316,1), 'extend':'both'}),
            ('u',     {'levels': range(-1,16,1)  , 'extend':'both'}),
            ('v',     {'levels': range(-6,7,1)   , 'extend':'both'}),
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
            ('shf',   {'ymin':-40., 'ymax':  300.}),
            ('lhf',   {'ymin':-40., 'ymax':   40.}),
            ('ustar', {'ymin':  0., 'ymax':    1.}),
            ('tsurf', {'ymin':280., 'ymax':  320.}),
        ]),
    }), # end TS_surface         
    #######################
    ("TS_cloud",{
        'head'     : 'Clouds (TS)'          ,
        'type'     : 'plotTS'               ,
        'tmin'     : tmin                   ,
        'tmax'     : tmax                   ,        
        'dtlabel'  : '1h'                   ,
        'xname'    : 'Hours since beginning',
        'variables': OrderedDict([
            ('cc',  {'ymin': -5., 'ymax':  105.}),
            ('lwp', {'ymin': -5., 'ymax':   20.}),            
        ]),
    }), # end TS_cloud  
    #######################
    ("hour4-5_basic",{
        'head'     : 'Basic 4-5h'           ,
        'type'     : 'plotAvgP'             ,
        'tmin'     : tmin.add(4,cdtime.Hour),
        'tmax'     : tmin.add(5,cdtime.Hour),  
        'ymin'     : 0.                     ,
        'ymax'     : 2.5                    ,
        'yname'    : 'altitude (km)'        ,
        'levunits' : 'km'                   ,
        'rtitle'   : '4-5 hour'             ,        
        'variables': OrderedDict([
            ('u',        {'xmin':   -1.  , 'xmax':  17. , 'init':True }),
            ('v',        {'xmin':   -3.  , 'xmax':  10. , 'init':True }),
            ('theta',    {'xmin':  299.5 , 'xmax': 315. , 'init':True }),
        ]),
    }), # end hour4-5_basic   
    #######################
    ("2D_conv",{
        'head'     : 'Convection (2D)'   ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :    2.5              ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '1h'                ,
        'xname'    : 'Hours since beginning',
        'variables': OrderedDict([
            ('w_up',     {'levels': [i*0.2 for i in range(0,16,1)]                , 'extend':'max', 'firstwhite':True }),
            ('alpha_up', {'levels': [0,0.01,0.1,1]+[i*2. for i in range(1,16,1)]  , 'extend':'max', 'firstwhite':True }),
            ('Mf',       {'levels': [0,0.001,0.01]+[i*0.02 for i in range(1,19,1)], 'extend':'max', 'firstwhite':True }),
            ('dTv_up',   {'levels': [i*0.1 for i in range(-7,8,1)]                , 'extend':'both'                   }),
            ('B_up',     {'levels': [i*0.005 for i in range(-7,8,1)]              , 'extend':'both'                   }),
            ('eps_u',    {'levels': [i*0.5 for i in range(0,15,1)]                , 'extend':'both'                   }),
            ('det_u',    {'levels': [i*0.5 for i in range(0,15,1)]                , 'extend':'both'                   }),
        ]),
    }), # end 2D_conv
    #######################
    ("hour4-5_conv",{
        'head'     : 'Convection 4-5h'      ,
        'type'     : 'plotAvgP'             ,
        'tmin'     : tmin.add(4,cdtime.Hour),
        'tmax'     : tmin.add(5,cdtime.Hour),  
        'ymin'     : 0.                     ,
        'ymax'     : 2.5                    ,
        'yname'    : 'altitude (km)'        ,
        'levunits' : 'km'                   ,
        'rtitle'   : '4-5 hour'             ,        
        'variables': OrderedDict([
            ('w_up',     {'xmin':    0.  , 'xmax':   4.               }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.               }),
            ('Mf',       {'xmin':    0.  , 'xmax':   0.3, 'lev':'zh'  }),
            ('dTv_up',   {'xmin':   -2.  , 'xmax':   1.               }),
            ('B_up',     {'xmin':   -0.02, 'xmax':   0.02             }),
            ('eps_u',    {'xmin':   -0.5 , 'xmax':   5.               }),
            ('det_u',    {'xmin':   -0.5 , 'xmax':   5.               }),            
        ]),
    }), # end hour4-5_conv
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
            ('theta', {'xmin': 295., 'xmax':  450.}),
            ('qv',    {'xmin':  -1., 'xmax':    5.}),
            ('ql',    {'xmin':  -1., 'xmax':   20.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
            ('tke',   {'xmin':  -1., 'xmax':    1., 'lev':'zh'}),
        ]),
    }), # end init 
    #######################
    ("initLL",{
        'head'     : 'Init (zoom)'  ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 2.5            ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('u',     {'xmin':  -1., 'xmax':   17.}),
            ('v',     {'xmin':  -5., 'xmax':    5.}),
            ('theta', {'xmin': 295., 'xmax':  320.}),
            ('qv',    {'xmin':  -1., 'xmax':    5.}),
            ('ql',    {'xmin':  -1., 'xmax':   20.}),
            ('qi',    {'xmin':  -1., 'xmax':   20.}),
            ('tke',   {'xmin':  -1., 'xmax':    1., 'lev':'zh'}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
