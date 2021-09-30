#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import logging
logger = logging.getLogger(__name__)

from collections import OrderedDict

import math
import numpy as np
import numpy.ma as ma
import xarray as xr

from datetime import datetime, timedelta
import cftime

import atlas1d
import atlas1d.plotutils as plotutils
import atlas1d.constants as cc

def plot_timeseries(filein,varname,coef=None,units='',tmin=None,tmax=None,dtlabel='1h',error=None,**kwargs):
    """
       Do a timeseries plot of varname for several MUSC files
    """

    data = OrderedDict()
    time = {}
    if coef is None:
        coef = {k: 1. for k in filein.keys()}

    for k in filein.keys():
        with xr.open_dataset(filein[k], use_cftime=True) as ds:
            try:
                data[k] = np.squeeze(ds[varname[k]].data)*coef[k]
                data[k] = np.ma.masked_where(data[k] == cc.missing, data[k])
                time[k] = ds[varname[k]].time.data
                kref = k
            except KeyError as e:
                data[k] = None  
                time[k] = None
                logger.debug('Variable {2} probably unknown in dataset {0} (file={1})'.format(k,filein[k],varname[k]))
                logger.debug('Raised error: KeyError')
                if error is not None:
                    if isinstance(error,dict):
                        if k in error:
                            error[k].append(varname[k])
                        else:
                            error[k] = [varname[k],]
                    else:
                        logger.error('type of error unexpected:', type(error))
                        logger.error('error should be a dictionnary')
                        raise ValueError
            except:
                raise

    for k in filein.keys():
        if data[k] is None:
            del(data[k])
            del(time[k])

    try:
        timeref = time[kref]
        tunits = timeref[0].strftime("hours since %Y-%m-%d %H:%M:0.0")

        if tmin is None:
            tmin = timeref[0]
        logger.debug('tmin = ' + tmin.isoformat())
    
        if tmax is None:
            tmax = timeref[-1]
        logger.debug('tmax = ' + tmax.isoformat())

        tlabels = get_time_labels(tmin, tmax, tunits, dtlabel)

        tmin_rel = cftime.date2num(tmin, tunits)
        tmax_rel = cftime.date2num(tmax, tunits)

        for k in data.keys():
            time[k] = cftime.date2num(time[k], tunits)

        plotutils.plot1D(time, data,\
                xmin=tmin_rel, xmax=tmax_rel,\
                xlabels=tlabels,\
                **kwargs)

    except UnboundLocalError as e:
        logger.info('No data for variable {0}'.format(varname[k]))
        pass
    except:
        raise


def plot_profile(filein,varname,lines=None,coef=None,units='',lev=None,levunits='km',tt=None,tmin=None,tmax=None,init=False,t0=False,lbias=False,refdataset=None,error=None,**kwargs):
    """
       Do a profile plot of varname for several MUSC files
    """

    data = OrderedDict()
    level = {}
    if coef is None:
        coef = {k: 1. for k in filein.keys()}
    
    if lev is None:
        lev = {k: 'zf' for k in filein.keys()}
    if isinstance(lev,str):
      lev = {k: lev for k in filein.keys()}

    for i,k in enumerate(filein.keys()):
        with xr.open_dataset(filein[k], use_cftime=True) as ds:

            try:
                time = ds[varname[k]].time.data
                if tmin is not None and tmax is not None:

                    data[k] = np.average(ds[varname[k]].sel(time=slice(tmin,tmax)).data,axis=0)*coef[k]
                    level[k] = get_level(ds, lev[k], nlev=data[k].shape[0])

                    if len(level[k].shape) == 2:
                        level[k] = np.average(level[k].sel(time=slice(tmin,tmax)).data,axis=0)

                elif t0:

                    data[k] = ds[varname[k]].data[0,:]*coef[k]
                    level[k] = get_level(ds, lev[k], nlev=data[k].shape[0])

                    if len(level[k].shape) == 2:
                        level[k] = level[k].data[0,:]

                elif tt is not None:

                    if tmin is None:
                        tmin = time[0]
                    if tmax is None:
                        tmax = time[-1]

                    logger.debug('tmin = ' + tmin.isoformat())
                    logger.debug('tmax = ' + tmax.isoformat())

                    if isinstance(tt,int):
                        tt = time[tt]
                    else:
                        if tt < tmin:
                            logger.info('tt={0} is lower than tmin={1}'.format(tt.isoformat(),tmin.isoformat()))
                        if tt > tmax:
                            logger.info('tt={0} is greatet than tmax={1}'.format(tt.isoformat(),tmax.isoformat()))

                    logger.debug('dataset = ' + k)
                    logger.debug('tt = ' + tt.isoformat())

                    data[k] = ds[varname[k]].sel(time=tt, method='nearest').data*coef[k]
                    level[k] = get_level(ds, lev[k], nlev=data[k].shape[0])

                    if len(level[k].shape) == 2:
                        level[k] = level[k].sel(time=tt, method='nearest').data

                else:
                    logger.error('Case unexpected : tmin, tmax and tt are None and t0 is False')
                    raise ValueError
                    
                kref = k

            except (KeyError, AttributeError) as e:
                data[k] = None
                level[k] = None   
                logger.debug('Variable {2} probably unknown in dataset {0} (file={1})'.format(k,filein[k],varname[k]))
                logger.debug('Raised error: {0}'.format(e))
                if error is not None:
                    if isinstance(error,dict):
                        if k in error:
                            error[k].append(varname[k])
                        else:
                            error[k] = [varname[k],]
                    else:
                        logger.error('type of error unexpected:', type(error))
                        logger.error('error should be a dictionnary')
                        raise ValueError
            except:
                raise


    for i,k in enumerate(filein.keys()):

        if data[k] is None:
            del(data[k])
            del(level[k])
        else:
            level[k] = update_level(level[k], lev[k], levunits)

    if init: # Adding initial profiles on plot
        with xr.open_dataset(filein[kref]) as ds:
            data['init'] = ds[varname[kref]].data[0,:]*coef[k]
            tmp = get_level(ds, lev[kref], nlev=data['init'].shape[0])
            if len(tmp.shape) == 2:
                level['init'] = tmp[0,:]
            elif len(tmp.shape) == 1:
                level['init'] = tmp[:]
            else:
                logger.error('level shape unexpected:', tmp.shape)
                raise ValueError

        level['init'] = update_level(level['init'], lev[kref], levunits)

        if lines is None:
            lines = {}
        lines['init'] = 'k--'



    if lbias:
        if refdataset is None:
            logger.error('please provide reference dataset (keyword refdataset) to compute bias)')
            raise ValueError
        else: 
            for k in data.keys():
                if not(k == refdataset):
                    data[k] = data[k]-data[refdataset]
            data[refdataset] = data[refdataset]*0.

    plotutils.plot1D(data,level,lines=lines,**kwargs)


def plot2D(filein,varname,coef=None,units='',lev=None,levunits=None,tmin=None,tmax=None,dtlabel='1h',namefig=None,lbias=False,refdataset=None,error=None,**kwargs):
    """
       Do a 2D plot of varname for several MUSC file
    """

    title0 = kwargs['title']

    data = OrderedDict()
    levax = {}
    time = {}
    timeax = {}

    if coef is None:
        coef = {k: 1. for k in filein.keys()}
    elif isinstance(coef,int) or isinstance(coef,float):
        coef = {k: coef for k in filein.keys()}
    
    if lev is None:
        lev = {k: 'zh' for k in filein.keys()}
        levunits = {k: 'km' for k in filein.keys()}
    elif isinstance(lev,str):
        lev = {k: lev for k in filein.keys()}

    if levunits is None:
        levunits = {}
        for k in filein.keys():
            if lev[k] == 'zh':
                levunits[k] = 'km'
            elif lev[k] in['ph','pf']:
                levunits[k] = 'hPa'
            else:
                logger.error('lev={} not coded yet'.format(lev[k]))
                raise NotImplementedError
    elif isinstance(levunits,str):
        levunits = {k: levunits for k in filein.keys()}

    datasets = filein.keys()
    if lbias:
        if refdataset is None:
            logger.error('please provide reference dataset (keyword refdataset) to compute bias)')
            raise ValueError
        else: 
            with xr.open_dataset(filein[refdataset]) as ds:
                dataref = ds[varname[refdataset]].data*coef[refdataset]
            datasets.remove(refdataset)

    for k in datasets:
        with xr.open_dataset(filein[k], use_cftime=True) as ds:
            try:
                data = ds[varname[k]].data*coef[k]
                if lbias:
                    nt,_ = data.shape
                    data = data-dataref[0:nt,:]

                time = ds[varname[k]].time.data
                tunits = time[0].strftime("hours since %Y-%m-%d %H:%M:0.0")

                if tmin is None:
                    tmin = time[0]
                logger.debug('tmin = ' + tmin.isoformat())
      
                if tmax is None:
                    tmax = time[-1]
                logger.debug('tmax = ' + tmax.isoformat())

                tlabels = get_time_labels(tmin, tmax, tunits, dtlabel)

                tmin_rel = cftime.date2num(tmin, tunits)
                tmax_rel = cftime.date2num(tmax, tunits)

                time = cftime.date2num(time, tunits)
                    
      
                try:
                    levax = ds[lev[k]].data
                except:
                    if lev[k] == 'zh':
                        levax = ds.zf.data
                    if lev[k] == 'ph':
                        levax = ds.pf.data         

                levax = update_level(levax, lev[k], levunits[k])
      
                if len(levax.shape) == 2:
                    nt,nlev = levax.shape
                    timeax = np.tile(time[:],(nlev,1))
                    X = timeax
                    Y = np.transpose(levax)
                else:
                    nlev, = levax.shape
                    nt, = time.shape
                    timeax = np.tile(time[:],(nlev,1))
                    levax = np.tile(levax,(nt,1))
                    X = np.array(timeax[:])
                    Y = np.transpose(levax[:])

                if isinstance(namefig,str):
                    tmp = k + '_' + namefig
                elif isinstance(namefig,dict):
                    tmp = namefig[k]
                elif namefig is None:
                    tmp = None
                else:
                    logger.error('namefig type unexpected:', namefig)
                    raise ValueError

                kwargs['title'] = '{0} - {1}'.format(title0,k)

                plotutils.plot2D(X,Y,ma.transpose(data),\
                    xmin=tmin_rel, xmax=tmax_rel,\
                    xlabels=tlabels,\
                    namefig=tmp,\
                    **kwargs)

            except (KeyError, AttributeError) as e:
                logger.debug('Variable {2} probably unknown in dataset {0} (file={1})'.format(k,filein[k],varname[k]))
                logger.debug('Raised error: ' + str(e))
                if error is not None:
                    if isinstance(error,dict):
                        if k in error:
                            error[k].append(varname[k])
                        else:
                            error[k] = [varname[k],]
                    else:
                        logger.error('type of error unexpected:', type(error))
                        logger.error('error should be a dictionnary')
                        raise ValueError
            except:
                raise

def get_time_labels(tmin, tmax, tunits, dtlabel):

    tt = []
    tlabels = []

    if dtlabel == '1h':

        tmin0 = datetime(tmin.year,tmin.month,tmin.day,tmin.hour)
        t0 = tmin0 + timedelta(hours=0)
        while t0 <= tmax:
            if t0 >= tmin: 
                tt.append(cftime.date2num(t0, tunits))
                tlabels.append('{0}'.format(t0.hour))
            t0 = t0 + timedelta(hours=1)

    elif dtlabel == '2h':

        tmin0 = datetime(tmin.year,tmin.month,tmin.day,tmin.hour)
        t0 = tmin0 + timedelta(hours=0)
        while t0 <= tmax:
            if t0 >= tmin: 
                tt.append(cftime.date2num(t0, tunits))
                tlabels.append('{0}'.format(t0.hour))
            t0 = t0 + timedelta(hours=2)

    elif dtlabel == '6h':

        tmin0 = datetime(tmin.year,tmin.month,tmin.day,tmin.hour)
        t0 = tmin0 + timedelta(hours=0)
        while t0 <= tmax:
            if t0 >= tmin: 
                tt.append(cftime.date2num(t0, tunits))
                tlabels.append('{0}'.format(t0.hour))
            t0 = t0 + timedelta(hours=6)
        
    elif dtlabel == '10d':

        tmin0 = datetime(tmin.year,tmin.month,tmin.day,tmin.hour)
        t0 = tmin0 + timedelta(hours=0)
        while t0 <= tmax:
            if t0 >= tmin:
                tt.append(cftime.date2num(t0, tunits))
                tlabels.append('{0}/{1}'.format(t0.month,t0.day))
            if t0.day == 1:
                t0 = cftime.datetime(t0.year,t0.month,10,0)
            elif t0.day == 10:
                t0 = cftime.datetime(t0.year,t0.month,20,0)
            elif t0.day == 20:
                if t0.month == 12:
                    t0 = cftime.datetime(t0.year+1,1,1,0)
                else:
                    t0 = cftime.datetime(t0.year,t0.month+1,1,0)
            else:
                t0 = t0 + timedelta(days=10)

    else:

        logger.error('dtlabel={} not coded yet'.format(dtlabel))
        raise NotImplementedError

    return tt, tlabels

def get_level(ds, lev, nlev=None):

    if lev == 'zf':
        level = ds[lev]
    elif lev == 'zh':
        try:
            level = ds[lev]
        except:
            try:
                level = ds['zf']
            except:
                raise
    elif lev == 'pf':
        level = ds[lev]
    elif lev == 'ph':
        try:
            level = ds[lev]
        except:
            try:
                level = ds['pf']
            except:
                raise
    else:
        logger.error('Level unexpected: {0}'.forma(lev))
        raise NotImplementedError

    if nlev is not None:
        if len(level.shape) == 2:
            _, nlev_loc = level.shape
        else:
            nlev_loc, = level.shape

        if nlev != nlev_loc:
            if lev == 'zf':
                level = ds['zh']
            elif lev == 'zh':
                level = ds['zf']
            elif lev == 'pf':
                level = ds['ph']
            elif lev == 'ph':
                level = ds['pf']

    return level

def update_level(level, levname, levunits):

    if levname in ['zf','zh']:
        if levunits == 'm':
            levelloc = level
        elif levunits == 'km':
            levelloc = level/1000.
        else:
            logger.error('levunits={0} for levname={1} not coded yet'.format(levunits,levname))
            raise NotImplementedError
    elif levname in ['pf','ph']:
        if levunits == 'Pa':
            levelloc = level
        elif levunits == 'hPa':
            levelloc = level/100.
        else:
            logger.error('levunits={} for levname={1} not coded yet'.format(levunits,levname))
            raise NotImplementedError
    else:
        logger.error('levname={} not coded yet'.format(levname))
        raise NotImplementedError

    return levelloc

