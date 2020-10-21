# Covid-Tracking-in-Kenya-Apr-2020-Basemap-Visualization
## Description
I volunteered to help visualize the level of need and preparedness in relation to Covid-19 for one of my acquaintances. Having just learned about Matplotlib's Basemap at that time, I thought to try out some Basemap visualizations.  

## Datasets used
Two datasets used: "Kenya Covid 19 Need Map - Amenities Count.xlsx" and "Kenya Covid 19 Need Map - Preparedness Benchmark met.xlsx". 

"Kenya Covid 19 Need Map - Amenities Count.xlsx" contains data per county for variables such as Latitude, Longitude, Population Density, Number of Hospitals per 100k, Number of ICU beds, Number of Ventilators and so on. 

"Kenya Covid 19 Need Map - Preparedness Benchmark met.xlsx" contains data per country like the former, but instead focuses on attainment of the prepardness benchmark for certain variables: Number of Isolation Beds, Number of ICU Beds, Number of Ventilators, Number of ICU beds for General Patients.

## Main procedure
For each column of interest, I created a Basemap lcc projection of Kenya on which I scattered the longitudes and latitudes of the various counties. For each county, the size of the point represented its population size while the color represented the column of interest number scaled according to the colorbar provided.

For the visualizations where attainment of benchmark was being checked, the colorbar scale goes from negative to positive.

## Sample results
 
Below is a sample visualization: 
![](https://github.com/induhiu/Covid-Tracking-in-Kenya-Apr-2020-Basemap-Visualization/blob/master/Covid-19%20Preparedness%20Check%20in%20Kenya%20Visualized/ICU%20Beds%20Benchmark%20Remaining%20against%20Population%20density.png)
