try:
    ds = gdal.Open('S:\\\\JESSE\\\\GIS\\\\AngeloSagehorn\\\\area_slope_shed.tif')
#     ds = gdal.Open('S:\JESSE\GIS\DEM\Elev_FlowAccum_FlowLength_Watershed4.tif')
except RuntimeError, e:
    print 'Unable to open .tif'
    print e
    sys.exit(1)

print ds.GetMetadata()