from setuptools import setup, find_namespace_packages
from setup_helper import find_resource_files

# -- Apps Definition -- #
app_package = 'national_water_level_forecast_ecuador'
release_package = 'tethysapp-' + app_package

# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_resource_files('tethysapp/' + app_package + '/templates', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/public', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/workspaces', 'tethysapp/' + app_package)


resource_files += find_resource_files('tethysapp/' + app_package + '/scripts', 'tethysapp/' + app_package)
setup(
    name=release_package,
    version='1.2',
    description='This app uses the Bias Correction, the GESS forecast, and the observed water level to create a  National Hydrological Forecast Model in Ecuador.',
    long_description='',
    keywords='"Hydrology", "Time Series", "Bias Correction", "Hydrostats", "GEOGloWS", "Water Level", "Ecuador"',
    author='Darlly Judith Rojas-Lesmes, Jorge Luis Sanchez-Lozano, Karina Larco',
    author_email='djrojasl@unal.edu.co, jorgessanchez7@gmail.com, karynina3@gmail.com',
    url='',
    license='',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)