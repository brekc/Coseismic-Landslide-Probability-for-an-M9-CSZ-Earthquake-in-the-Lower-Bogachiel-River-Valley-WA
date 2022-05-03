## Import modules
import rasterio
import fiona
import numpy as np

## Set file paths
shp = r'C:\Users\brekc\Desktop\Capstone_Data\BRV_Ext_reproj.shp'
pgv_data_in= r'C:\Users\brekc\Desktop\Capstone_Data\CSZ_M9\CSZ_M9_100m'
pgv_data_out = r'C:\Users\brekc\Desktop\Capstone_Data\CSZ_M9\CSZ_M9_100m_clip'

## Create a list for M9 CSZ scenarios
csz_nums = ['csz002', 'csz003', 'csz004', 
            'csz005', 'csz006', 'csz007', 
            'csz008', 'csz009', 'csz010', 
            'csz011', 'csz012', 'csz013', 
            'csz014', 'csz017', 'csz018', 
            'csz019', 'csz020', 'csz021', 
            'csz022', 'csz023', 'csz024', 
            'csz025', 'csz026', 'csz027', 
            'csz028', 'csz029', 'csz030', 
            'csz031', 'csz032', 'csz033']

## Clip the PGV data to the extent of the study area
for csz_mod in csz_nums:
    input_data = pgv_data_in + '\\' + csz_mod + '_100m.tif'
    pgv_clip = pgv_data_out + '\\' + csz_mod + '_100m_clip.tif'
    
    with fiona.open(shp, "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]
    mask_kwargs = {'filled':True, 'crop':True, 'nodata':np.nan}
    
    with rasterio.open(input_data) as model_raster:
        out_raster, out_transform = rasterio.mask.mask(model_raster, shapes, **mask_kwargs)
        out_meta = model_raster.meta
    
    out_meta.update({"driver": "GTiff",
                 "height": out_raster.shape[1],
                 "width": out_raster.shape[2],
                 "transform": out_transform})

    with rasterio.open(pgv_clip, "w", **out_meta) as dest:
        dest.write(out_raster)

    