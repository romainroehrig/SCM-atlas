#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os
import importlib

import logging
logger = logging.getLogger(__name__)

from collections import OrderedDict

import atlas1d
from atlas1d.Atlas import Atlas

class MultiAtlas:

    def __init__(self,name,simulations={},root_dir=atlas1d._default_dirout,linfo=False):

        self.name = name

        if simulations == {}:
            logger.error('you must give at least one simulation')
            raise ValueError

        # Simulation datasets
        self.simulations = simulations

        # Model list
        self.models = OrderedDict()
        for case in self.simulations.keys():
            for subcase in self.simulations[case]:
                for sim in self.simulations[case][subcase]:
                    if not(sim.name in self.models.keys()):
                        self.models[sim.name] = sim.model

        # Root directory of the multi-atlas

        if root_dir[0] == '/':
            self.atlas_dir = '{0}/{1}'.format(root_dir,self.name)
        else:
            logger.error('root directory is expected to be given with an absolute path. root_dir=', root_dir)
            raise ValueError

        if not(os.path.exists(self.atlas_dir)):
            os.makedirs(self.atlas_dir)

        # pdf directory

        self.pdf_dir = '{}/pdf'.format(self.atlas_dir)

        # html directory

        self.html_dir = '{0}/html'.format(self.atlas_dir)

        # Atlas list
        self.atlaslist = []

        self.cases = []
        self.subcases = {}
        for case in simulations.keys():
            self.cases.append(case)
            self.subcases[case] = []
            for subcase in simulations[case]:
                self.subcases[case].append(subcase)

                try:
                    config = importlib.import_module('atlas_{0}_{1}'.format(case,subcase))
                except:
                    try:
                        config = importlib.import_module('atlas_{0}'.format(case))
                    except:
                        logger.error('Cannot find a atlas config files in {0}/../default_atlas/ for case {1}, subcase {2}'.format(
                            atlas1d._dir_atlas_config_default,case,subcase))
                        logger.error('or in user-defined ATLAS_CONFIG directory: {0}'.format(atlas1d._dir_atlas_config))
                        raise

                tmp = Atlas('{0}/{1}'.format(case,subcase),references=config.references,simulations=simulations[case][subcase],root_dir=self.atlas_dir)
                tmp.init_from_dict(config.diagnostics)
                if linfo:
                    tmp.info(references=True,simulations=True,groups=True)

                self.atlaslist.append(tmp)

        # Initialize output if avalaible
        self.run(lcompute=False,lverbose=False)

    def info(self):
        print('### Multi Atlas {0} ###'.format(self.name))
        print('Multi atlas directory:', self.atlas_dir)
        print('Cases:')
        for c in self.cases:
            print('  {0}: {1}'.format(c,self.subcases[c]))
        for a in self.atlaslist:
            a.info(references=True,simulations=True)


    def run(self,cases=None,subcases=None,lcompute=True,lverbose=True):

        if cases is None:
            for atlas in self.atlaslist:
                logger.debug(atlas.name)
                atlas.run(lcompute=lcompute)
        else:
            for atlas in self.atlaslist:
                if atlas.case in cases:
                    if subcases is None:
                        logger.debug(atlas.name)
                        atlas.run(lcompute=lcompute)
                    else:
                        if atlas.subcase in subcases[atlas.case]:
                            logger.debug(atlas.name)
                            atlas.run(lcompute=lcompute)


    def topdf(self,lverbose=True):

        if not(os.path.exists(self.pdf_dir)):
            os.makedirs(self.pdf_dir)

        for atlas in self.atlaslist:
            logger.debug(atlas.name)
            atlas.topdf()
            pdflink = '{0}/{1}'.format(self.pdf_dir,atlas.pdfname)
            if os.path.exists(pdflink):
                os.remove(pdflink)
            os.system('ln -s {0}/{1} {2}/{1}'.format(atlas.pdf_dir,atlas.pdfname,self.pdf_dir))

    def tohtml(self):

        if not(os.path.exists(self.html_dir)):
            os.makedirs(self.html_dir)

        for atlas in self.atlaslist:
            atlas.tohtml(index='{0}/index.html'.format(self.html_dir))

        width_per_group = 150

        
        f = open('{0}/index.html'.format(self.html_dir),'w')
        f.write('<head><title>SCM Atlas</title></head>\n')
        f.write('<h1 style="text-align: center;">SCM Atlas</h1>\n')
        f.write('<h2><span style="text-decoration: underline;"><strong>Evaluated configurations</strong></span></h2>\n')
        f.write('<ul>\n')
        for modname in self.models.keys():
            f.write('<table style="border-collapse: collapse; height: 18px;" border="0"><tbody>\n')
            f.write('<tr style="height: 18px;">')
            f.write('<td style="width: 150; height: 18px;" align="left"><strong>{0}:</strong></td>\n'.format(modname))
            f.write('<td style="width: 250; height: 18px;" align="left">Code version: <strong>{0}</strong></td>\n'.format(self.models[modname].binVersion))
            f.write('<td style="width: 150; height: 18px;" align="left">time-step: <strong>{0}s</strong></td>\n'.format(self.models[modname].tstep))
            f.write('<td style="width: 250; height: 18px;" align="left">Vertical discretization: <strong>{0}</strong></td>\n'.format(self.models[modname].levgrid))
            f.write('<td style="width: 100; height: 18px;" align="left"><a href="file://{0}">ATM namelist</a></td>\n'.format(self.models[modname].namATM))
            f.write('<td style="width: 100; height: 18px;" align="left"><a href="file://{0}">SFX namelist</a></td>\n'.format(self.models[modname].namSFX))
            f.write('</tr>\n')
            f.write('</tbody></table>\n')
        f.write('</ul>\n')
        f.write('<h2><span style="text-decoration: underline;"><strong>Diagnostics</strong></span></h2>\n')


        for i,atlas in enumerate(self.atlaslist):

            f.write('<table style="border-collapse: collapse; height: 18px;" border="0"><tbody>\n')
            f.write('<tr style="height: 18px;">')
            f.write('<td style="width: 150; height: 18px;" align="left"><strong>{0}/{1}</strong></td>\n'.format(atlas.case,atlas.subcase))
            for group in atlas.grouplist:
                #f.write('<td style="width: {0}; height: 18px;" align="center"><a href="file://{1}/{2}.html">{3}</a></td>\n'.format(
                #    width_per_group,atlas.html_dir,group.name,group.head,))                
                f.write('<td style="width: {0}; height: 18px;" align="center"><a href="../{1}/{2}/html/{3}.html">{4}</a></td>\n'.format(
                    width_per_group,atlas.case,atlas.subcase,group.name,group.head))

            f.write('</tr>\n')
            f.write('</tbody></table>\n')
            if i < len(self.atlaslist)-1:
                case = atlas.case
                if not(case == self.atlaslist[i+1].case):
                    f.write('<hr>')
                


        f.close()            

