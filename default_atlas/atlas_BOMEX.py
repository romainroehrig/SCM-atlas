# -*- coding:UTF-8 -*-

import sys
sys.path = ['./','../utils/'] + sys.path

from collections import OrderedDict

import cdtime
from matplotlib import cm # for colormaps

from Dataset import Dataset

####################################
# References for BOMEX atlas
####################################

tmp = OrderedDict([
       ('LES',      {'ncfile': '/Users/romainroehrig/data/LES/BOMEX/BOMEX_LES_MESONH_RR.nc',      'line': 'k'}),
       ('LES_core', {'ncfile': '/Users/romainroehrig/data/LES/BOMEX/BOMEX_LES_MESONH_RR_core.nc', 'line': 'g.'}),
       ('BLM_csam', {'ncfile': '/Users/romainroehrig/data/LES/BOMEX/BOMEX_LES_MESONH_RR_csam.nc', 'line': 'k.'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='BOMEX',subcase='REF',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for BOMEX atlas
####################################

tmin = cdtime.comptime(1969,6,24,0)
tmax = cdtime.comptime(1969,6,24,14)

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
        'xname'    : '24 June 1969 (UTC)',
        'variables': OrderedDict([
            ('u', {'levels': [i*0.5 for i in range(-16,1,1)], 'extend':'both'}),
            ('v', {'levels': [i*0.5 for i in range(-8,9,1)] ,  'extend':'both'}),
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
        'dtlabel'  : '1h'                ,
        'xname'    : '24 June 1969 (UTC)',
        'variables': OrderedDict([
            ('theta', {'levels': range(298,316,1)  , 'extend':'both'                 }),
            ('qv'   , {'levels': [0,]+range(4,19,1), 'extend':'max', 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_thermo
    #######################
    ("TS_surface",{
        'head'     : 'Surface (TS)'      ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '1h'                ,
        'xname'    : '24 June 1969 (UTC)',
        'variables': OrderedDict([
            ('shf',   {'ymin':  0., 'ymax':   20.}),
            ('lhf',   {'ymin':  0., 'ymax':  200.}),
            ('ustar', {'ymin':  0., 'ymax':    1.}),
            ('tsurf', {'ymin':280., 'ymax':  320.}),
            ('rain',  {'ymin':  0., 'ymax':    2.}),
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
        'dtlabel'  : '1h'                ,
        'xname'    : '24 June 1969 (UTC)',
        'variables': OrderedDict([
            ('rneb', {'levels': range(0,16,1)                 , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('ql'  , {'levels': range(0,16,1)                 , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qr'  , {'levels': [i*0.2 for i in range(0,21,1)], 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_cloud
    #######################
    ("TS_cloud",{
        'head'     : 'Clouds (TS)'       ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '1h'                ,
        'xname'    : '24 June 1969 (UTC)',
        'variables': OrderedDict([
            ('cc',  {'ymin':  0., 'ymax':   60.}),
            ('zcb', {'ymin':  0., 'ymax': 1000.}),
            ('zct', {'ymin':  0., 'ymax': 4000.}),
            ('lwp', {'ymin':  0., 'ymax':   40.}),            
            ('rwp', {'ymin':  0., 'ymax':   40.}),            
        ]),
    }), # end TS_cloud  
    #######################
    ("hour7-8_basic",{
        'head'     : 'Basic 7-8h'           ,
        'type'     : 'plotAvgP'             ,
        'tmin'     : tmin.add(7,cdtime.Hour),
        'tmax'     : tmin.add(8,cdtime.Hour),  
        'ymin'     : 0.                     ,
        'ymax'     : 4.                     ,
        'yname'    : 'altitude (km)'        ,
        'levunits' : 'km'                   ,
        'rtitle'   : '7-8 hour'             ,        
        'variables': OrderedDict([
            ('u',        {'xmin':  -12.  , 'xmax':   0. , 'init':True }),
            ('v',        {'xmin':   -3.  , 'xmax':   3. , 'init':True }),
            ('theta',    {'xmin':  295.  , 'xmax': 325. , 'init':True }),
            ('qv',       {'xmin':    0.  , 'xmax':  18. , 'init':True }),
            ('rneb',     {'xmin':    0.  , 'xmax':  15.               }),
            ('ql',       {'xmin':    0.  , 'xmax':  30.               }),
            ('qr',       {'xmin':    0.  , 'xmax':   3.               }),
        ]),
    }), # end hour7-8_basic   
    #######################
    ("hour9-10_basic",{
        'head'     : 'Basic 9-10h'           ,
        'type'     : 'plotAvgP'              ,
        'tmin'     : tmin.add(9,cdtime.Hour) ,
        'tmax'     : tmin.add(10,cdtime.Hour),  
        'ymin'     : 0.                      ,
        'ymax'     : 4.                      ,
        'yname'    : 'altitude (km)'         ,
        'levunits' : 'km'                    ,
        'rtitle'   : '9-10 hour'             ,        
        'variables': OrderedDict([
            ('u',        {'xmin':  -12.  , 'xmax':   0. , 'init':True }),
            ('v',        {'xmin':   -3.  , 'xmax':   3. , 'init':True }),
            ('theta',    {'xmin':  295.  , 'xmax': 325. , 'init':True }),
            ('qv',       {'xmin':    0.  , 'xmax':  18. , 'init':True }),
            ('rneb',     {'xmin':    0.  , 'xmax':  15.               }),
            ('ql',       {'xmin':    0.  , 'xmax':  30.               }),
            ('qr',       {'xmin':    0.  , 'xmax':   3.               }), 
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
        'dtlabel'  : '1h'                ,
        'xname'    : '24 June 1969 (UTC)',
        'variables': OrderedDict([
            ('w_up',     {'levels': [i*0.2 for i in range(0,16,1)]              , 'extend':'max', 'firstwhite':True }),
            ('alpha_up', {'levels': [0,0.01,0.1,1]+[i*2. for i in range(1,16,1)], 'extend':'max', 'firstwhite':True }),
            ('Mf',       {'levels': [0,0.001]+[i*0.01 for i in range(1,19,1)]   , 'extend':'max', 'firstwhite':True }),
            ('dTv_up',   {'levels': [i*0.1 for i in range(-7,8,1)]              , 'extend':'both'                   }),
            ('B_up',     {'levels': [i*0.005 for i in range(-7,8,1)]            , 'extend':'both'                   }),
            ('eps_u',    {'levels': [i*0.5 for i in range(0,15,1)]              , 'extend':'both'                   }),
            ('det_u',    {'levels': [i*0.5 for i in range(0,15,1)]              , 'extend':'both'                   }),
        ]),
    }), # end 2D_conv
    #######################
    ("hour7-8_conv",{
        'head'     : 'Convection 7-8h'      ,
        'type'     : 'plotAvgP'             ,
        'tmin'     : tmin.add(7,cdtime.Hour),
        'tmax'     : tmin.add(8,cdtime.Hour),  
        'ymin'     : 0.                     ,
        'ymax'     : 4.                     ,
        'yname'    : 'altitude (km)'        ,
        'levunits' : 'km'                   ,
        'rtitle'   : '7-8 hour'             ,        
        'variables': OrderedDict([
            ('w_up',     {'xmin':    0.  , 'xmax':   4.               }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.               }),
            ('Mf',       {'xmin':    0.  , 'xmax':   0.3, 'lev':'zh'  }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.               }),
            ('B_up',     {'xmin':   -0.02, 'xmax':   0.02             }),
            ('eps_u',    {'xmin':   -0.5 , 'xmax':   5.               }),
            ('det_u',    {'xmin':   -0.5 , 'xmax':   5.               }),            
        ]),
    }), # end hour7-8_conv
    #######################
    ("hour9-10_conv",{
        'head'     : 'Convection 9-10h'      ,
        'type'     : 'plotAvgP'              ,
        'tmin'     : tmin.add(9,cdtime.Hour) ,
        'tmax'     : tmin.add(10,cdtime.Hour),  
        'ymin'     : 0.                      ,
        'ymax'     : 4.                      ,
        'yname'    : 'altitude (km)'         ,
        'levunits' : 'km'                    ,
        'rtitle'   : '9-10 hour'             ,        
        'variables': OrderedDict([
            ('w_up',     {'xmin':    0.  , 'xmax':   4.               }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.               }),
            ('Mf',       {'xmin':    0.  , 'xmax':   0.3, 'lev':'zh'  }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.               }),
            ('B_up',     {'xmin':   -0.02, 'xmax':   0.02             }),
            ('eps_u',    {'xmin':   -0.5 , 'xmax':   5.               }),
            ('det_u',    {'xmin':   -0.5 , 'xmax':   5.               }),            
        ]),
    }), # end hour9-10_conv  
    #######################
    ("init",{
        'head'     : 'Init'         ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 20.            ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('u',     {'xmin': -12., 'xmax':    0.}),
            ('v',     {'xmin':  -3., 'xmax':    3.}),
            ('theta', {'xmin': 295., 'xmax':  450.}),
            ('qv',    {'xmin':  -1., 'xmax':   18.}),
            ('ql',    {'xmin':  -1., 'xmax':   20.}),
            ('qi',    {'xmin':  -1., 'xmax':    5.}),
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
            ('u',     {'xmin': -12., 'xmax':    0.}),
            ('v',     {'xmin':  -3., 'xmax':    3.}),
            ('theta', {'xmin': 295., 'xmax':  325.}),
            ('qv',    {'xmin':  -1., 'xmax':   18.}),
            ('ql',    {'xmin':  -1., 'xmax':   20.}),
            ('qi',    {'xmin':  -1., 'xmax':    5.}),
            ('tke',   {'xmin':  -1., 'xmax':    1., 'lev':'zh'}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
