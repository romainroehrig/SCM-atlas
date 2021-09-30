#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

import logging
logger = logging.getLogger(__name__)

from collections import OrderedDict

import atlas1d
from atlas1d.Diagnostic import Diagnostic

class DiagGroup:

    def __init__(self,name,head=None):

        # Name of the group of diagnostics
        self.name = name

        if head is None:
            self.head = self.name
        else:
            self.head = head

        # List of diagnostics
        self.diaglist = []

        self.datasets = None

    def info(self):
        print('*'*20)
        print('Group of diagnostic:', self.name)
        for diag in self.diaglist:
            diag.info()

    def add_diag(self,diag):

        self.diaglist.append(diag)

    def init_from_dict(self,diagnostics):

        if 'head' in diagnostics:
            self.head = diagnostics['head']

        if 'type' in diagnostics: # all diagnostic of this group are of same type
            diag_type = diagnostics['type']
            plotdico0 = {}
            for att in diagnostics.keys():
                if not(att in ['type','variables','head']):
                    plotdico0[att] = diagnostics[att]
            for var in diagnostics['variables']:
                plotdico = {}
                for att in diagnostics['variables'][var].keys():
                    plotdico[att] = diagnostics['variables'][var][att]
                plotdico.update(plotdico0)
                diag = Diagnostic(diag_type=diag_type,variable=var,plot_details=plotdico)

                self.add_diag(diag) 

        else:
            logger.error('not coded yet')
            raise NotImplementedError 

    def printOutput(self):

        print('-'*40)
        print('--- Output for group of diagnostics {0}:'.format(self.name))
        for diag in self.diaglist:
            diag.printOutput()

    def printError(self):

        print('-'*40)
        print('--- Errors for group of diagnostics {0}:'.format(self.name))
        for diag in self.diaglist:
            diag.printError()

    def run(self,datasets,root_dir=None,lcompute=True):

        if root_dir is None:
            logger.error('root_dir is None for DiagGroup {0}'.format(self.name))
            raise ValueError
        
        loc_dir = '{0}/{1}'.format(root_dir,self.name)
        if not(os.path.exists(loc_dir)):
            os.makedirs(loc_dir)

        # Update datasets of the present DiagGroup object
        self.datasets = datasets

        for diag in self.diaglist:
            diag.run(self.datasets,root_dir=loc_dir,lcompute=lcompute)

    def tohtml(self,index=None,root_dir=None):

        if root_dir is None:
            logger.error('root_dir is None for DiagGroup {0}'.format(self.name))
            raise ValueError

        diag_dir = '{0}/{1}'.format(root_dir,self.name)

        dat = self.datasets[0]

        width = 400
        ndiag_per_line = 4

        all2D = True
        all1D = True

        for diag in self.diaglist:
                all2D = all2D and (diag.diag_type == 'plot2D')
                all1D = all1D and ((diag.diag_type == 'plotTS') or (diag.diag_type == 'plotAvgP') or\
                                   (diag.diag_type == 'plotInitP'))

        f = open('{0}/{1}.html'.format(root_dir,self.name),'w')
        f.write('<head><title>{0}/{1}/{2}</title></head>\n'.format(dat.case,dat.subcase,self.name))
        f.write('<h1 style="text-align: center;">{0}/{1}: {2}</h1>\n'.format(dat.case,dat.subcase,self.head))
        #f.write('<a href="file://{0}">Back to main index</a>\n'.format(index))
        f.write('<a href="../../../html/index.html">Back to main index</a>\n')
        if all2D:
            for diag in self.diaglist:
                f.write('<ul><li><h3><span style="text-decoration: underline;"><strong>{0}</strong></span></h3></li></ul>\n'.format(diag.name))
                diags = list(diag.output.keys())
                ndiag = len(diags)
                if ndiag % 4 == 0:
                    nlines = ndiag//ndiag_per_line
                else:
                    nlines = ndiag//ndiag_per_line+1
                for i in range(0,nlines):
                    f.write('<table><tr>\n')
                    i1 = i*ndiag_per_line
                    i2 = min((i+1)*ndiag_per_line,ndiag)
                    for j in range(i1,i2):
                        #f.write('<td> <img src="file://{0}" style="width: {1}px;"/> </td>\n'.format(diag.output[diags[j]],width))
                        path = diag.output[diags[j]].split('/')
                        path = os.path.join('..',path[-2],path[-1])
                        f.write('<td> <img src="{0}" style="width: {1}px;"/> </td>\n'.format(path,width))
                    f.write('</tr></table>\n')
        elif all1D:
            nplot_per_line = 4
            nplot = len(self.diaglist)
            nlines = nplot//nplot_per_line
            for i in range(0,nlines+1):
                f.write('<table><tr>\n')
                for j in range(0,nplot_per_line):
                    if i*nplot_per_line+j < nplot:
                        #f.write('<td> <img src="file://{0}" style="width: {1}px;"/> </td>\n'.format(self.diaglist[i*nplot_per_line+j].output,width))
                        path = self.diaglist[i*nplot_per_line+j].output.split('/')
                        path = os.path.join('..',path[-2],path[-1])
                        f.write('<td> <img src="{0}" style="width: {1}px;"/> </td>\n'.format(self.diaglist[i*nplot_per_line+j].output,width))
                f.write('</tr></table>\n')
        else:
            logger.error('mixed case not coded yet')
            raise NotImplementedError

        f.close()

