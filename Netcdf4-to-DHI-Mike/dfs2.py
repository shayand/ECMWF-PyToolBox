'''
NAME
    ECMWF PyToolBox - Converts NetCDF to CF Convention (DHI Mike raw input file)
PURPOSE
    This script converts ECMWF netcdf data to CF Convention and raw text file
    that can be used for importing data to DHI Mike
PROGRAMMER(S)
    Shayan Davarzani (info@shayand.com) [Master of Engineering - Civil Engineering]
REVISION HISTORY
    20190425 -- Initial python file which extract 2D data from NetCDF
                Thanks to Chris Slocum for his documenting guide
                Special Thanks to JetBrains for developing PyCharm
REFERENCES
    netcdf4-python -- http://code.google.com/p/netcdf4-python/
    netCDF4 module -- https://unidata.github.io/netcdf4-python/netCDF4/index.html
    Institute of Earth Sciences Coders -- https://iescoders.com/2017/10/03/reading-netcdf4-data-in-python/
    Dr. Ali Asghar Golshani -- My Best and Scientist Teacher -- https://ir.linkedin.com/in/aliasghar-golshani-57a78414/
    Dr. Vahid Chegini -- https://www.linkedin.com/in/vahid-chegini-72962b92/
    IA University Central Tehran Branch-- https://www.iau.ac.ir/
    Mostafa Nazarali -- https://github.com/mostafanazarali/
'''
import netCDF4
from datetime import datetime

# initial params

exportFileName = "persian-gulf-wave.txt" # you can give name with , your destination path
geographicalArea = "persian-gulf-oman-sea"
importFileName = "tez\persian-gulf-1979-wave.nc" # nc file
timeStep = 6 # time steps in hours
floatingPoint = "4" # number of floats

# open a file for writting on it
exportFile = open(exportFileName, "w")

importFile = netCDF4.Dataset(importFileName, "r")

importVariablesTime = importFile.variables["time"]

importDimLatitude = importFile.dimensions["latitude"]
importDimLongitude = importFile.dimensions["longitude"]

dates = netCDF4.num2date(importVariablesTime[:], importVariablesTime.units, importVariablesTime.calendar)

axisDate = datetime.fromtimestamp(importVariablesTime[0])

exportFile.write('"Title" "'+geographicalArea+'"\n')
exportFile.write('"Dim" 2\n')
exportFile.write('"Geo" "LONG/LAT" %d %d 0\n' % ( importFile.variables["longitude"][0] , importFile.variables["latitude"][0] ))
exportFile.write('"Time" "EqudistantTimeAxis" "%s" "%s" %d %d\n' % (axisDate.strftime("%Y-%m-%d"),axisDate.strftime("%I:%M:%S"),len(importVariablesTime), timeStep * 3600))
exportFile.write('"NoGridPoints" %d %d\n' % (len(importDimLongitude) , len(importDimLatitude) ))
exportFile.write('"Spacing" %g %g\n' % (abs(importFile.variables["longitude"][1] - importFile.variables["longitude"][0]),abs(importFile.variables["latitude"][1] - importFile.variables["latitude"][0])))
exportFile.write('"NoStaticItems" 0\n')


totalDynamicParams = 0
dynamicParams = []
dynamicVariables = []
for key , singleVar in importFile.variables.items():
    if (key == "time") or  (key == "latitude") or (key == "longitude"):
        continue
    else:
        totalDynamicParams = totalDynamicParams + 1
        dynamicParams.append([singleVar.long_name,singleVar._name,singleVar.units])
        dynamicVariables.append(singleVar[:,:,:])
#

exportFile.write('"NoDynamicItems" '+ str(totalDynamicParams) +'\n')

for dynamicParam in dynamicParams:
    exportFile.write('"Item" "%s" "%s" "%s"\n' % (dynamicParam[0],dynamicParam[1],dynamicParam[2]))

exportFile.write('NoCustomBlocks 1\n')
exportFile.write('"M21_Misc" 1 7 0 -1E-030 -900 -999 -1E-030 -1E-030 -1E-030\n')
exportFile.write('"Delete" -1E-030\n')
exportFile.write('"DataType" 0\n')
exportFile.write('\n')

dynamicKey = 0
floatFormat = "1." + floatingPoint + "f"


dynamicParamDetails = dynamicVariables[0].shape
totalTimeSteps = dynamicParamDetails[0]
totalX = dynamicParamDetails[1]
totaly = dynamicParamDetails[2]

stepCount = 0
while stepCount < totalTimeSteps:
    dynamicKey = 0
    for dynamicParam in dynamicParams:
        itemNo = dynamicKey +1
        exportFile.write('\n"tstep" %d "item" %d "layer" 0\n' % (stepCount, itemNo))
        singleXY = dynamicVariables[dynamicKey][stepCount]
        countX = 0
        while countX < totalX:
            singleY = singleXY[countX]
            finalStr = ' '.join(format(x, floatFormat) for x in singleY)
            exportFile.write("%s\n" % (finalStr))
            countX = countX + 1
        dynamicKey = dynamicKey + 1
    stepCount = stepCount + 1
exportFile.close()