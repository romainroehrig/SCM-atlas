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
       ('LES',{'ncfile': os.path.join(dir_references, 'KB2006/KB2006_LES_MESONH.nc'),  'line': 'k'}),
       ])

references = []
for ref in tmp.keys():
    references.append(Dataset(name=ref,case='KB2006',subcase='MESONH',ncfile=tmp[ref]['ncfile'],line=tmp[ref]['line']))

####################################
# Configuration file for ARMCU atlas
####################################

tmin = datetime(2001,9,27,0)
tmax = datetime(2001,10,2,0)

diagnostics = OrderedDict([
    ("2D_dyn",{
        'head'     : 'Dynamics (2D)'     ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,
        'ymin'     :    0.               ,
        'ymax'     :    8.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '27 Sept - 1 Oct 2001 (UTC)',
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
        'ymax'     :    8.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '27 Sept - 1 Oct 2001 (UTC)',
        'variables': OrderedDict([
            #('theta',  {'levels': list(range(300,321,1))   , 'extend':'both'                 }),
            ('thetal', {'levels': list(range(300,321,1))  , 'extend':'both'                 }),
            #('qv'   ,  {'levels': [0] + list(range(4,18,1)), 'extend':'max', 'cmap': cm.RdBu }),
            ('qt'   ,  {'levels': [0] + list(range(4,18,1)), 'extend':'max', 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_thermo
    #######################
    ("TS_surface",{
        'head'     : 'Surface (TS)'      ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '6h'                ,
        'xname'    : '27 Sept - 1 Oct 2001 (UTC)',
        'variables': OrderedDict([
            ('hfss',  {'ymin':-10., 'ymax':   50.}),
            ('hfls',  {'ymin':  0., 'ymax':  400.}),
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
        'ymax'     :    18.               ,
        'yname'    : 'altitude (km)'     ,
        'levunits' : 'km'                ,
        'dtlabel'  : '6h'                ,
        'xname'    : '27 Sept - 1 Oct 2001 (UTC)',
        'variables': OrderedDict([
            ('cl' , {'levels': [0,1] + list(range(4,21,2))     , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('ql' , {'levels': [0,0.1,2] + list(range(4,41,4)) , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qi' , {'levels': [0,0.1,1] +list(range(2,21,2))  , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qc' , {'levels': [0,0.1,2] +list(range(4,41,4))  , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qr' , {'levels': [i*0.5 for i in range(0,17,1)]  , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qsn', {'levels': [i*0.5 for i in range(0,17,1)]  , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
            ('qp' , {'levels': [i*0.5 for i in range(0,17,1)]  , 'extend':'max', 'firstwhite':True, 'cmap': cm.RdBu }),
        ]),
    }), # end 2D_cloud
    #######################
    ("TS_cloud",{
        'head'     : 'Clouds (TS)'       ,
        'type'     : 'plotTS'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'dtlabel'  : '6h'                ,
        'xname'    : '27 Sept - 1 Oct 2001 (UTC)',
        'variables': OrderedDict([
            ('clt', {'ymin':  0., 'ymax':   100.}),
            ('zcb', {'ymin':  0., 'ymax':  4000.}),
            ('zct', {'ymin':  0., 'ymax': 18000.}),
            ('lwp', {'ymin':  0., 'ymax':   100.}),            
            ('rwp', {'ymin':  0., 'ymax':    50.}),            
        ]),
    }), # end TS_cloud  
    #######################
    ("cumulus_basic",{
        'head'     : 'Basic Cumulus'          ,
        'type'     : 'plotAvgP'               ,
        'tmin'     : tmin + timedelta(hours=6),
        'tmax'     : tmin + timedelta(hours=12),  
        'ymin'     : 0.                       ,
        'ymax'     : 4.                       ,
        'yname'    : 'altitude (km)'          ,
        'levunits' : 'km'                     ,
        'rtitle'   : '6-12 hour (Cumulus)'    ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -10.  , 'xmax':  10. , 'init':True }),
            ('va',     {'xmin':   -3.  , 'xmax':   3. , 'init':True }),
            ('theta',  {'xmin':  295.  , 'xmax': 315. , 'init':True }),
            ('thetal', {'xmin':  295.  , 'xmax': 315. , 'init':True }),
            ('qv',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax':  20.               }),
            ('ql',     {'xmin':    0.  , 'xmax':  30.               }),
            ('qr',     {'xmin':    0.  , 'xmax':   4.               }),
        ]),
    }), # end cumulus_basic   
    #######################
    ("transition1_basic",{
        'head'     : 'Basic Transition 1'      ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=12) ,
        'tmax'     : tmin + timedelta(hours=60),  
        'ymin'     : 0.                        ,
        'ymax'     : 12.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '12-60 hour (Transition 1)' ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -10.  , 'xmax':  10. , 'init':True }),
            ('va',     {'xmin':   -3.  , 'xmax':   3. , 'init':True }),
            ('theta',  {'xmin':  295.  , 'xmax': 320. , 'init':True }),
            ('thetal', {'xmin':  295.  , 'xmax': 320. , 'init':True }),
            ('qv',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax':  20.               }),
            ('ql',     {'xmin':    0.  , 'xmax':  20.               }),
            ('qi',     {'xmin':    0.  , 'xmax':  20.               }),
            ('qc',     {'xmin':    0.  , 'xmax':  20.               }),
            ('qr',     {'xmin':    0.  , 'xmax':   5.               }),
            ('qsn',    {'xmin':    0.  , 'xmax':   5.               }),
            ('qp',     {'xmin':    0.  , 'xmax':   5.               }),
        ]),
    }), # end trnasition1_basic  
    #######################
    ("transition2_basic",{
        'head'     : 'Basic Transition 2'       ,
        'type'     : 'plotAvgP'                 ,
        'tmin'     : tmin + timedelta(hours=60) ,
        'tmax'     : tmin + timedelta(hours=90) ,  
        'ymin'     : 0.                         ,
        'ymax'     : 12.                        ,
        'yname'    : 'altitude (km)'            ,
        'levunits' : 'km'                       ,
        'rtitle'   : '60-90 hour (Transition 2)',        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -10.  , 'xmax':  10. , 'init':True }),
            ('va',     {'xmin':   -3.  , 'xmax':   3. , 'init':True }),
            ('theta',  {'xmin':  295.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  295.  , 'xmax': 325. , 'init':True }),
            ('qv',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax':  20.               }),
            ('ql',     {'xmin':    0.  , 'xmax':  20.               }),
            ('qi',     {'xmin':    0.  , 'xmax':  20.               }),
            ('qc',     {'xmin':    0.  , 'xmax':  20.               }),
            ('qr',     {'xmin':    0.  , 'xmax':  20.               }),
            ('qsn',    {'xmin':    0.  , 'xmax':  20.               }),
            ('qp',     {'xmin':    0.  , 'xmax':  20.               }),
        ]),
    }), # end trnasition2_basic
    #######################
    ("deep_basic",{
        'head'     : 'Basic Deep'               ,
        'type'     : 'plotAvgP'                 ,
        'tmin'     : tmin + timedelta(hours=90) ,
        'tmax'     : tmin + timedelta(hours=120),  
        'ymin'     : 0.                         ,
        'ymax'     : 12.                        ,
        'yname'    : 'altitude (km)'            ,
        'levunits' : 'km'                       ,
        'rtitle'   : '90-120 hour (Deep)'       ,        
        'variables': OrderedDict([
            ('ua',     {'xmin':  -10.  , 'xmax':  10. , 'init':True }),
            ('va',     {'xmin':   -3.  , 'xmax':   3. , 'init':True }),
            ('theta',  {'xmin':  295.  , 'xmax': 325. , 'init':True }),
            ('thetal', {'xmin':  295.  , 'xmax': 325. , 'init':True }),
            ('qv',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('qt',     {'xmin':    0.  , 'xmax':  20. , 'init':True }),
            ('cl',     {'xmin':    0.  , 'xmax':  20.               }),
            ('ql',     {'xmin':    0.  , 'xmax':  20.               }),
            ('qi',     {'xmin':    0.  , 'xmax':  20.               }),
            ('qc',     {'xmin':    0.  , 'xmax':  20.               }),
            ('qr',     {'xmin':    0.  , 'xmax':  40.               }),
            ('qsn',    {'xmin':    0.  , 'xmax':  40.               }),
            ('qp',     {'xmin':    0.  , 'xmax':  40.               }),
        ]),
    }), # end trnasition2_basic
    #######################
    ("2D_conv",{
        'head'     : 'Convection (2D)'   ,
        'type'     : 'plot2D'            ,
        'tmin'     : tmin                ,
        'tmax'     : tmax                ,        
        'ymin'     :    0.               ,
        'ymax'     :    18.              ,
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
    ("cumulus_conv",{
        'head'     : 'Convection Cumulus'      ,
        'type'     : 'plotAvgP'                ,
        'tmin'     : tmin + timedelta(hours=6) ,
        'tmax'     : tmin + timedelta(hours=12),
        'ymin'     : 0.                        ,
        'ymax'     : 4.                        ,
        'yname'    : 'altitude (km)'           ,
        'levunits' : 'km'                      ,
        'rtitle'   : '6-12 hour (Cumulus)'     ,        
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end cumulus_conv
    #######################
    ("transition1_conv",{
        'head'     : 'Convection Transition 1'  ,
        'type'     : 'plotAvgP'                 ,
        'tmin'     : tmin + timedelta(hours=12) ,
        'tmax'     : tmin + timedelta(hours=60) ,
        'ymin'     : 0.                         ,
        'ymax'     : 12.                        ,
        'yname'    : 'altitude (km)'            ,
        'levunits' : 'km'                       ,
        'rtitle'   : '12-60 hour (Transition 1)',        
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end transition1_conv 
    #######################
    ("transition2_conv",{
        'head'     : 'Convection Transition 2'  ,
        'type'     : 'plotAvgP'                 ,
        'tmin'     : tmin + timedelta(hours=60) ,
        'tmax'     : tmin + timedelta(hours=90) ,
        'ymin'     : 0.                         ,
        'ymax'     : 12.                        ,
        'yname'    : 'altitude (km)'            ,
        'levunits' : 'km'                       ,
        'rtitle'   : '60-90 hour (Transition 2)',        
        'variables': OrderedDict([
            ('wa_up',    {'xmin':    0.  , 'xmax':   4.  }),
            ('alpha_up', {'xmin':    0.  , 'xmax':  25.  }),
            ('mf_up',    {'xmin':    0.  , 'xmax':   0.3 }),
            ('dTv_up',   {'xmin':   -1.  , 'xmax':   1.  }),
            ('b_up',     {'xmin':   -0.02, 'xmax':   0.02}),
            ('ent_up',   {'xmin':   -0.5 , 'xmax':   5.  }),
            ('det_up',   {'xmin':   -0.5 , 'xmax':   5.  }),            
        ]),
    }), # end transition2_conv
    #######################
    ("deep_conv",{
        'head'     : 'Convection Deep'          ,
        'type'     : 'plotAvgP'                 ,
        'tmin'     : tmin + timedelta(hours=90) ,
        'tmax'     : tmin + timedelta(hours=120),
        'ymin'     : 0.                         ,
        'ymax'     : 12.                        ,
        'yname'    : 'altitude (km)'            ,
        'levunits' : 'km'                       ,
        'rtitle'   : '90-120 hour (Deep)'       ,        
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
