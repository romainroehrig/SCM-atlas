# SCM-atlas - Tools to prepare atlas of SCM simulation

## Prerequisites

* 3.7 or higher
* Python packages numpy, netCDF4 and matplotlib, xarray
* Optional pylatex[https://jeltef.github.io/PyLaTeX/latest/] to prepare atlas pdf files.

## Quick installation
To install SCM-atlas on a CNRM computer, with access to the CNRM Lustre system:
1. Get the installation script: 

   `wget https://raw.githubusercontent.com/romainroehrig/SCM-atlas/master/install.sh`

2. Modify `install.sh`:

   * Set `ATLAS_VERSION`, e.g., `ATLAS_VERSION=1.0`
   * Set where you want to install SCM-atlas tools: default is `DIR_ATLAS=$HOME/Tools/SCM-atlas/V${ATLAS_VERSION}`
   * Set where you want to run SCM-atlas tools: default is `DIR_RUN=$HOME/Atlas1D/V${ATLAS_VERSION}`
   * Set where the reference datasets (e.g., LES) can be found: default is `DIR_REF=/cnrm/amacs/USERS/roehrig/share/SCM-atlas/References/V1.0`

3. Execute `install.sh`. A test is done at the end with provided SCM simulation with ARPEGE-Climat 6.3.1 for the ARMCU/REF, RICO/SHORT and SANDU/REF cases. Check the output atlas at the link provided at the end of the test.

## Using SCM-atlas
1. Go in the `DIR_RUN` directory
2. Source setenv to have the right PATH and PYTHONPATH environment variables

   `source setenv`

3. Prepare you own config file, following the example `config/config_CMIP6.py`

4. Run SCM-atlas:

   `run_atlas1d.py -config config/YOUR_CONFIG_FILE`

   You can add the option --pdf to export pdf files for each case.
