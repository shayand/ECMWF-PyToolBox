'''
NAME
    ECMWF PyToolBox - Merging two or more Netcdf4 files
PURPOSE
    This script merge two or more Netcdf4 files and export a Netcdf4 with diffrent datasets
PROGRAMMER(S)
    Shayan Davarzani (info@shayand.com) [Master of Engineering - Civil Engineering]
REFERENCES
    Institute of Earth Sciences Coders -- https://iescoders.com/2017/10/03/reading-netcdf4-data-in-python/
    Dr. Ali Asghar Golshani -- My Best and Scientist Teacher -- https://ir.linkedin.com/in/aliasghar-golshani-57a78414/
    IA University Central Tehran Branch-- https://www.iau.ac.ir/
'''
import xarray

filesArray = ["tez\persian-gulf-2012-2015-other.nc","tez\persian-gulf-2016-2019-other.nc"] #input files for merging

ds = xarray.merge([xarray.open_dataset(f) for f in filesArray])
ds.to_netcdf('persian-gulf-2000-2011-other.nc')