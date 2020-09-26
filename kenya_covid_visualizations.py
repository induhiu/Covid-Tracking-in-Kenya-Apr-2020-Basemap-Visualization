''' Ian Nduhiu
    Basemap visualizations to aid covid tracking in Kenya as of April 2020
'''
# Imports necessary for visualization
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Get directory containing epsg file for Basemap import to work
import os
os.environ["PROJ_LIB"] = 'C:\\Users\\nderi\\.conda\\pkgs\\proj4-5.2.0-ha925a31_1\\Library\\share'
from mpl_toolkits.basemap import Basemap

def draw_map(lons, lats, pop_density, var_tested, colorbar_label, directory="", colorbar_scheme=""):
    ''' 
    Draws scatterplot Basemap map of Kenya and saves plot in given directory path
    
    Args:
        lons: Numpy array of values representing longitudes
        lats: Numpy array of values representing latitudes
        pop_density: Numpy array of values representing population density
        var_tested: Numpy array of values representing the variable of interest
        colorbar_label: String representing the colorbar title
        directory: (Optional) string, directory path for saving file
        colorbar_scheme: (Optional) string, scheme for colorbar

    Returns:
        None
    '''

    # Draws background map of Kenya.
    _ = plt.figure(figsize=(8,8))
    m = Basemap(projection='lcc', lat_0=0.0236, lon_0=37.9062, width=1E6
    , height=1.2E6, resolution='h')
    m.shadedrelief()
    m.drawcoastlines(color='gray')
    m.drawcountries(color='gray')
    # m.fillcontinents(lake_color="aqua", zorder=0)

    # Draw scatterplot on the Basemap figure and include colorbar, legend
    m.scatter(lons, lats, latlon=True, c=var_tested, s=pop_density, cmap=colorbar_scheme, alpha=0.5)
    plt.colorbar(label=colorbar_label)
    for density in [100, 300, 500]:
        plt.scatter([],[],c='k',alpha=0.5,s=density, label=str(density) + ' individuals per km$^2$')
    plt.legend(scatterpoints=1, frameon=False,
               labelspacing=1, loc='lower left')

    # Set plot title and save/show figure
    plt.title(colorbar_label + " against Population Density per county")    
    plt.savefig(directory + colorbar_label + " against Population density")



if __name__ == "__main__":
    # Extract first dataset
    amenities_dataset = pd.read_excel("Kenya Covid-19 Need Map - Amenities Count.xlsx", sheet_name="Sheet1")

    # Columns of interest in the first dataset
    columns_to_visualize = ["# of Hospitals (Level 4,5,6)",
                            "# of Hospital Beds",
                            "# of ICU Beds",
                            "# of Ventilators",
                            "# of Covid Isolation Centers",
                            "# of Beds in Isolation Centers",
                            "# of Covid treatment Centers",
                            "# of Covid Testing Centers"]

    # Visualize number of basic Covid-preparedness amenities per county
    for col in columns_to_visualize:
        draw_map(amenities_dataset["Longitude"].values, 
                 amenities_dataset["Latitude"].values,
                 amenities_dataset["Population Density"].values,
                 amenities_dataset[col].values, col,
                 "Covid-19 Basic Amenities in Kenya Visualized\\",
                 'cividis')

    # Extract second dataset and merge with former dataset to get pop density, longitude and lat
    preparedness_dataset = pd.read_excel("Kenya Covid 19 Need Map - Preparedness Benchmark met.xlsx", sheet_name="Sheet1")
    modified_dataset = pd.merge(amenities_dataset, preparedness_dataset, on="County")

    # Visualize covid-19 preparedness benchmark per Kenyan county
    for col in preparedness_dataset.columns:
        if col != "County":
            draw_map(modified_dataset["Longitude"].values,
                     modified_dataset["Latitude"].values,
                     modified_dataset["Population Density"].values,
                     modified_dataset[col].values,
                     col,
                     "Covid-19 Preparedness Check in Kenya Visualized\\",
                     "viridis")



