#!/bin/sh

set -evx

#####################################################
# User specific

# SCM-atlas version
ATLAS_VERSION=1.2.1

# Directory where SCM-atlas is installed
DIR_ATLAS=$HOME/Tools/SCM-atlas/V${ATLAS_VERSION}

# Directory where SCM-atlas will be run
DIR_RUN=$HOME/Atlas1D/V${ATLAS_VERSION}

# Directory where References can be found
DIR_REF=/cnrm/amacs/USERS/roehrig/share/SCM-atlas/References/V1.0

#####################################################

DIR0=`pwd`

#####################################################
# Some tests to avoid overwriting

if [ -d "$DIR_ATLAS" ]; then
  echo "DIR_ATLAS="$DIR_ATLAS
  echo "DIR_ATLAS already exists. Please remove it or modify DIR_ATLAS at the top of install.sh"
  exit
fi

if [ -d "$DIR_RUN" ]; then
  echo "DIR_RUN="$DIR_RUN
  echo "DIR_RUN already exists. Please remove it or modify DIR_RUN at the top of install.sh"
  exit
fi

#####################################################
# Download and install SCM-atlas in DIR_ATLAS
[ -d $DIR_ATLAS ] || mkdir -p $DIR_ATLAS
cd $DIR_ATLAS

wget https://github.com/romainroehrig/SCM-atlas/archive/V${ATLAS_VERSION}.tar.gz
tar zxvf V${ATLAS_VERSION}.tar.gz
rm -f V${ATLAS_VERSION}.tar.gz
mv SCM-atlas-${ATLAS_VERSION}/* .
rm -rf SCM-atlas-${ATLAS_VERSION}

#####################################################
# Prepare what is needed to run SCM-atlas simulations in DIR_RUN
[ -d "$DIR_RUN" ] || mkdir -p $DIR_RUN
cd $DIR_RUN
cp -r $DIR_ATLAS/examples/* .
ln -s $DIR_ATLAS/apptools/run_atlas1d.py

tmp=$(printf '%s' "$DIR_ATLAS" | sed -e 's/[\/&]/\\&/g')
sed -i.bak "s/__DIR_ATLAS__/"$tmp"/" setenv

tmp=$(printf '%s' "$DIR_REF" | sed -e 's/[\/&]/\\&/g')
sed -i.bak "s/__DIR_REF__/"$tmp"/" setenv

#####################################################
# Some Testing
testing="y"

if [ $testing == "y" ]; then

    source setenv

    tmp=$(printf '%s' "$DIR_ATLAS" | sed -e 's/[\/&]/\\&/g')
    sed -i.bak "s/__DIR_ATLAS__/"$tmp"/" $DIR_ATLAS/test/config_test.py

    tmp=$(printf '%s' "$DIR_RUN" | sed -e 's/[\/&]/\\&/g')
    sed -i.bak "s/__DIR_RUN__/"$tmp"/" $DIR_ATLAS/test/config_test.py

    run_atlas1d.py -config $DIR_ATLAS/test/config_test.py

    echo "Check atlas at $DIR_RUN/MyAtlas/TEST/html/index.html"

fi

#####################################################
# Back in directory where installation was launched
cd $DIR0

