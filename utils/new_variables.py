#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import logging
logger = logging.getLogger(__name__)

import numpy as np
import xarray as xr

import constants as cc

encoding = {'dtype': 'float32', '_FillValue': np.float32(cc.missing)}

def f_zcb(zf,zneb):

    nt,nlev = zneb.shape

    zcb = np.zeros(nt,dtype=np.float32) + cc.missing
    if len(zf.shape) == 1:
        zf = np.tile(zf.data,(nt,1))

    if zf[0,0] > zf[0,1]:
        lpos = False
    else:
        lpos = True

    for it in range(0,nt):
      lfound = False
      ilev = nlev-1
      if lpos: ilev = 0
      while not(lfound) and not(ilev == -1) and not(ilev == nlev):
        if zneb[it,ilev] >= 0.001:
            lfound = True
            zcb[it] = zf[it,ilev]
        else:
            if lpos: # zf is in increasing order
                ilev = ilev + 1
            else:    # zf is in decreasing order
                ilev = ilev - 1

    zcb = xr.DataArray(zcb, coords=[zneb.time,])
    zcb.encoding = encoding
    zcb.attrs["missing_value"] = np.float32(cc.missing)
    zcb.attrs["long_name"] = 'Cloud base height'
    zcb.attrs["units"] = 'm'

    return zcb

def f_zct(zf,zneb):

    nt,nlev = zneb.shape

    zct = np.zeros(nt,dtype=np.float32) + cc.missing
    if len(zf.shape) == 1:
        zf = np.tile(zf.data,(nt,1))

    if zf[0,0] > zf[0,1]:
        lpos = False
    else:
        lpos = True

    for it in range(0,nt):
      lfound = False
      ilev = 0
      if lpos: ilev = nlev-1
      while not(lfound) and not(ilev == -1) and not(ilev == nlev):
        if zneb[it,ilev] >= 0.001:
            lfound = True
            zct[it] = zf[it,ilev]
        else:
            if lpos: # zf is in increasing order
                ilev = ilev - 1
            else:    # zf is in decreasing order
                ilev = ilev + 1

    zct = xr.DataArray(zct, coords=[zneb.time,])
    zct.encoding = encoding
    zct.attrs["missing_value"] = np.float32(cc.missing)
    zct.attrs["long_name"] = 'Cloud top height'
    zct.attrs["units"] = 'm'

    return zct

def f_int(ph,var2int):

    nt,nlev = var2int.shape
    zout = np.zeros(nt,dtype=np.float)

    if len(ph.shape) == 1:
        ph = np.tile(ph.data,(nt,1))

    if ph[0,0] < ph[0,1]:
        lpos = 1
    else:
        lpos = -1
    for ilev in range(0,nlev):
        dp = (ph[:,ilev+1]-ph[:,ilev])*lpos
        zout[:] = zout[:] + var2int[:,ilev]*dp/cc.g

    zout = xr.DataArray(zout, coords=[var2int.time,])
    zout.encoding = encoding
    zout.attrs["missing_value"] = np.float32(cc.missing)
    zout.attrs["long_name"] = 'Vertically-integrated {0}'.format(var2int.attrs['long_name'])
    zout.attrs["units"] = var2int.attrs['units']

    return zout

def f_avg(zf, var2avg, zmin, zmax):

    nt,nlev = var2avg.shape

    zout = np.zeros(nt,dtype=np.float)
    ztot = np.zeros(nt,dtype=np.float)

    if len(zf.shape) == 1:
        zf = np.tile(zf.data,(nt,1))

    if zf[0,0] < zf[0,1]:

        zup = np.zeros((nt,nlev),dtype=np.float)
        zdn = np.zeros((nt,nlev),dtype=np.float)

        zup[:,nlev-1] = 1.e20
        zdn[:,0] = 0

        zup[:,0:nlev-1] = (zf[:,0:nlev-1]+zf[:,1:nlev])/2.
        zdn[:,1:nlev] = (zf[:,0:nlev-1]+zf[:,1:nlev])/2.

        dz = np.zeros((nt,nlev),dtypecode=np.float)
        dz = np.where((zdn <= zmin) & (zup > zmin), zup-zmin, dz)
        dz = np.where((zdn < zmax)  & (zup >= zmax), zmax - zdn, dz)
        dz = np.where((zdn >= zmin) & (zup <= zmax), zup - zdn, dz)

        zout = np.sum(var2avg*dz,axis=1)
        ztot = np.sum(dz,axis=1)

    else:

        zup = np.zeros((nt,nlev),dtype=np.float32)
        zdn = np.zeros((nt,nlev),dtype=np.float32)

        zup[:,0] = 1.e20
        zdn[:,nlev-1] = 0

        zup[:,1:nlev] = (zf[:,0:nlev-1]+zf[:,1:nlev])/2.
        zdn[:,0:nlev-1] = (zf[:,0:nlev-1]+zf[:,1:nlev])/2.

        dz = np.zeros((nt,nlev),dtype=np.float32)
        dz = np.where((zdn <= zmin) & (zup > zmin), zup-zmin, dz)
        dz = np.where((zdn < zmax)  & (zup >= zmax), zmax - zdn, dz)
        dz = np.where((zdn >= zmin) & (zup <= zmax), zup - zdn, dz)

        zout = np.sum(var2avg*dz,axis=1)
        ztot = np.sum(dz,axis=1)

    zout[:] = zout[:]/ztot[:]

    zout = xr.DataArray(zout, coords=[var2avg.time,])
    zout.encoding = encoding
    zout.attrs["missing_value"] = np.float32(cc.missing)
    zout.attrs["long_name"] = '{0} averaged between {1}m and {2}m'.format(var2int.attrs['long_name'], zmin, zmax)
    zout.attrs["units"] = var2int.attrs['units']

    return zout

def add_ql_to_dataset(ds):
    """
    Compute ql=ql+qlc in case of PCMT. If no ql or no qlc, raise exception.
    """

    try:
        ds['ql'] = ds.ql + ds.qlc
        ds['ql'].attrs['long_name'] = 'Liquid water content'
        ds['ql'].attrs['units'] = 'kg kg-1'
    except AttributeError as e:
        logger.debug('Error in computing ql=ql+qlc:' + str(e))
        logger.debug('Most probably, either ql or qlc does not exist in the dataset (specific to PCMT)')
        logger.debug('Thus just raise exception (AttributeError)')
        raise
    except:
        raise    

def add_qr_to_dataset(ds):
    """
    Compute qr=qr+qrc in case of PCMT. If no qr or no qrc, raise exception.
    """

    try:
        ds['qr'] = ds.qr + ds.qrc
        ds['qr'].attrs['long_name'] = 'Rain water content'
        ds['qr'].attrs['units'] = 'kg kg-1'
    except AttributeError as e:
        logger.debug('Error in computing qr=qr+qrc:' + str(e))
        logger.debug('Most probably, either qr or qrc does not exist in the dataset (specific to PCMT)')
        logger.debug('Thus just raise exception (AttributeError)')
        raise
    except:
        raise  

def get_ql(ds):
    """
    Get ql in dataset ds
    """

    try:
        tmp = ds.ql+ds.qlc
        tmp.attrs['long_name'] = 'Liquid water content'
        tmp.attrs['units'] = 'kg kg-1'
    except AttributeError as e:
        logger.debug('Error in computing ql=ql+qlc:' + str(e))
        logger.debug('Most probably, either ql or qlc does not exist in the dataset (specific to PCMT)')
        logger.debug('Try to get ql')
        try:
            tmp = ds.ql
            logger.debug('Dataset has ql. We can continue!')
        except AttributeError as e:
            logger.debug('Dataset has no ql: ' + str(e))
            logger.debug('Just raise exception (AttributeError)')
            raise
        except:
            raise
        pass            
    except:
        raise

    return tmp

def get_qr(ds):
    """
    Get qr in dataset ds
    """

    try:
        tmp = ds.qr+ds.qrc
        tmp.attrs['long_name'] = 'Rain water content'
        tmp.attrs['units'] = 'kg kg-1'
    except AttributeError as e:
        logger.debug('Error in computing qr=qr+qrc:' + str(e))
        logger.debug('Most probably, either qr or qrc does not exist in the dataset (specific to PCMT)')
        logger.debug('Try to get qr')
        try:
            tmp = ds.qr
            logger.debug('Dataset has qr. We can continue!')
        except AttributeError as e:
            logger.debug('Dataset has no qr: ' + str(e))
            logger.debug('Just raise exception (AttributeError)')
            raise
        except:
            raise
        pass            
    except:
        raise

    return tmp


def compute(filein, fileout, var):

    with xr.open_dataset(filein) as ds:
        logger.debug('Computing ' + var + ' in ' + filein)

        if var == 'zcb':
            ds['zcb'] = f_zcb(ds.zf, ds.rneb)
        elif var == 'zct':
            ds['zct'] = f_zct(ds.zf, ds.rneb)
        elif var == 'ql':
            add_ql_to_dataset(ds)
        elif var == 'qr':
            add_qr_to_dataset(ds)
        elif var == 'lwp':
            tmp = get_ql(ds)
            ds['lwp'] = f_int(ds.zh, tmp)
            ds['lwp'].attrs['long_name'] = 'Liquid water path'
            ds['lwp'].attrs['units'] = 'kg m-2'
        elif var == 'rwp':
            tmp = get_qr(ds)
            ds['rwp'] = f_int(ds.zh, tmp)
            ds['rwp'].attrs['long_name'] = 'Rain water path'
            ds['rwp'].attrs['units'] = 'kg m-2'
        elif var == 'theta_0_500':
            ds[var] = f_avg(ds.zf,ds.theta,0,500)
            ds[var].attrs['long_name'] = 'Potential temperature averaged over 0-500m'
            ds[var].attrs['units'] = 'K'
        elif var == 'qv_0_500':
            ds[var] = f_avg(ds.zf,ds.qv,0,500)
            ds[var].attrs['long_name'] = 'Specific humidity averaged over 0-500m'
            ds[var].attrs['units'] = 'kg kg-1'
        elif var == 'theta_2000_5000':
            ds[var] = f_avg(ds.zf,ds.theta,2000,5000)
            ds[var].attrs['long_name'] = 'Potential temperature averaged over 2000-5000m'
            ds[var].attrs['units'] = 'K'
        elif var == 'qv_2000_5000':
            ds[var] = f_avg(ds.zf,ds.qv,2000,5000)
            ds[var].attrs['long_name'] = 'Specific humidity averaged over 2000-5000m'
            ds[var].attrs['units'] = 'kg kg-1'
        elif var == 'max_cf':
            ds[var] = ds.rneb.max(axis=1)
            ds[var].attrs['long_name'] = 'Maximum cloud fraction'
            ds[var].attrs['units'] = '-'
        elif var == 'Qr_int':
            ds[var] = ds.rsus - ds.rsds + ds.rlus - ds.rlds + ds.rsdt - ds.rsut - ds.rlut
            ds[var].attrs['long_name'] = 'Integrated radiative heating'
            ds[var].attrs['units'] = 'W m-2'
        elif var == 'TOA_cre_sw':
            ds[var] = d.rsutcs - ds.rsut
            ds[var].attrs['long_name'] = 'TOA SW CRE'
            ds[var].attrs['units'] = 'W m-2'
        elif var == 'TOA_cre_lw':
            ds[var] = ds.rlutcs - ds.rlut
            ds[var].attrs['long_name'] = 'TOA LW CRE'
            ds[var].attrs['units'] = 'W m-2'
        elif var == 'Qr_int_cre':
            zqr = ds.rsus - ds.rsds + ds.rlus - ds.rlds + ds.rsdt - ds.rsut - ds.rlut
            zqrcs = ds.rsuscs - ds.rsdscs + ds.rlus - ds.rldscs + ds.rsdt - ds.rsutcs - ds.rlutcs
            ds[var] = zqr-zqrcs
            ds[var].attrs['long_name'] = 'Atmospheric CRE'
            ds[var].attrs['units'] = 'W m-2'
        else:
            logger.error('variable to be computed is unknown:', var)
            raise NotImplementedError

        ds[var].encoding = encoding
        ds[var].attrs["missing_value"] = np.float32(cc.missing)

        ds.to_netcdf(fileout)

