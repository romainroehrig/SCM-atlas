#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

import logging
logger = logging.getLogger(__name__)

from collections import OrderedDict

import atlas1d
from atlas1d.DiagGroup import DiagGroup

class Atlas:

    def __init__(self,name,references={},simulations={},root_dir=atlas1d._default_dirout):

        # Name of the atlas
        self.name = name

        if references == {} and simulations == {}:
            logger.error('you must give at least one reference or one simulation')
            raise ValueError

        # Reference datasets
        self.references = references

        # Simulation datasets
        self.simulations = simulations

        # datasets = union(references,simulations
        self.datasets = []
        for ref in self.references:
            self.datasets.append(ref)
        for sim in self.simulations:
            self.datasets.append(sim)

        # Case and subcase of the atlas
        dat0 = self.datasets[0]
        self.case = dat0.case
        self.subcase = dat0.subcase

        # List of diagnostic groups
        self.grouplist = []

        # Directory where to store atlas outputs
        if root_dir[0] == '/':
            self.atlas_dir = '{0}/{1}'.format(root_dir,self.name)
        else:
            logger.error('root directory is expected to be given with an absolute path. root_dir=', root_dir)
            raise ValueError

        if not(os.path.exists(self.atlas_dir)):
            os.makedirs(self.atlas_dir)

        # Directory for diagnostics output
        #self.diag_dir = '{0}/{1}/{2}'.format(self.atlas_dir,self.case,self.subcase)
        self.diag_dir = self.atlas_dir

        if not(os.path.exists(self.diag_dir)):
            os.makedirs(self.diag_dir)

        # Directory for pdf file output
        self.pdf_dir = self.atlas_dir

        if not(os.path.exists(self.pdf_dir)):
            os.makedirs(self.pdf_dir)

        # pdf filename
        self.pdfname = '{0}_{1}.pdf'.format(self.case,self.subcase)

        # Directory for html file
        self.html_dir = '{0}/html'.format(self.atlas_dir)

        if not(os.path.exists(self.html_dir)):
            os.makedirs(self.html_dir)


    def info(self,groups=False,references=False,simulations=False):
        print('#'*30)
        print('Atlas:', self.name)
        if references:
            print('#'*10, 'References:')
            for ref in self.references:
                ref.info()
        if simulations:
            print('#'*10, 'Simulations:')
            for sim in self.simulations:
                sim.info()
        if groups:
            print('#'*10, 'Groups of diagnostics:')
            for group in self.grouplist:
                group.info()        

    def add_group(self,groupdiag):

        self.grouplist.append(groupdiag)

    def init_from_dict(self,diagnostics):

        for group in diagnostics:
            diagGroup = DiagGroup(group)
            diagGroup.init_from_dict(diagnostics[group])

            self.add_group(diagGroup) 
    
    def printOutput(self):

        print('#'*40)
        print('--- Output for atlas "{0}"'.format(self.name))
        for group in self.grouplist:
            group.printOutput()

    def printError(self):

        print('#'*40)
        print('--- Error for atlas "{0}"'.format(self.name))
        for group in self.grouplist:
            group.printError()

    def is_valid(self):

        dat0 = self.datasets[0]
        case = self.datasets[0].case
        subcase = self.datasets[0].subcase
        for dat in self.datasets:
            if not(dat.case == case) and not(dat.subcase == subcase):
                logger.error('all datasets must be for the same CASE/SUBCASE')
                logger.error('{0} is for {1}/{2}'.format(dat0.name,case,subcase))
                logger.error('{0} is for {1}/{2}'.format(dat.name,dat.case,dat.subcase))
                return False

        return True

    def run(self,printOutput=False,printError=False,lcompute=True):

        if not(self.is_valid()):
            raise ValueError('Atlas not valid')

        for group in self.grouplist:
            if lcompute:
                logger.info('Running diagnostic group {0} for {1} atlas'.format(group.name,self.name))
            else:
                logger.info('Initialize diagnostic group {0} for {1} atlas'.format(group.name,self.name))
            group.run(self.datasets,root_dir=self.diag_dir,lcompute=lcompute)

        # synthesis of output
        if printOutput:
            self.printOutput()
       
        # synthesis of encountered errors
        if printError:
            self.printError()

    def topdf(self,pdfname=None):

        from pylatex import Document, Figure, SubFigure, NoEscape, Command,\
            PageStyle, Head, Foot, NewPage, simple_page_number, Package
        from pylatex.utils import bold

        logger.info('Preparing pdf file for atlas ' + self.name)

        if pdfname is None:
            pdfname = self.pdfname

        logger.info('PDF file is ' + pdfname)

        filename = pdfname[:-4]

        geometry_options = {"margin": "2cm"}
        doc = Document(
                default_filepath=filename,
                geometry_options=geometry_options
                )
        doc.documentclass = Command(
                'documentclass',
                options=['12pt','landscape'],
                arguments=['article'],
                )

        doc.packages.append(Package('fancyhdr'))
        for group in self.grouplist:
            doc.preamble.append(NoEscape(r'\fancypagestyle{{{0}}}{{\fancyhf{{}}\fancyhead[L]{{\textbf{{{1}/{2}}}}}\fancyhead[R]{{{3}}}\fancyfoot[R]{{Page\ \thepage\ of \pageref{{LastPage}}}}}}'.format(group.name.replace('_',''),self.case,self.subcase,group.head)))

        width = 0.25 #min(int(0.9/nplot*100.)/100.,0.25)
        nplot_per_line = 4

        for group in self.grouplist:
            doc.append(NoEscape(r'\pagestyle{{{0}}}'.format(group.name.replace('_',''))))
            all2D = True
            all1D = True
            for diag in group.diaglist:
                all2D = all2D and (diag.diag_type == 'plot2D')
                all1D = all1D and ((diag.diag_type == 'plotTS') or (diag.diag_type == 'plotAvgP') or\
                                   (diag.diag_type == 'plotInitP'))

            if all2D:
                for diag in group.diaglist:
                    header = PageStyle("header")
                    keys = list(diag.output.keys())
                    nplot = len(keys)
                    nlines = nplot//nplot_per_line
                    for i in range(0,nlines+1):
                        with doc.create(Figure(position='h!')) as fig:
                            for j in range(0,nplot_per_line):
                                if i*nplot_per_line+j < nplot:
                                    with doc.create(SubFigure(
                                        position='b',
                                        width=NoEscape(r'{0}\linewidth'.format(width)))
                                        ) as subfig:
                                        subfig.add_image(diag.output[keys[i*nplot_per_line+j]],width=NoEscape(r'\linewidth'))
                    if nlines > 0:
                        doc.append(NoEscape(r'\clearpage'))

            elif all1D:
                nplot = len(group.diaglist)
                nlines = nplot//nplot_per_line
                for i in range(0,nlines+1):
                    with doc.create(Figure(position='h!')) as fig:
                        for j in range(0,nplot_per_line):
                            if i*nplot_per_line+j < nplot:
                                with doc.create(SubFigure(
                                    position='b',
                                    width=NoEscape(r'{0}\linewidth'.format(width)))
                                    ) as subfig:
                                    subfig.add_image(group.diaglist[i*nplot_per_line+j].output,width=NoEscape(r'\linewidth'))

            else:
                logger.error('mixed case not coded yet')
                raise ValueError

            doc.append(NoEscape(r'\clearpage'))

        doc.generate_pdf(clean_tex=True)

        os.system('mv {0}.pdf {1}/'.format(filename,self.pdf_dir))

    def tohtml(self,index=None):

        logger.info('Preparing html interface to atlas ' + self.name)

        if index is None:
            index = '{0}/index.html'.format(self.html_dir)

        width_per_letter = 0.5

        width = 0
        for group in self.grouplist:
            width = width + len(group.head)*width_per_letter

        width = int(width) + 1

        f = open('{0}/index.html'.format(self.html_dir),'w')
        f.write('<head><title>SCM Atlas</title></head>\n')
        f.write('<h1 style="text-align: center;">SCM Atlas</h1>\n')
        f.write('<h2><span style="text-decoration: underline;"><strong>Evaluated configurations</strong></span></h2>\n')
        f.write('<ul>\n')
        for sim in self.simulations:
            f.write('<li>{0}: Code version: {1}</li>\n'.format(sim.name,sim.model.binVersion))
        f.write('</ul>\n')
        f.write('<h2><span style="text-decoration: underline;"><strong>Atlas</strong></span></h2>\n')
        f.write('<table style="border-collapse: collapse; width: {0}%; height: 18px;" border="0"><tbody>\n'.format(width+5))
        f.write('<tr style="height: 18px;">')
        f.write('<td style="width: 5%; height: 18px;"><strong>{0}/{1}</strong></td>\n'.format(self.case,self.subcase))
        for group in self.grouplist:
            #f.write('<td style="width: {0}%; height: 18px;"><a href="file://{1}/{2}.html">{3}</a></td>\n'.format(
            #    int(len(group.head)*width_per_letter),self.html_dir,group.name,group.head,))            
            f.write('<td style="width: {0}%; height: 18px;"><a href="{1}.html">{2}</a></td>\n'.format(
                int(len(group.head)*width_per_letter),group.name,group.head,))
            group.tohtml(root_dir=self.html_dir,index=index)

        f.write('</tr>\n')
        f.write('</tbody></table>\n')


        f.close()



        
