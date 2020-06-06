#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os, sys
sys.path = ['./','../config/'] + sys.path

import json

from Model import save_all as save_all_models 
from Model import load_all as load_all_models 
from Model import get_model

_dir_path = os.path.dirname(os.path.realpath(__file__))
_rep_MUSC = os.getenv('REP_MUSC')

_lines = ['r','b','g']

_known_simulations = {}

class Simulation:

    def __init__(self,name=None,case=None,subcase=None,model=None,
            namATM=None,namSFX=None,
            ncfile=None,comment=None,
            coefs={},varnames={},line=None):

        if name  is None or model   is None or\
           case  is None or subcase is None:
            print 'ERROR: name, model, case andsubcase must be defined'
            raise ValueError

        self.id = '{0}/{1}/{2}/{3}'.format(name,model.id,case,subcase)
        self.name = name
        self.model = model
        self.case = case
        self.subcase = subcase        
        self.namATM = namATM
        self.namSFX = namSFX
        self.comment = comment
        self.coefs = coefs
        self.varnames = varnames

        if ncfile is None:
            tmp = '{0}/simulations/{1}/{2}/{3}_{4}s/{5}/{6}/Output/netcdf/Out_klevel.nc'.format(_rep_MUSC,self.model.binVersion,name,self.model.levgrid,self.model.tstep,case,subcase)
            if os.path.exists(tmp):
                self.ncfile = tmp
            else:
                self.ncfile = None
        else:
            self.ncfile = ncfile

        if namATM is None:
            tmp = '{0}/simulations/{1}/{2}/{3}_{4}s/{5}/{6}/namarp_{2}'.format(_rep_MUSC,self.model.binVersion,name,self.model.levgrid,self.model.tstep,case,subcase)
            if os.path.exists(tmp):
                self.namATM = tmp
            else:
                self.namATM = None
        else:
            self.namATM = namATM

        if namSFX is None:
            tmp = '{0}/simulations/{1}/{2}/{3}_{4}s/{5}/{6}/namsfx_{2}'.format(_rep_MUSC,self.model.binVersion,name,self.model.levgrid,self.model.tstep,case,subcase)
            if os.path.exists(tmp):
                self.namSFX = tmp
            else:
                self.namSFX = None
        else:
            self.namSFX = namSFX

        if self.model.MUSC:
            for var in ['shf','lhf']:
                self.coefs[var] = -1.

        if line is None:
            self.line = _lines.pop()
        else:
            self.line = line

    def is_valid(self):

        return not(self.ncfile is None) and os.path.exists(self.ncfile)

    def info(self):

        self.model.info()
        print '--- Simulation {0} ---'.format(self.name)
        print 'Case simulated: {0}/{1}'.format(self.case,self.subcase)
        print 'ncfile: ', self.ncfile
        print 'Atmospheric namelist:', self.namATM
        print 'SURFEX namelist:', self.namSFX
        print 'Comment:', self.comment
        print 'varnames:', self.varnames
        print 'coefs:', self.coefs
        print "line for plots: '{0}'".format(self.line)

    def add2known(self,overwrite=False):

        if self.id in _known_simulations.keys():
            if overwrite:
                print 'WARNING: Simulation {0} is already known'.format(self.name)
                print 'WARNING: it is overwritten'
                _known_simulations[self.id] = self
            else:
                print 'ERROR: Simulation {0} is already known'.format(self.name)
                print 'You can overwrite it using overwrite argument'
                sys.exit()
        else:
            _known_simulations[self.id] = self

        self.model.add2known()


def print_known_simulations():

    for sim in sorted(_known_simulations.keys()):
        _known_simulations[sim].info()

def save_all(overwrite=False):

    fileout = "{0}/known_simulations.json".format(_dir_path)
    if not(overwrite):
        if os.path.exists(fileout):
            print "ERROR: Can't overwrite existing json file containing known simulations"
            sys.exit()

    save_all_model()

    data2save = {}
    for sim in _known_simulations.keys():
        data2save[sim] = {'name':       _known_simulations[sim].name      ,
                          'model':      _known_simulations[sim].model.name,
                          'case':       _known_simulations[sim].case      ,
                          'subcase':    _known_simulations[sim].subcase   ,                
                          'namATM':     _known_simulations[sim].namATM    ,
                          'namSFX':     _known_simulations[sim].namSFX    ,
                          'comment':    _known_simulations[sim].comment   ,
                          'ncfile':     _known_simulations[sim].ncfile    ,
                          }

    with open(fileout, 'w') as outfile:
        json.dump(data2save, outfile, indent=4, sort_keys=True)

def load_all(overwrite=False):

    load_all_models()

    filein = "{0}/known_simulations.json".format(_dir_path)
    with open(filein) as json_file:
        data = json.load(json_file)
        for name in data.keys():
            print name
            data['model'] = get_model(data[model])
            sim = Simulation(**data[name])
            sim.add2known(overwrite=overwrite)


def discover():

    print 'ERROR: not updated'
    sys.exit()

    binVersions = os.listdir('{0}/simulations/'.format(_rep_MUSC))
    try:
        binVersions.remove('.DS_Store')
    except ValueError:
        pass
    except:
        raise
        
    for binVersion in binVersions:
        names = os.listdir('{0}/simulations/{1}/'.format(_rep_MUSC,binVersion))
        try:
            names.remove('.DS_Store')
        except ValueError:
            pass
        except:
            raise

        for name in names:
            lts = os.listdir('{0}/simulations/{1}/{2}/'.format(_rep_MUSC,binVersion,name))
            try:
                lts.remove('.DS_Store')
            except ValueError:
                pass
            except:
                raise
            
            for lt in lts:
                level,tstep = lt.split('_')
                tstep = int(tstep[:-1])        
                cases = os.listdir('{0}/simulations/{1}/{2}/{3}/'.format(_rep_MUSC,binVersion,name,lt))
                try:
                    cases.remove('.DS_Store')
                except ValueError:
                    pass
                except:
                    raise

                for case in cases:
                    subcases = os.listdir('{0}/simulations/{1}/{2}/{3}/{4}'.format(_rep_MUSC,binVersion,name,lt,case))
                    try:
                        subcases.remove('.DS_Store')
                    except ValueError:
                        pass
                    except:
                        raise
                        
                    for subcase in subcases:
                        sim = Simulation(name=name,
                                case=case,subcase=subcase,
                                binVersion=binVersion,
                                level=level,tstep=tstep)
                        #sim.info()
                        if sim.is_valid():
                            sim.add2known()





