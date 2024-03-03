var2compute = ['zcb','zct','ql','qi','qc','qr','qsn','qp','lwp','iwp','rwp','swp','gwp','qt','thetal','windspeed']

variables_info = {
        # 2D Variables
        'ua':       {'name': 'Zonal wind',                         'units': 'm s$^{-1}$',           'coef': 1.},
        'va':       {'name': 'Meridional wind',                    'units': 'm s$^{-1}$',           'coef': 1.},
        'windspeed':{'name': 'Horizontal wind speed',              'units': 'm s$^{-1}$',           'coef': 1.},
        'theta':    {'name': 'Potential temperature',              'units': 'K',                    'coef': 1.},
        'thetal':   {'name': 'Liquid-Water Potential Temperature', 'units': 'K',            'coef': 1.},
        'ta':       {'name': 'Temperture',                         'units': 'K',                    'coef': 1.},
        'qv':       {'name': 'Specific humidity',                  'units': 'g kg$^{-1}$',          'coef': 1000.},
        'hur':      {'name': 'Relative humidity',                  'units': '%',                    'coef': 100.},
        'cl':       {'name': 'Cloud fraction',                     'units': '%',                    'coef': 100.},
        'ql':       {'name': 'Liquid Water Content',               'units': 'mg kg$^{-1}$',         'coef': 1.e6},
        'qi':       {'name': 'Ice Water Content',                  'units': 'mg kg$^{-1}$',         'coef': 1.e6},
        'qc':       {'name': 'Condensed Water Content',            'units': 'mg kg$^{-1}$',         'coef': 1.e6},        
        'qr':       {'name': 'Rain Water Content',                 'units': 'mg kg$^{-1}$',         'coef': 1.e6},
        'qsn':      {'name': 'Snow Water Content',                 'units': 'mg kg$^{-1}$',         'coef': 1.e6},
        'qg':       {'name': 'Graupel Water Content',              'units': 'mg kg$^{-1}$',         'coef': 1.e6},
        'qp':       {'name': 'Precipitating Water Content',        'units': 'mg kg$^{-1}$',         'coef': 1.e6},        
        'qt':       {'name': 'Total Water Content',                'units': 'g kg$^{-1}$',        'coef': 1000.},
        'tke':      {'name': 'Turbulent kinetic energy',           'units': 'm$^2$ s$^{-2}$',       'coef': 1.},
        'wa_up':    {'name': 'Updraft vertical velocity',          'units': 'm s$^{-1}$',           'coef': 1.},
        'alpha_up': {'name': 'Updraft area fraction',              'units': '%',                    'coef': 100.},
        'mf_up':    {'name': 'Updraft mass flux',                  'units': 'kg m$^{-2}$ s$^{-1}$', 'coef': 1.},
        'dTv_up':   {'name': 'Updraft dTv',                        'units': 'K',                    'coef': 1.},
        'b_up':     {'name': 'Updraft buoyancy',                   'units': 'm s$^{-2}$',           'coef': 1.},
        'ent_up':   {'name': 'Updraft entrainment',                'units': 'km$^{-1}$',            'coef': 1000.},
        'det_up':   {'name': 'Updraft detrainment',                'units': 'km$^{-1}$',            'coef': 1000.},
        # 1D Variables
        'hfss':     {'name': 'Sensible heat flux',                 'units': 'W m$^{-2}$',           'coef': 1.},
        'hfls':     {'name': 'Latent heat flux',                   'units': 'W m$^{-2}$',           'coef': 1.},
        'hflsn':    {'name': 'Latent heat flux over snow',         'units': 'W m$^{-2}$',           'coef': 1.},
        'ustar':    {'name': 'Surface friction velocity',          'units': 'm s$^{-1}$',           'coef': 1.},
        'ts':       {'name': 'Surface temperature',                'units': 'K',                    'coef': 1.},
        'pr':       {'name': 'Surface precipitation',              'units': 'mm day$^{-1}$',        'coef': 86400.},
        'clt':      {'name': 'Total cloud fraction',               'units': '%',                    'coef': 100.},
        'zcb':      {'name': 'Cloud base height',                  'units': 'm',                    'coef': 1.},
        'zct':      {'name': 'Cloud top height',                   'units': 'm',                    'coef': 1.},
        'prw':      {'name': 'Precipitable water',                 'units': 'kg m$^{{-2}}$',        'coef': 1.},
        'lwp':      {'name': 'Liquid water path',                  'units': 'g m$^{{-2}}$',         'coef': 1000.},
        'iwp':      {'name': 'Ice water path',                     'units': 'g m$^{{-2}}$',         'coef': 1000.},
        'rwp':      {'name': 'Rain path',                          'units': 'g m$^{{-2}}$',         'coef': 1000.},
        'swp':      {'name': 'Snow path',                          'units': 'g m$^{{-2}}$',         'coef': 1000.},
        'gwp':      {'name': 'Graupel path',                       'units': 'g m$^{{-2}}$',         'coef': 1000.},        
}
