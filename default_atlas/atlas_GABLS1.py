# -*- coding:UTF-8 -*-

import sys
sys.path = ['./','../utils/'] + sys.path

from collections import OrderedDict

import cdtime
from matplotlib import cm # for colormaps

from Dataset import Dataset


####################################
# References for AYOTTE/00SC atlas
####################################

tmp = OrderedDict([
       ('MO'     ,  {'ncfile': '/Users/romainroehrig/data/GABLS1/files/MO_1m_allvar.nc'     , 'line': 'k'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='GABLS1',subcase='REF',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for GABLS1 atlas
####################################

tmin = cdtime.comptime(2000,1,1,10)
tmax = cdtime.comptime(2000,1,1,19)

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
            ('theta', {'levels': range(260,275,1), 'extend':'both'}),
            ('u',     {'levels': range(-1,9,1)   , 'extend':'both'}),
            ('v',     {'levels': range(-3,3,1)   , 'extend':'both'}),
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
        'head'     : 'Basic 7-8h'           ,
        'type'     : 'plotAvgP'             ,
        'tmin'     : tmin.add(7,cdtime.Hour),
        'tmax'     : tmin.add(8,cdtime.Hour),  
        'ymin'     : 0.                     ,
        'ymax'     : 400                    ,
        'yname'    : 'altitude (m)'         ,
        'levunits' : 'm'                    ,
        'rtitle'   : '7-8 hour'             ,        
        'variables': OrderedDict([
            ('u',        {'xmin':   -1. , 'xmax':  10. , 'init':True }),
            ('v',        {'xmin':   -3. , 'xmax':   3. , 'init':True }),
            ('theta',    {'xmin':  260. , 'xmax': 275. , 'init':True }),
        ]),
    }), # end hour7-8_basic   
    #######################
    ("hour8-9_basic",{
        'head'     : 'Basic 8-9h'           ,
        'type'     : 'plotAvgP'             ,
        'tmin'     : tmin.add(8,cdtime.Hour),
        'tmax'     : tmin.add(9,cdtime.Hour),  
        'ymin'     : 0.                     ,
        'ymax'     : 400                    ,
        'yname'    : 'altitude (m)'         ,
        'levunits' : 'm'                    ,
        'rtitle'   : '8-9 hour'             ,        
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
            ('tke',   {'xmin':  -1., 'xmax':    1., 'lev':'zh'}),
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
            ('tke',   {'xmin':  -1., 'xmax':    1., 'lev':'zh'}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
