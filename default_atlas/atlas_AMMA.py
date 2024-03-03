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
       ('LES',{'ncfile': os.path.join(dir_references, 'AMMA.new/AMMA_LES_MESONH.nc'),  'line': 'k'}),
       ('LES0',{'ncfile': os.path.join(dir_references, 'AMMA/AMMA_LES_MESONH_RR.nc'),  'line': 'grey'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='AMMA',subcase='REF',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for ARMCU atlas
####################################

tmin = datetime(2006,7,10,6)
tmax = datetime(2006,7,10,18)

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
        'xname'    : '10 July 2006 (UTC)',
        'variables': OrderedDict([
            ('ua', {'levels': list(range(-12,13,2))           , 'extend':'both'}),
            ('va', {'levels': [i*0.5 for i in range(-6,7,1)], 'extend':'both'}),
        ]),
    }), # end 2D_dyn
    #######################
    ("2D_thermo",{
        'head'     : 'Thermo (2D)'       ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :   18.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '1h'                ,
        'xname'    : '10 July 2006 (UTC)',
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
        'dtlabel'  : '1h'                ,
        'xname'    : '10 July 2006 (UTC)',
        'variables': OrderedDict([
            ('hfss',  {'ymin':-40., 'ymax':  400.}),
            ('hfls',  {'ymin':  0., 'ymax':  100.}),
            ('ustar', {'ymin':  0., 'ymax':    1.}),
            ('ts',    {'ymin':280., 'ymax':  320.}),
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
        'ymax'     :   18.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '1h'                ,
        'xname'    : '10 July 2006 (UTC)',
        'variables': OrderedDict([
            ('cl' , {'levels': [0,1] + list(range(4,21,2))   , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('ql' , {'levels': list(range(0,41,4))           , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qi' , {'levels': list(range(0,41,4))           , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qc' , {'levels': list(range(0,41,4))           , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qr' , {'levels': [i*4 for i in range(0,11,1)], 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qsn', {'levels': [i*4 for i in range(0,11,1)], 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qg' , {'levels': [i*4 for i in range(0,11,1)], 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qp' , {'levels': [i*4 for i in range(0,11,1)], 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_cloud
    #######################
    ("TS_cloud",{
        'head'     : 'Clouds (TS)'       ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '1h'                ,
        'xname'    : '10 July 2006 (UTC)',
        'variables': OrderedDict([
            ('clt',  {'ymin':  0., 'ymax':   100.}),
            ('zcb', {'ymin':  0., 'ymax':  4000.}),
            ('zct', {'ymin':  0., 'ymax': 18000.}),
            ('lwp', {'ymin':  0., 'ymax':   100.}),            
            ('iwp', {'ymin':  0., 'ymax':   100.}),            
            ('rwp', {'ymin':  0., 'ymax':   200.}),            
            ('swp', {'ymin':  0., 'ymax':   200.}),            
            ('gwp', {'ymin':  0., 'ymax':   200.}),            
        ]),
    }), # end TS_cloud  
    #######################
    # Convective Boundary Layer - 8-10h LT
    ("CBL_basic",{
        'head'     : 'Basic CBL'              ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=2), # 8h LT
        'tmax'     : tmin + timedelta(hours=4), # 10h LT  
        'ymin'     : 0.                       ,
        'ymax'     : 6.                       ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '8-10h LT'                  ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -20.  , 'xmax':  20. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':   6. , 'init':True }),
            #('theta',  {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            #('qv',     {'xmin':    0.  , 'xmax':  18. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax':  40.               }),
            ('ql',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qr',     {'xmin':    0.  , 'xmax':  10.               }),
        ]),
    }), # end CBL_basic   
    #######################
    # Shallow convection phase
    ("shallow_basic",{
        'head'     : 'Basic Shallow'       ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=4), # 10h LT
        'tmax'     : tmin + timedelta(hours=8), # 14h LT
        'ymin'     : 0.                       ,
        'ymax'     : 6.                      ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '10-14h LT'                 ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -20.  , 'xmax':  20. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':   6. , 'init':True }),
            #('theta',  {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            #('qv',     {'xmin':    0.  , 'xmax':  18. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax':  40.               }),
            ('ql',     {'xmin':    0.  , 'xmax':  60.               }),
            ('qr',     {'xmin':    0.  , 'xmax':  10.               }),
        ]),
    }), # end shallow_basic    
    #######################
    # Congestus phase
    ("congestus_basic",{
        'head'     : 'Basic Congestus'        ,
        'type'     : 'plotAvgP'                  ,
        'tmin'     : tmin + timedelta(hours=9)   , # 15h LT
        'tmax'     : tmin + timedelta(hours=10, minutes=30), # 16h30 LT  
        'ymin'     : 0.                          ,
        'ymax'     : 18.                         ,
        'yname'    : 'altitude (km)'             ,
        'levunits' : 'km'                        ,
        'rtitle'   : '15-16h30 LT'                  ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -20.  , 'xmax':  20. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':   6. , 'init':True }),
            #('theta',  {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            #('qv',     {'xmin':    0.  , 'xmax':  18. , 'init':True }),
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
    }), # end congestus_basic    
    #######################
    # Deep convection phase 16h30-18h LT
    ("deep_basic",{
        'head'     : 'Basic Deep'                ,
        'type'     : 'plotAvgP'                  ,
        'tmin'     : tmin + timedelta(hours=10, minutes=30), # 16h30 LT
        'tmax'     : tmin + timedelta(hours=12)  , # 18h LT 
        'ymin'     : 0.                          ,
        'ymax'     : 18.                         ,
        'yname'    : 'altitude (km)'             ,
        'levunits' : 'km'                        ,
        'rtitle'   : '16h30-18h LT'              ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -20.  , 'xmax':  20. , 'init':True }),
            ('va',     {'xmin':   -6.  , 'xmax':   6. , 'init':True }),
            #('theta',  {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  300.  , 'xmax': 325. , 'init':True }),
            #('qv',     {'xmin':    0.  , 'xmax':  18. , 'init':True }),
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
    }), # end deep_basic    
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
        'xname'    : '10 July 2006 (UTC)',
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
    ("CBL_conv",{
        'head'     : 'Convection CBL'        ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=2), # 8h LT
        'tmax'     : tmin + timedelta(hours=4), # 10h LT
        'ymin'     : 0.                       ,
        'ymax'     : 6.                       ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '8-10h LT'               ,        
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end CBL_conv
    #######################
    ("shallow_conv",{
        'head'     : 'Convection Shallow'     ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=4), # 10h LT
        'tmax'     : tmin + timedelta(hours=8), # 14h LT
        'ymin'     : 0.                       ,
        'ymax'     : 6.                       ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '10-14h LT'              ,        
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end shallow_conv  
    #######################
    ("congestus_conv",{
        'head'     : 'Convection Congestus'     ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=9), # 15h LT
        'tmax'     : tmin + timedelta(hours=10, minutes=30), # 16h30 LT
        'ymin'     : 0.                       ,
        'ymax'     : 18.                      ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '15-16h30 LT'              ,        
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end shallow_conv 
    #######################
    ("deep_conv",{
        'head'     : 'Convection Deep'         ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=10, minutes=30), # 16h30 LT
        'tmax'     : tmin + timedelta(hours=12), # 18h LT
        'ymin'     : 0.                        ,
        'ymax'     : 18.                       ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '16h30-18h LT'            ,        
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end deep_conv 
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
