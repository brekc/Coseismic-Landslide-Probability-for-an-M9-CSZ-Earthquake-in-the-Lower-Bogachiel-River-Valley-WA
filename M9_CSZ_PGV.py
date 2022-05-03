## Import modules
import xarray as xr
import os
import numpy as np
from scipy.interpolate import interp2d
import utm
import rioxarray as rio

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

## Set file paths
fpath = r'C:\Users\brekc\Desktop\Capstone_Data\CSZ_M9'
fn = '\SurfacePGA_PGV_all.nc' 

## Create GeoTIFFs for each M9 CSZ scenario
## Lines 28-68 were written by Alex Grant
for n in csz_nums:
    outdir = r'C:\Users\brekc\Desktop\Capstone_Data\CSZ_M9_100m'
    fout = n + '_pgv.tif'   # can name iteratively if saving all
    # lower left and upper right corners of output geotiffs (decimal degrees)
    lowerleft = [47, -125]
    upperright = [48.5, -123]
    csznumber = n  #realization name (may want to replace with loop to export all data)
    IMname = 'PGV'    #PGA or PGV     [g] and [cm/s]
    res = 100  # output resolution, meters
    kind = 'cubic'  #interpolation type
    
    def corners(lat, lon):
        east, north, zn, zl = utm.from_latlon(lat, lon)
        return north, east
    
    def meshrefine(IM, ll, ur, res = 2000, kind = 'linear'):
        lats = IM.lat.values
        lons = IM.lon.values
        
        los = np.arange(ll[1], ur[1], res)
        las = np.arange(ll[0], ur[0], res)
        
        fx = interp2d(lons, lats, IM, kind = kind)   #kind = cubic or linear interpolation
        IM_fine = fx(los, las)
        return IM_fine, los, las
    
    dat = xr.open_dataset(fpath+fn)
    ll = corners(*lowerleft)
    ur = corners(*upperright)
    IM = dat[IMname].sel(csz = csznumber)
    IM_fine, los, las = meshrefine(IM, ll, ur, res = res, kind = kind)
    
    WorkingDirectory = outdir
    if not os.path.exists(WorkingDirectory):
        os.makedirs(WorkingDirectory)
    os.chdir(WorkingDirectory)
    
    I = xr.Dataset({IMname: (['lat','lon'], IM_fine),}, coords = {'lon': (['lon'], los), 'lat': (['lat'], las)})
    
    I = I.rio.write_crs(32610)
    I.rio.set_spatial_dims('lon', 'lat')
    I.rio.to_raster(fout, driver = 'GTiff')
    
    