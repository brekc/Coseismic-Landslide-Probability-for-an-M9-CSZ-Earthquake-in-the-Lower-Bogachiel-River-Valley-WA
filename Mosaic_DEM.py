## Import modules
import rasterio as rio
import glob
import os
from rasterio.merge import merge
from rasterio.plot import show

## Set file paths 
data_path = r'C:\Users\brekc\Desktop\Capstone_Data\lidar_data'
out_tiff = r'C:\Users\brekc\Desktop\Capstone_Data\BRV_DEM.tif'

## Load the LiDAR data and create a mosaiced DEM
wildcard = '*.tif'
data_path_wildcard = os.path.join(data_path, wildcard)
lidar_files = glob.glob(data_path_wildcard)
data_to_mosaic = []

for lidar_data in lidar_files:
    lidar_rio = rio.open(lidar_data)
    data_to_mosaic.append(lidar_rio)

mosaic_dem, out_transform = merge(data_to_mosaic)
show(mosaic_dem, cmap='terrain') # This creates a plot of the mosaiced DEM

## Write a GeoTIFF file
out_metadata = lidar_rio.meta.copy()
out_metadata.update({"driver": "GTiff",
                "height": mosaic_dem.shape[1],
                "width": mosaic_dem.shape[2],
                "transform": out_transform})

if not os.path.exists(out_tiff):
    with rio.open(out_tiff, 'w', **out_metadata) as dest:
        dest.write(mosaic_dem)

