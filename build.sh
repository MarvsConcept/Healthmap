#!/usr/bin/env bash
# exit on error
# set -o errexit

echo "Starting build process..."

# Install GDAL and its development libraries
echo "Installing GDAL and development libraries..."
apt-get update
apt-get install -y gdal-bin libgdal-dev

# Check if GDAL is installed and locate its shared object file
echo "Verifying GDAL installation..."
gdalinfo --version
GDAL_LIB=$(find /usr/lib -name "libgdal.so*" | head -n 1)

if [ -z "$GDAL_LIB" ]; then
    echo "Error: GDAL library not found!"
    exit 1
fi

# Export the found GDAL library path
export GDAL_LIBRARY_PATH=$GDAL_LIB
echo "GDAL library path set to: $GDAL_LIBRARY_PATH"

# Set include paths for GDAL
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

# Print Python and GDAL versions
echo "Python version:"
python --version
echo "GDAL version:"
gdal-config --version

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --no-cache-dir -r requirements.txt

# Run Django management commands
echo "Running Django management commands..."
python manage.py collectstatic --no-input
python manage.py migrate

# Log GDAL library path for debugging
echo "GDAL library path set to: $GDAL_LIBRARY_PATH" >> build_log.txt

echo "Build process completed."