#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os
import shutil

import logging
logger = logging.getLogger(__name__)

from collections import OrderedDict

import json

from matplotlib import cm # for colormaps

import atlas1d
import atlas1d.plotMUSC as plotMUSC
from atlas1d.new_variables import compute

from variables_info import variables_info, var2compute

lverbose = False

_known_diagnostics = ['plot2D','plotTS','plotInstP','plotAvgP','plotInitP']
_diag_names = {
        'plot2D':    '2D time-level plot'                 ,
        'plotTS':    'Time series plot'                   ,
        'plotInstP': 'Instantaneous vertical profile plot',
        'plotAvgP':  'Time average vertical profile plot' ,
        'plotInitP': 'Initial vertical profile plot' ,
        }

class Diagnostic:

    def __init__(self,diag_type=None,variable=None,plot_details=None):

        # Diagnostic type
        self.diag_type = diag_type

        # Variables involved
        self.variable = variable

        self.name = variables_info[self.variable]['name']

        # Dictionnary for plot details
        self.plot_details = plot_details

        # Output
        self.output = None

        # Error
        self.error = {}

    def set_type(self,diag_type):

        if diag_type in know_diagnostics:
            self.diag_type = diag_type
        else:
            logger.error('Diagnostic {0} is not known')
            logger.error('Known diagnostics are:', _known_diagnostics)
            for d in _know_diagnostics:
                logger.error('{0}: {1}'.format(d,_diag_names[d]))
            raise ValueError

    def info(self):
        print('-'*10)
        print('Diagnostic type: {0} ({1})'.format(self.diag_type,_diag_names[self.diag_type]))
        print('Diagnostic variable:', self.variable)
        print('Diagnostic plot details:')
        for att in ['tmin','tmax','dtlabel','xname','ymin','ymax','yname','levunits','levels','extend','cmap']: 
            if att in self.plot_details.keys():
                if att == 'cmap':
                    print(' '*5, '{0}:'.format(att), self.plot_details[att].name)
                else:
                    print(' '*5, '{0}:'.format(att), self.plot_details[att])

    def printOutput(self):
        if self.output is None:
            print('Diagnostic {0}/{1}: No output'.format(self.diag_type,self.variable))
        else:
            print('Diagnostic {0}/{1}, output:'.format(self.diag_type,self.variable))
            try:
                for key,value in self.output.items():
                    print('    {0}: {1}'.format(key,value))
            except AttributeError:
                print('    {0}'.format(self.output))
            except:
               raise        

    def printError(self):
        if self.error == {}:
            print('Diagnostic {0}/{1}: No error'.format(self.diag_type,self.variable))
        else:
            print('Diagnostic {0}/{1}, error with the following datasets:'.format(self.diag_type,self.variable))
            print([key for key in self.error.keys()])

    def run(self,datasets,root_dir=None,lcompute=True):

        if root_dir is None:
            logger.error('root_dir is None for DiagGroup {0}'.format(self.name))
            raise ValueError

        if not(os.path.exists(root_dir)):
            os.makedirs(root_dir)

        if lcompute:
            ncfiles = OrderedDict()

            if self.variable in var2compute:
                tmp_dir = '{0}/tmp/'.format(root_dir)
                if not(os.path.exists(tmp_dir)):
                    os.makedirs(tmp_dir)
                for dat in datasets:
                    fin = dat.ncfile
                    fout = '{0}/{1}.nc'.format(tmp_dir,dat.name)
                    try:
                        compute(fin, fout, self.variable)
                        ncfiles[dat.name] = fout
                    except (KeyError, AttributeError, FileNotFoundError) as e:
                        logger.debug(e)
                        ncfiles[dat.name] = dat.ncfile
                        pass
                    except:
                        raise
            else:
                for dat in datasets:
                    ncfiles[dat.name] = dat.ncfile  

            varloc = {}
            coefloc = {}
            for dat in datasets:
                if self.variable in dat.varnames:
                    varloc[dat.name] = dat.varname[self.variable]
                else:
                    varloc[dat.name] = self.variable
                if self.variable in dat.coefs:
                    coefloc[dat.name] = dat.coefs[self.variable]
                else:
                    coefloc[dat.name] = variables_info[self.variable]['coef']

        ############ 2D plot
        if self.diag_type == 'plot2D':

            if lcompute:
                plotdico = {
                    'lev'       : 'zhalf'                                                   ,
                    'minmax'    : True                                                      ,
                    'units'     : variables_info[self.variable]['units']                    ,
                    'title'     : '{0} ({1})'.format(variables_info[self.variable]['name']  ,
                                                     variables_info[self.variable]['units']),
                    'extend'    : 'neither'                                                 ,
                    'firstwhite': False                                                     ,
                    'cmap'      : cm.RdBu.reversed()                                        ,
                    }
                for key in self.plot_details.keys():
                    plotdico[key] = self.plot_details[key]

                plotdico['namefig'] = {}
                self.output = OrderedDict()
                for dat in datasets:
                    plotdico['namefig'][dat.name] = '{0}/2D_{2}_{1}.png'.format(root_dir,dat.name,self.variable)
                    self.output[dat.name] = plotdico['namefig'][dat.name]

                plotMUSC.plot2D(ncfiles,varloc,coef=coefloc,error=self.error,**plotdico)
                for e in self.error.keys():
                    del(self.output[e])

                with open('{0}/.output_{1}'.format(root_dir,self.variable), 'w') as f:
                    f.write(json.dumps(self.output))
            else:
                try:
                    with open('{0}/.output_{1}'.format(root_dir,self.variable), 'r') as f:
                        self.output = json.loads(f.read(),object_pairs_hook=OrderedDict)
                except IOError:
                    self.output = None
                    pass
                except:
                    raise

        ############ Time series plot
        elif self.diag_type == 'plotTS':

            if lcompute:
                lines = {}
                for dat in datasets:
                    lines[dat.name] = dat.line

                plotdico = {
                    'title'  : '{0} ({1})'.format(variables_info[self.variable]['name'],
                                                  variables_info[self.variable]['units']),
                    'lines'  : lines                                                     ,
                    'namefig': '{0}/TS_{1}.png'.format(root_dir,self.variable)           ,
                    }
                self.output = plotdico['namefig']
                for key in self.plot_details.keys():
                    plotdico[key] = self.plot_details[key]

                plotMUSC.plot_timeseries(ncfiles,varloc,coef=coefloc,error=self.error,**plotdico)
            else:
                self.output = '{0}/TS_{1}.png'.format(root_dir,self.variable)

        ############ Instantaneous vertical profile plot
        elif self.diag_type == 'plotInstP':

            logger.error('Not coded yet')
            raise NotImplementedError

        ############ Time-averaged vertical profile plot
        elif self.diag_type == 'plotAvgP':

            if lcompute:
                lines = {}
                for dat in datasets:
                    lines[dat.name] = dat.line

                plotdico = {
                    'title'  : '{0} ({1}) - {2}'.format(variables_info[self.variable]['name'],
                                                        variables_info[self.variable]['units'],
                                                        self.plot_details['rtitle']),
                    'lev'    : 'zfull'                                              ,
                    'init'   : False                                                ,
                    'lbias'  : False                                                ,
                    'units'  : variables_info[self.variable]['units']               ,
                    'lines'  : lines                                                ,
                    'lplot0' : True                                                 ,
                    'namefig': '{0}/AvgP_{1}.png'.format(root_dir,self.variable)    ,
                    }
                self.output = plotdico['namefig']
                for key in self.plot_details.keys():
                    if not(key in ['rtitle',]):
                        plotdico[key] = self.plot_details[key]
 
                plotMUSC.plot_profile(ncfiles,varloc,coef=coefloc,error=self.error,**plotdico)
            else:
                self.output = '{0}/AvgP_{1}.png'.format(root_dir,self.variable)

        ############ Instantaneous vertical profile plot
        elif self.diag_type == 'plotInitP':

            if lcompute:
                lines = {}
                for dat in datasets:
                    lines[dat.name] = dat.line
                plotdico = {
                    'title'  : '{0} ({1}) - First timestep'.format(variables_info[self.variable]['name'],
                                                                    variables_info[self.variable]['units']),
                    'lev'    : 'zfull'                                                                     ,
                    'init'   : False                                                                       ,
                    'lbias'  : False                                                                       ,
                    'units'  : variables_info[self.variable]['units']                                      ,
                    'lines'  : lines                                                                       ,
                    'lplot0' : True                                                                        ,
                    'namefig': '{0}/InitP_{1}.png'.format(root_dir,self.variable)                          ,
                    }
                self.output = plotdico['namefig']
                for key in self.plot_details.keys():
                     plotdico[key] = self.plot_details[key]

                plotMUSC.plot_profile(ncfiles,varloc,coef=coefloc,t0=True,error=self.error,**plotdico)
            else:
                self.output = '{0}/InitP_{1}.png'.format(root_dir,self.variable)

        ############ Unknown diagnostic
        else:
            logger.error('Diagnostic {0} is not known')
            logger.error('Known diagnostics are:', _known_diagnostics)
            for d in _know_diagnostics:
                logger.error('{0}: {1}'.format(d,_diag_names[d]))
            raise ValueError


        if lcompute:
            if self.variable in var2compute:
                 if os.path.exists(tmp_dir):
                      shutil.rmtree(tmp_dir)




