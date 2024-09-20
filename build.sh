# #!/usr/bin/env bash
# # exit on error
# set -o errexit

# pip install -r requirements.txt

# python manage.py collectstatic --no-input
# python manage.py migrate


#!/usr/bin/env bash
# exit on error
# set -o errexit

# Install GDAL and GEOS
sudo apt-get update
sudo apt-get install -y gdal-bin libgdal-dev libgeos-dev

# Set up environment variables for GDAL and GEOS (optional if set in settings.py)
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

# Install Python dependencies
pip install -r requirements.txt

# Run Django management commands
python manage.py collectstatic --no-input
python manage.py migrate
