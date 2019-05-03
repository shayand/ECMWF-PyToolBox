'''
NAME
    ECMWF PyToolBox - ERA5 Area Data Extractor
PURPOSE
    This script get ERA5 data for specific area in world
PROGRAMMER(S)
    Shayan Davarzani (info@shayand.com) [Master of Engineering - Civil Engineering]
REFERENCES
    Institute of Earth Sciences Coders -- https://iescoders.com/2017/10/03/reading-netcdf4-data-in-python/
    Dr. Ali Asghar Golshani -- My Best and Scientist Teacher -- https://ir.linkedin.com/in/aliasghar-golshani-57a78414/
    IA University Central Tehran Branch-- https://www.iau.ac.ir/
'''
import cdsapi

c = cdsapi.Client()

year = "1979"
filename = "persian-gulf-"+year+"-wave.nc"

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type':'reanalysis',
        'format':'netcdf',
        'variable':[
            '10m_wind_direction','10m_wind_speed','mean_wave_direction',
            'mean_wave_period','peak_wave_period','significant_height_of_combined_wind_waves_and_swell'
        ],
        'area' : [18,46,30.5,73], # North, West, South, East. Default: global
        'year':[
            '1979'
        ],
        'month':[
            '01','02','03',
            '04','05','06',
            '07','08','09',
            '10','11','12'
        ],
        'day':[
            '01','02','03',
            '04','05','06',
            '07','08','09',
            '10','11','12',
            '13','14','15',
            '16','17','18',
            '19','20','21',
            '22','23','24',
            '25','26','27',
            '28','29','30',
            '31'
        ],
        'time':[
            '00:00',
            '06:00',
            '12:00',
            '18:00'
        ]
    },
    filename)