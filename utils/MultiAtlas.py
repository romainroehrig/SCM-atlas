#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os, sys
sys.path = ['../config/',] + sys.path
import importlib

from collections import OrderedDict

from Atlas import Atlas

_dir_home = os.getenv('HOME')
_default_dirout = '{0}/SCM_atlas'.format(_dir_home)

class MultiAtlas:

    def __init__(self,name,simulations={},root_dir=_default_dirout,linfo=False):

        self.name = name

        if simulations == {}:
            print 'ERROR: you must give at least one simulation'
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
            print 'ERROR: root directory is expected to be given with an absolute path. root_dir=', root_dir
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

                if os.path.isfile('config/config_{0}_{1}.py'.format(case,subcase)):
                    config = importlib.import_module('config_{0}_{1}'.format(case,subcase))
                elif os.path.isfile('config/config_{0}.py'.format(case)):
                    config = importlib.import_module('config_{0}'.format(case))
                else:
                    print 'ERROR: Cannot find a config files in ../config/ for case {0}, subcase {1}'.format(case,subcase)
                    raise ValueError

                tmp = Atlas('{0}/{1}'.format(case,subcase),references=config.references,simulations=simulations[case][subcase],root_dir=self.atlas_dir)
                tmp.init_from_dict(config.diagnostics)
                if linfo:
                    tmp.info(references=True,simulations=True,groups=True)

                self.atlaslist.append(tmp)

        # Initialize output if avalaible
        self.run(lcompute=False,lverbose=False)

    def info(self):
        print '### Multi Atlas {0} ###'.format(self.name)
        print 'Multi atlas directory:', self.atlas_dir
        print 'Cases:'
        for c in self.cases:
            print '  {0}: {1}'.format(c,self.subcases[c])
        for a in self.atlaslist:
            a.info(references=True,simulations=True)


    def run(self,cases=None,subcases=None,lcompute=True,lverbose=True):

        if cases is None:
            for atlas in self.atlaslist:
                if lverbose:
                    print atlas.name
                atlas.run(lcompute=lcompute)
        else:
            for atlas in self.atlaslist:
                if atlas.case in cases:
                    if subcases is None:
                        if lverbose:
                            print atlas.name
                        atlas.run(lcompute=lcompute)
                    else:
                        if atlas.subcase in subcases[atlas.case]:
                            if lverbose:
                                print atlas.name
                            atlas.run(lcompute=lcompute)


    def topdf(self,lverbose=True):

        if not(os.path.exists(self.pdf_dir)):
            os.makedirs(self.pdf_dir)

        for atlas in self.atlaslist:
            if lverbose:
                print atlas.name
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
                f.write('<td style="width: {0}; height: 18px;" align="center"><a href="file://{1}/{2}.html">{3}</a></td>\n'.format(
                    width_per_group,atlas.html_dir,group.name,group.head,))

            f.write('</tr>\n')
            f.write('</tbody></table>\n')
            if i < len(self.atlaslist)-1:
                case = atlas.case
                if not(case == self.atlaslist[i+1].case):
                    f.write('<hr>')
                


        f.close()            

