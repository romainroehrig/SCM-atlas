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
       ('LES',{'ncfile': os.path.join(dir_references, 'LBA/LBA_LES_MESONH.nc'),  'line': 'k'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='LBA',subcase='REF',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for ARMCU atlas
####################################

tmin = datetime(1999,2,23,7,30)
tmax = datetime(1999,2,23,15)

diagnostics = OrderedDict([
    ("2D_dyn",{
        'head'     : 'Dynamics (2D)'     ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,
        'ymin'     :    0.               ,
        'ymax'     :   18.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '1h'                ,
        'xname'    : '23 February 1999 (UTC)',
        'variables': OrderedDict([
            ('ua', {'levels': list(range(-10,11,2)), 'extend':'both'}),
            ('va', {'levels': list(range(-6,7,1)),   'extend':'both'}),
        ]),
    }), # end 2D_dyn
    #######################
    ("2D_thermo",{
        'head'     : 'Thermo (2D)'       ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :    6.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '1h'                ,
        'xname'    : '23 February 1999 (UTC)',
        'variables': OrderedDict([
            #('theta', {'levels': list(range(300,321,1))   , 'extend':'both'                 }),
            ('thetal', {'levels': list(range(295,315,1))  , 'extend':'both'                 }),
            #('qv'   , {'levels': [0] + list(range(4,18,1)), 'extend':'max', 'cmap': cm.RdBu }),
            ('qt'   , {'levels': [0] + list(range(4,21,1)), 'extend':'max', 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_thermo
    #######################
    ("TS_surface",{
        'head'     : 'Surface (TS)'      ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '1h'                ,
        'xname'    : '23 February 1999 (UTC)',
        'variables': OrderedDict([
            ('hfss',  {'ymin':-40., 'ymax':  300.}),
            ('hfls',  {'ymin':  0., 'ymax':  600.}),
            ('ustar', {'ymin':  0., 'ymax':    1.}),
            ('ts',    {'ymin':280., 'ymax':  320.}),
            ('pr',    {'ymin':  0., 'ymax':   40.}),
        ]),
    }), # end TS_surface         
    #######################
    ("2D_cloud",{
        'head'     : 'Clouds (2D)'       ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :   18.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '1h'                ,
        'xname'    : '23 February 1999 (UTC)',
        'variables': OrderedDict([
            ('cl' , {'levels': [0,1] + list(range(4,21,2)), 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('ql' , {'levels': list(range(0,41,4)),         'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qi' , {'levels': list(range(0,41,4)),         'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qc' , {'levels': list(range(0,41,4)),         'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qr' , {'levels': list(range(0,41,4)),         'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qsn', {'levels': list(range(0,21,2)),         'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qg' , {'levels': list(range(0,21,2)),         'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qp' , {'levels': list(range(0,21,2)),         'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_cloud
    #######################
    ("TS_cloud",{
        'head'     : 'Clouds (TS)'       ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '1h'                ,
        'xname'    : '23 February 1999 (UTC)',
        'variables': OrderedDict([
            ('clt', {'ymin':  0., 'ymax':   100.}),
            ('zcb', {'ymin':  0., 'ymax':  4000.}),
            ('zct', {'ymin':  0., 'ymax': 18000.}),
            ('lwp', {'ymin':  0., 'ymax':   300.}),            
            ('iwp', {'ymin':  0., 'ymax':   300.}),            
            ('rwp', {'ymin':  0., 'ymax':   300.}),            
            ('swp', {'ymin':  0., 'ymax':   300.}),            
            ('gwp', {'ymin':  0., 'ymax':   300.}),            
        ]),
    }), # end TS_cloud  
    #######################
    ("hour2-3_basic",{
        'head'     : 'Basic 2-3h'             ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=2),
        'tmax'     : tmin + timedelta(hours=3),  
        'ymin'     : 0.                       ,
        'ymax'     : 18.                      ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '2-3 hour'               ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -15.  , 'xmax':  15. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':   6. , 'init':True }),
            ('theta',  {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('qv',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax': 100.               }),
            ('ql',     {'xmin':    0.  , 'xmax': 100.               }),
            ('qi',     {'xmin':    0.  , 'xmax': 100.               }),
            ('qc',     {'xmin':    0.  , 'xmax': 100.               }),
            ('qr',     {'xmin':    0.  , 'xmax': 100.               }),
            ('qsn',    {'xmin':    0.  , 'xmax': 100.               }),
            ('qg',     {'xmin':    0.  , 'xmax': 100.               }),
            ('qp',     {'xmin':    0.  , 'xmax': 100.               }),
        ]),
    }), # end hour2-3_basic   
    #######################
    ("hour6-7_basic",{
        'head'     : 'Basic 6-7h'             ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=6),
        'tmax'     : tmin + timedelta(hours=7),  
        'ymin'     : 0.                       ,
        'ymax'     : 18.                      ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '6-7 hour'               ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -15.  , 'xmax':  15. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':   6. , 'init':True }),
            ('theta',  {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('qv',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax': 100.               }),
            ('ql',     {'xmin':    0.  , 'xmax': 100.               }),
            ('qi',     {'xmin':    0.  , 'xmax': 100.               }),
            ('qc',     {'xmin':    0.  , 'xmax': 100.               }),
            ('qr',     {'xmin':    0.  , 'xmax': 100.               }),
            ('qsn',    {'xmin':    0.  , 'xmax': 100.               }),
            ('qg',     {'xmin':    0.  , 'xmax': 100.               }),
            ('qp',     {'xmin':    0.  , 'xmax': 100.               }),
        ]),
    }), # end hour6-7_basic    
    #######################
    ("2D_conv",{
        'head'     : 'Convection (2D)'   ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :   18.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '1h'                ,
        'xname'    : '23 February 1999 (UTC)',
        'variables': OrderedDict([
            ('wa_up',    {'levels': list(range(0,16,1))                 , 'extend':'max', 'firstwhite':True }),
            ('alpha_up', {'levels': [0,0.01,0.1,1.] + [i*2. for i in range(1,16,1)], 'extend':'max', 'firstwhite':True }),
            ('mf_up',    {'levels': [0,0.001]+[i*0.01 for i in range(1,16,1)] , 'extend':'max', 'firstwhite':True }),
            ('dTv_up',   {'levels': [i*0.1 for i in range(-7,8,1)]                 , 'extend':'both'                   }),
            ('b_up',     {'levels': [i*0.005 for i in range(-7,8,1)]               , 'extend':'both'                   }),
            ('ent_up',   {'levels': [i*0.5 for i in range(0,15,1)]                 , 'extend':'both'                   }),
            ('det_up',   {'levels': [i*0.02 for i in range(0,15,1)]                , 'extend':'both'                   }),
        ]),
    }), # end 2D_conv
    #######################
    ("hour2-3_conv",{
        'head'     : 'Convection 2-3h'        ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=2),
        'tmax'     : tmin + timedelta(hours=3),
        'ymin'     : 0.                       ,
        'ymax'     : 18.                      ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '2-3 hour'               ,        
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':  20.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.1 }),
            ('dTv_up',   {'xmin':   -2.  , 'xmax':   2.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour2-3_conv
    #######################
    ("hour6-7_conv",{
        'head'     : 'Convection 6-7h'        ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=6),
        'tmax'     : tmin + timedelta(hours=7),
        'ymin'     : 0.                       ,
        'ymax'     : 18.                      ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '6-7 hour'               ,        
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':  20.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.1 }),
            ('dTv_up',   {'xmin':   -2.  , 'xmax':   2.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour6-7_conv  
    #######################
    ("init",{
        'head'     : 'Init'         ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 30.            ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('ua',     {'xmin': -20., 'xmax':   20.}),
            ('va',     {'xmin': -10., 'xmax':   10.}),
            ('theta',  {'xmin': 295., 'xmax':  450.}),
            ('thetal', {'xmin': 295., 'xmax':  450.}),
            ('qv',     {'xmin':  -1., 'xmax':   20.}),
            ('qt',     {'xmin':  -1., 'xmax':   20.}),
            ('ql',     {'xmin':  -1., 'xmax':  100.}),
            ('qi',     {'xmin':  -1., 'xmax':  100.}),
            ('tke',    {'xmin':  -1., 'xmax':    1.}),
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
            ('ua',     {'xmin':  -5., 'xmax':    5.}),
            ('va',     {'xmin':  -7., 'xmax':    7.}),
            ('theta',  {'xmin': 295., 'xmax':  325.}),
            ('thetal', {'xmin': 295., 'xmax':  325.}),
            ('qv',     {'xmin':  -1., 'xmax':   20.}),
            ('qt',     {'xmin':  -1., 'xmax':   20.}),
            ('ql',     {'xmin':  -1., 'xmax':  100.}),
            ('qi',     {'xmin':  -1., 'xmax':  100.}),
            ('tke',    {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
