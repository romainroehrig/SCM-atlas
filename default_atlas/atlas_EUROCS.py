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
       ('LES',{'ncfile': os.path.join(dir_references, 'EUROCS/EUROCS_LES_MESONH.nc'),  'line': 'k'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='EUROCS',subcase='REF',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for ARMCU atlas
####################################

tmin = datetime(1997,6,27,11,30)
tmax = datetime(1997,7,1,11,30)

diagnostics = OrderedDict([
    ("2D_dyn",{
        'head'     : 'Dynamics (2D)'     ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,
        'ymin'     :    0.               ,
        'ymax'     :   14.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '27 June - 1 July 1997 (UTC)',
        'variables': OrderedDict([
            ('ua', {'levels': list(range(-16,17,2)), 'extend':'both'}),
            ('va', {'levels': list(range(-7,8,1)),   'extend':'both'}),
        ]),
    }), # end 2D_dyn
    #######################
    ("2D_thermo",{
        'head'     : 'Thermo (2D)'       ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :    8.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '27 June - 1 July 1997 (UTC)',
        'variables': OrderedDict([
            #('theta', {'levels': list(range(300,321,1))   , 'extend':'both'                 }),
            ('thetal', {'levels': list(range(300,321,1))  , 'extend':'both'                 }),
            #('qv'   , {'levels': [0] + list(range(4,18,1)), 'extend':'max', 'cmap': cm.RdBu }),
            ('qt'   , {'levels': [0] + list(range(4,18,1)), 'extend':'max', 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_thermo
    #######################
    ("TS_surface",{
        'head'     : 'Surface (TS)'      ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '6h'                ,
        'xname'    : '27 June - 1 July 1997 (UTC)',
        'variables': OrderedDict([
            ('hfss',  {'ymin':-50., 'ymax':  150.}),
            ('hfls',  {'ymin':  0., 'ymax':  500.}),
            ('ustar', {'ymin':  0., 'ymax':    1.}),
            ('ts',    {'ymin':280., 'ymax':  320.}),
            ('pr',    {'ymin':  0., 'ymax':   20.}),
        ]),
    }), # end TS_surface         
    #######################
    ("2D_cloud",{
        'head'     : 'Clouds (2D)'       ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :   14.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '27 June - 1 July 1997 (UTC)',
        'variables': OrderedDict([
            ('cl' , {'levels': [0,1] + list(range(4,21,2))   , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('ql' , {'levels': list(range(0,41,4))           , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qi' , {'levels': list(range(0,41,4))           , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qc' , {'levels': list(range(0,41,4))           , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qr' , {'levels': list(range(0,151,10))         , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qsn', {'levels': list(range(0,151,10))         , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qg' , {'levels': list(range(0,151,10))         , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qp' , {'levels': list(range(0,151,10))         , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_cloud
    #######################
    ("TS_cloud",{
        'head'     : 'Clouds (TS)'       ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '6h'                ,
        'xname'    : '27 June - 1 July 1997 (UTC)',
        'variables': OrderedDict([
            ('clt', {'ymin':  0., 'ymax':   100.}),
            ('zcb', {'ymin':  0., 'ymax':  4000.}),
            ('zct', {'ymin':  0., 'ymax': 18000.}),
            ('lwp', {'ymin':  0., 'ymax':   500.}),            
            ('iwp', {'ymin':  0., 'ymax':   500.}),            
            ('rwp', {'ymin':  0., 'ymax':   500.}),            
            ('swp', {'ymin':  0., 'ymax':   500.}),            
            ('gwp', {'ymin':  0., 'ymax':   500.}),            
        ]),
    }), # end TS_cloud  
    #######################
    ("hour15-18h_day1_basic",{
        'head'     : 'Basic 15-18h Day 1'         ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=3, minutes=30),
        'tmax'     : tmin + timedelta(hours=6, minutes=30),  
        'ymin'     : 0.                        ,
        'ymax'     : 14.                       ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '15-18h Day 1'            ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -15.  , 'xmax':  15. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':   6. , 'init':True }),
            ('theta',  {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  290.  , 'xmax': 325. , 'init':True }),
            ('qv',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax':  40.               }),
            ('ql',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qi',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qc',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qr',     {'xmin':    0.  , 'xmax':  10.               }),
            ('qsn',    {'xmin':    0.  , 'xmax':  10.               }),
            ('qg',     {'xmin':    0.  , 'xmax':  10.               }),
            ('qp',     {'xmin':    0.  , 'xmax':  10.               }),
        ]),
    }), # end hour15-18_day1_basic
    #######################
    ("hour15-18h_day2_basic",{
        'head'     : 'Basic 15-18h Day 2'         ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=27, minutes=30),
        'tmax'     : tmin + timedelta(hours=30, minutes=30),  
        'ymin'     : 0.                        ,
        'ymax'     : 14.                       ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '15-18h Day 2'            ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -15.  , 'xmax':  15. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':   6. , 'init':True }),
            ('theta',  {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  290.  , 'xmax': 325. , 'init':True }),
            ('qv',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax':  40.               }),
            ('ql',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qi',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qc',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qr',     {'xmin':    0.  , 'xmax':  10.               }),
            ('qsn',    {'xmin':    0.  , 'xmax':  10.               }),
            ('qg',     {'xmin':    0.  , 'xmax':  10.               }),
            ('qp',     {'xmin':    0.  , 'xmax':  10.               }),
        ]),
    }), # end hour15-18_day2_basic
    #######################
    ("hour15-18h_day3_basic",{
        'head'     : 'Basic 15-18h Day 3'         ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=51, minutes=30),
        'tmax'     : tmin + timedelta(hours=53, minutes=30),  
        'ymin'     : 0.                        ,
        'ymax'     : 14.                       ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '15-18h Day 3'            ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -15.  , 'xmax':  15. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':   6. , 'init':True }),
            ('theta',  {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  290.  , 'xmax': 325. , 'init':True }),
            ('qv',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax':  40.               }),
            ('ql',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qi',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qc',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qr',     {'xmin':    0.  , 'xmax':  10.               }),
            ('qsn',    {'xmin':    0.  , 'xmax':  10.               }),
            ('qg',     {'xmin':    0.  , 'xmax':  10.               }),
            ('qp',     {'xmin':    0.  , 'xmax':  10.               }),
        ]),
    }), # end hour15-18_day3_basic
    #######################
    ("hour15-18h_day4_basic",{
        'head'     : 'Basic 15-18h Day 4'         ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=75, minutes=30),
        'tmax'     : tmin + timedelta(hours=78, minutes=30),  
        'ymin'     : 0.                        ,
        'ymax'     : 14.                       ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '15-18h Day 4'            ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -15.  , 'xmax':  15. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':   6. , 'init':True }),
            ('theta',  {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  290.  , 'xmax': 325. , 'init':True }),
            ('qv',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax':  40.               }),
            ('ql',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qi',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qc',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qr',     {'xmin':    0.  , 'xmax':  10.               }),
            ('qsn',    {'xmin':    0.  , 'xmax':  10.               }),
            ('qg',     {'xmin':    0.  , 'xmax':  10.               }),
            ('qp',     {'xmin':    0.  , 'xmax':  10.               }),
        ]),
    }), # end hour15-18_day4_basic
    #######################
    ("2D_conv",{
        'head'     : 'Convection (2D)'   ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :    14.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '21 June 1997 (UTC)',
        'variables': OrderedDict([
            ('wa_up',    {'levels': [i*0.2 for i in range(0,16,1)]                 , 'extend':'max', 'firstwhite':True }),
            ('alpha_up', {'levels': [0,0.01,0.1,1.] + [i*2. for i in range(1,16,1)], 'extend':'max', 'firstwhite':True }),
            ('mf_up',    {'levels': [0,0.001,0.01]+[i*0.02 for i in range(1,16,1)] , 'extend':'max', 'firstwhite':True }),
            ('dTv_up',   {'levels': [i*0.1 for i in range(-7,8,1)]                 , 'extend':'both'                   }),
            ('b_up',     {'levels': [i*0.005 for i in range(-7,8,1)]               , 'extend':'both'                   }),
            ('ent_up',   {'levels': [i*0.5 for i in range(0,15,1)]                 , 'extend':'both'                   }),
            ('det_up',   {'levels': [i*0.5 for i in range(0,15,1)]                 , 'extend':'both'                   }),
        ]),
    }), # end 2D_conv
    #######################
    ("hour15-18_day1_conv",{
        'head'     : 'Convection 15-18h Day 1' ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=3, minutes=30),
        'tmax'     : tmin + timedelta(hours=6, minutes=30),  
        'ymin'     : 0.                        ,
        'ymax'     : 14.                       ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '15-18h Day 1'            ,
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour15-18_day1_conv
    #######################
    ("hour15-18_day2_conv",{
        'head'     : 'Convection 15-18h Day 2' ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=27, minutes=30),
        'tmax'     : tmin + timedelta(hours=30, minutes=30),  
        'ymin'     : 0.                        ,
        'ymax'     : 14.                       ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '15-18h Day 2'            ,
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end hour15-18_day2_conv
    #######################
    ("init",{
        'head'     : 'Init'         ,
        'type'     : 'plotInitP'    ,
        'ymin'     : 0.             ,
        'ymax'     : 20.            ,
        'yname'    : 'altitude (km)',
        'levunits' : 'km'           ,
        'variables': OrderedDict([
            ('ua',     {'xmin': -20., 'xmax':   20.}),
            ('va',     {'xmin':  -7., 'xmax':    7.}),
            ('theta',  {'xmin': 295., 'xmax':  450.}),
            ('thetal', {'xmin': 295., 'xmax':  450.}),
            ('qv',     {'xmin':  -1., 'xmax':   18.}),
            ('qt',     {'xmin':  -1., 'xmax':   18.}),
            ('ql',     {'xmin':  -1., 'xmax':   10.}),
            ('qi',     {'xmin':  -1., 'xmax':   10.}),
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
            ('ua',     {'xmin': -20., 'xmax':   20.}),
            ('va',     {'xmin':  -7., 'xmax':    7.}),
            ('theta',  {'xmin': 295., 'xmax':  325.}),
            ('thetal', {'xmin': 295., 'xmax':  325.}),
            ('qv',     {'xmin':  -1., 'xmax':   18.}),
            ('qt',     {'xmin':  -1., 'xmax':   18.}),
            ('ql',     {'xmin':  -1., 'xmax':   10.}),
            ('qi',     {'xmin':  -1., 'xmax':   10.}),
            ('tke',    {'xmin':  -1., 'xmax':    1.}),
        ]),
    }), # end initLL 
    #######################    
]) # end diagnostics
