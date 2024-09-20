# #!/usr/bin/env bash
# # exit on error
# set -o errexit

# pip install -r requirements.txt

# python manage.py collectstatic --no-input
# python manage.py migrate


#!/usr/bin/env bash
# exit on error
# set -o errexit

# Install GDAL and its development libraries
sudo apt-get update
sudo apt-get install -y gdal-bin libgdal-dev

# Check if GDAL is installed and locate its shared object file
gdalinfo --version  # Verify GDAL installation
GDAL_LIB=$(find /usr/lib -name "libgdal.so*" | head -n 1)

if [ -z "$GDAL_LIB" ]; then
    echo "GDAL library not found!"
    exit 1
fi

# Export the found GDAL library path
export GDAL_LIBRARY_PATH=$GDAL_LIB
echo "GDAL library path: $GDAL_LIBRARY_PATH"

# Set CPLUS_INCLUDE_PATH and C_INCLUDE_PATH
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

# Install Python dependencies
pip install -r requirements.txt

# Run Django management commands
python manage.py collectstatic --no-input
python manage.py migrate
