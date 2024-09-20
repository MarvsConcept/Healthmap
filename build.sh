# #!/usr/bin/env bash
# # exit on error
# set -o errexit

# pip install -r requirements.txt

# python manage.py collectstatic --no-input
# python manage.py migrate


#!/usr/bin/env bash
# exit on error
# set -o errexit

# Install GDAL and dependencies
sudo apt-get update
sudo apt-get install -y gdal-bin libgdal-dev

# Ensure GDAL paths are correctly set
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

# Optional: find the GDAL path dynamically if it differs
export GDAL_LIBRARY_PATH=$(gdal-config --libs | awk '{print $1}' | sed 's/-L//g')

# Install Python dependencies
pip install -r requirements.txt

# Run Django management commands
python manage.py collectstatic --no-input
python manage.py migrate
