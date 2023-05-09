import geopandas as gpd
import pygeos
import uuid
import pandas as pd

imd_grid_path = '/mnt/d/vassar_python/gpd_c_i/IWM_0.05_GRID.shp'
intersection_file_path = '/mnt/d/vassar_python/gpd_c_i/Mahanadi_Above_Delta_subbasin_with_UUID_4326.shp'

output_file_path = '/mnt/d/vassar_python/gpd_c_i/Mahanadi_Above_Delta_imge_inter.shp'


def create_imd_intercsection(imd_grid, inte_file):
    """
    The function takes imd grid and the polygon file. 
    Return geodataframe of intersection with area and centriod.
    
    """
    #convert to 4326 coordinate system for to identify comman overlapping area
    imd_grid = imd_grid.to_crs(4326)
    inte_file = inte_file.to_crs(4326)
    
    #The overlay function calculates the intersetion area between two gdf (The output might be multipolygon)
    overlayyy = gpd.overlay(imd_grid, inte_file, how='intersection')
    
    # for multiplogon geometry calculating centriod of largest polygon
    # 1. created uuid for multipolygon for merging 
    overlayyy['uuid'] = overlayyy.apply(lambda _: uuid.uuid4(), axis=1)
    # 2. explode the geometry to make seperate polygons.
    exploded = overlayyy.explode()
    # 3. add centriod x and y co-ordinates 
    exploded["x"] = exploded.centroid.x
    exploded["y"] = exploded.centroid.y
    # 4. calculate area 
    exploded_cea = exploded['geometry'].to_crs({'proj':'cea'})
    exploded['Area_trial'] = exploded_cea.area
    # 5. get id of polygons which is having largest area
    idx = exploded.groupby(['uuid'])['Area_trial'].transform(max) == exploded['Area_trial']
    # 6. create filterd dataframe with filterd ID
    filter_x_y = exploded[idx]
    # 7. merge the x and y centriod coordinates in overlay file 
    merged = overlayyy.merge(filter_x_y[['uuid','x', 'y']], on = 'uuid')
    
    #calculating the area for multipolygon.
    merged_cea = merged['geometry'].to_crs({'proj':'cea'})
    merged['Area_sqkm'] = merged_cea.area / 10**6
    
    return merged


imd_grid = gpd.read_file(imd_grid_path)
inte_file = gpd.read_file(intersection_file_path)

merged = create_imd_intercsection(imd_grid, inte_file)

merged.to_file(output_file_path)