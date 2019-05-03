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
import xray

urls = ["tez\persian-gulf-1979-wave.nc","tez\persian-gulf-1980-1981-wave.nc"] #input files for merging
datasets = [xray.open_dataset(url) for url in urls]
merged = xray.concat(datasets, 'forecast_time')
merged.to_netcdf('all-data.nc')