'''
Put all buoy reference information in here to be read in by all notebooks.
'''

import pandas as pd

# read in buoy info
# # can use the following to find the file online
# loc = 'https://raw.githubusercontent.com/kthyng/tabswebsite/master/includes/buoys.csv'
# bys = pd.read_csv(loc, index_col=0).to_dict('index')

bys = pd.read_csv('../data/stations/buoys.csv', index_col=0).to_dict('index')


# For station g06010, the single time series data given at
# https://tidesandcurrents.noaa.gov/cdata/DataPlot?id=g06010&bin=0&bdate=20180421&edate=20180422&unit=1&timeZone=UTC
# is equivalent to depth 5.79 from the depths file, which the top of the 1 m-deep
# bin and listed as bin 3 or 21 feet on the PORTS website. The center of the
# bin is approximately 6.29. The depths file gives the depth of the top of the
# bin.
# The way to back out the depths from the information in that file is, e.g for
# the first bin top of bin:
# sensor_depth + first_bin_center - half of bin size
# for the list depth of the first bin:
# sensor_depth + first_bin_center

# Precipitation data
# USGS 08067000 Trinity Rv at Liberty, TX
# USGS 08077650 Moses Lk-Galveston Bay nr Texas City, TX;
# USGS 08073600 Buffalo Bayou at W Belt Dr, Houston, TX

## River inflow to Trinity Bay ##
# https://txpub.usgs.gov/txwaterdashboard/index.html
# direct link, read in as local time
# USGS 08078000 Chocolate Bayou nr Alvin, TX (drains into west bay)
# USGS 08077600 Clear Ck nr Friendswood, TX (drains in north of Eagle Pt)
# USGS 08074500 Whiteoak Bayou at Houston, TX (drains into north end of bay)
# all going into San Jac, north end of bay:
#  USGS 08068500 Spring Ck nr Spring, TX
#  USGS 08068090 W Fk San Jacinto Rv abv Lk Houston nr Porter, TX
#  USGS 08070500 Caney Ck nr Splendora, TX
#  USGS 08071000 Peach Ck at Splendora, TX
#  USGS 08070200 E Fk San Jacinto Rv nr New Caney, TX
#  USGS 08071280 Luce Bayou abv Lk Houston nr Huffman, TX
# USGS 08067252 Trinity Rv at Wallisville, TX (Trinity river)

# USGS 08075730 Vince Bayou at Pasadena, TX
# USGS 08075605 Berry Bayou at Nevada St, Houston, TX
# USGS 08075400 Sims Bayou at Hiram Clarke St, Houston, TX
# USGS 08075000 Brays Bayou at Houston, TX
# USGS 08073700 Buffalo Bayou at Piney Point, TX
# USGS 08074540 Little Whiteoak Bayou at Trimble St, Houston, TX
# USGS 08075770 Hunting Bayou at IH 610, Houston, TX
# USGS 08076500 Halls Bayou at Houston, TX
# USGS 08076000 Greens Bayou nr Houston, TX
# USGS 08076180 Garners Bayou nr Humble, TX
# USGS 08067525 Goose Ck at Baytown, TX
# USGS 08067500 Cedar Bayou nr Crosby, TX
# USGS 08066500 Trinity Rv at Romayor, TX
# USGS 08042558 W Fk Double Bayou at Eagle Ferry Rd nr Anahuac, TX

# Set up dictionary of buoy parameters to use in notebooks.
# buoys[buoyname]['ll'] gives lon, lat
# color is plotting color
# vars are variables stored in data.csv
# llshift is lon, lat shift for labeling stations on map
buoys = {'BOLI': {'ll': ([-94.783, 29.342]),  'vars': ['WaterT [deg C]', 'Depth [m]', 'Salinity'], 'llshift': (-0.08, 0.02)},
         'MIDG': {'ll': ([-94.875, 29.508]),   'vars': ['WaterT [deg C]', 'Depth [m]', 'Salinity']},
         'FISH': {'ll': ([-94.854, 29.670]),   'vars': ['WaterT [deg C]', 'Depth [m]', 'Salinity']},
         'TRIN': {'ll': ([-94.746, 29.661]),   'vars': ['WaterT [deg C]', 'Depth [m]', 'Salinity'], 'llshift': (-0.02, 0.02)},
         'OLDR': {'ll': ([-94.783, 29.833]),  'vars': ['WaterT [deg C]', 'Depth [m]', 'Salinity']},
         '08078000': {'ll': ([-95.32283, 29.3713056]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.04, 0.0)},
         '08077600': {'ll': ([-95.1783, 29.5172]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (-0.16, -0.03)},
         '08074500': {'ll': ([-95.39694, 29.775]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (-0.04, 0.02)},
         '08068500': {'ll': ([-95.4361, 30.110278]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.02, -0.02)},
         '08068090': {'ll': ([-95.3382, 30.141167]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (-0.04, 0.02)},
         '08070500': {'ll': ([-95.302, 30.2594]),  'vars': ['Flow rate [m^3/s]']},
         '08071000': {'ll': ([-95.168056, 30.23250]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.02, -0.01)},
         '08070200': {'ll': ([-95.124167, 30.145278]),  'vars': ['Flow rate [m^3/s]']},
         '08071280': {'ll': ([-95.05972, 30.1094]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.03, 0.0)},
         '08067252': {'ll': ([-94.731, 29.812]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.03, -0.01)},

         '08075730': {'ll': ([-95.21611, 29.6944]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.0, 0.01)},
         '08075605': {'ll': ([-95.2289, 29.656389]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.0, -0.03)},
         '08075400': {'ll': ([-95.445833, 29.618611]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (-0.16, -0.03)},
         '08075000': {'ll': ([-95.411944, 29.696944]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.0, -0.03)},
         '08073700': {'ll': ([-95.5233, 29.7467]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (-0.16, -0.04)},
         '08074540': {'ll': ([-95.368056, 29.79278]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (-0.16, 0.02)},
         '08075770': {'ll': ([-95.2678, 29.793056]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.0, 0.02)},
         '08076500': {'ll': ([-95.334722, 29.86167]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.0, 0.01)},
         '08076000': {'ll': ([-95.3067, 29.918056]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (-0.16, 0.02)},
         '08076180': {'ll': ([-95.23375, 29.9336389]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (-0.1, 0.03)},
         '08067525': {'ll': ([-94.99944, 29.77056]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.0, 0.02)},
         '08067500': {'ll': ([-94.9856, 29.9725]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.0, 0.02)},
         '08066500': {'ll': ([-94.85056, 30.425]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.0, 0.01)},
         '08042558': {'ll': ([-94.666114, 29.6756]),  'vars': ['Flow rate [m^3/s]'], 'llshift': (0.0, 0.02)},


         '08072000': {'ll': ([-95.1411, 29.91611]),  'vars': ['Gage height [m]'], 'llshift': (0.02, 0.01)},


         '08067000': {'ll': ([-94.818056, 30.0575]),  'vars': ['Rain [cm]'], 'llshift': (0.03, 0)},
         '08077650': {'ll': ([-94.92, 29.4472]),  'vars': ['Rain [cm]'], 'llshift': (-0.17, -0.01)},
         '08073600': {'ll': ([-95.55750, 29.76194]),  'vars': ['Rain [cm]'], 'llshift': (-0.03, 0.02)},
         '8771486': {'ll': ([bys['8771486']['lon'], bys['8771486']['lat']]),
                     'vars': ['Water Level [m]', 'AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]'], 'llshift': (-0.18, 0.01)},
         '8770613': {'ll': ([bys['8770613']['lon'], bys['8770613']['lat']]),
                     'vars': ['Water Level [m]', 'AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]', 'Salinity'], 'llshift': (-0.02, 0.04)},
         '8771013': {'ll': ([bys['8771013']['lon'], bys['8771013']['lat']]),
                     'vars': ['Water Level [m]', 'AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]', 'Salinity'], 'llshift': (-0.15, 0.02)},
         '8771341': {'ll': ([bys['8771341']['lon'], bys['8771341']['lat']]),
                     'vars': ['Water Level [m]', 'AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]',
                             'AtmPr [MB]']},
         '8771450': {'ll': ([bys['8771450']['lon'], bys['8771450']['lat']]),
                     'vars': ['Water Level [m]', 'AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]',
                             'AtmPr [MB]'], 'llshift': (0, -0.035)},
         'B': {'ll': ([bys['B']['lon'], bys['B']['lat']]),
                     'vars': ['AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]', 'Salinity', 'Along [cm/s]', 'Across [cm/s]']},
         'g06010': {'ll': ([bys['g06010']['lon'], bys['g06010']['lat']]),
                     'vars': ['Along [cm/s]'], 'llshift': (0.01, -0.03)},
         '42035': {'ll': ([bys['42035']['lon'], bys['42035']['lat']]),
                     'vars': ['AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]']},
         '8770808': {'ll': ([bys['8770808']['lon'], bys['8770808']['lat']]),
                     'vars': ['Water Level [m]', 'AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]']},
         '8770777': {'ll': ([bys['8770777']['lon'], bys['8770777']['lat']]),
                     'vars': ['Water Level [m]', 'AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]'], 'llshift': (0.0, 0.03)},
         '8770822': {'ll': ([bys['8770822']['lon'], bys['8770822']['lat']]),
                     'vars': ['Water Level [m]', 'AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]']},
         '8770971': {'ll': ([bys['8770971']['lon'], bys['8770971']['lat']]),
                     'vars': ['Water Level [m]', 'AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]']},
         '8771972': {'ll': ([bys['8771972']['lon'], bys['8771972']['lat']]),
                     'vars': ['Water Level [m]', 'AirT [deg C]', 'WaterT [deg C]', 'East [m/s]', 'North [m/s]']}
        }
