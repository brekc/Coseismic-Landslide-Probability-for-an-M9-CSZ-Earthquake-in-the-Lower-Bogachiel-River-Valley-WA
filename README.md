# Coseismic Landslide Probability for an M9 Cascadia Subduction Zone Earthquake in the Lower Bogachiel River Valley, WA
**By: Brek Chiles, 2022**

## Introduction
  The Cascadia Subduction Zone (CSZ) presents a significant seismic hazard to western Washington, Oregon, the northwest coast of California, Vancouver Island, and lower mainland British Columbia. Seismic activity from the CSZ is caused by the subduction of the Juan de Fuca plate underneath the North American plate (Atwater et al., 2015). The subduction zone can generate magnitude 9 (M9) megathrust earthquakes that cause abrupt coastal land-level change, tsunamis, and strong and long-duration ground shaking. Intense ground shaking can also cause widespread landsliding. According to a report by the Cascadia Region Earthquake Workgroup (2013), coastal areas will experience more ground shaking during a CSZ earthquake than other areas in Cascadia. Coastal communities may also lose access to inland areas as ground shaking and landslides cause severe damage to roadways and disrupt transportation networks (Cascadia Region Earthquake Workgroup, 2013). On the western Olympic Peninsula in Washington, communities are often affected by landslide and flooding hazards that damage roadways and properties (Clallam County, 2010; Jefferson County, 2011). For communities surrounding the Bogachiel River Valley, like other coastal communities, blocked or damaged roadways could prevent people from fleeing tsunami inundation zones and stall relief efforts.
  
  The Bogachiel River Valley is situated between Clallam and Jefferson counties on the Olympic Peninsula of Washington State. As of 2020, Clallam and Jefferson counties have a combined population of more than a hundred thousand people (Mohrman, 2020). Transportation routes, often narrow, cut through the Olympic Mountain Range, dense forests, and coastal plains (Clallam County, 2010). U.S. Highway 101, the major roadway that connects southern California to the Washington Olympic Peninsula, transects the lower Bogachiel River Valley. In a hazard mitigation plan, Clallam County (2010) recognizes the vulnerability of U.S. Highway 101 to landslides, citing the example of a 2008 landslide that cut off the town of Forks from the highway.
  
  The purpose of this study is to determine areas where landslides are most likely to occur in the lower Bogachiel River Valley following an M9 CSZ earthquake. Using an empirical model (Nowicki Jessee et al., 2018), I calculate landslide probability, given peak ground velocity (PGV) from published M9 CSZ earthquake scenarios (Frankel et al., 2018), and geospatial datasets for topographic slope, compound topographic index (CTI), land cover, and lithology. With a coseismic landslide probability map, I model where ground failures may occur in the lower Bogachiel River Valley and estimate the area at high risk of landslides for an M9 CSZ earthquake. The results provide insight into the distribution of potential ground failures from M9 CSZ earthquakes which could help improve hazard mitigation and relief plans for the lower Bogachiel River Valley.

## Datasets
1. LiDAR data for computing topographic slope and CTI inputs
   - https://lidarportal.dnr.wa.gov/
   - Olympics North Opsw 2018, OESF 2014, and Olympic Park 2014
2. 30 M9 CSZ earthquake scenarios for PGV input
   - https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published//PRJ-1355/Frankel_etal_Production/csz010
   - For the NetCDF file, contact Alex Grant (agrant@usgs.gov) 
3. Surface geology at 1:100,000 scale for lithology input
   - https://www.dnr.wa.gov/programs-and-services/geology/publications-and-data/gis-data-and-databases
4. ESA WorldCover for land cover input
   - https://esa-worldcover.org/en

## Tools & Packages

## Methodology
1. Data Collection (Python & QGIS)
  - Geospatial Datasets, Landslide Inventory, Fieldwork (May and July 2021)
2. Calculate Coseismic Landslide Probability (Python)
  - Calculate probability for 30 M9 CSZ scenarios (Frankel et al., 2018)
3. Geospatial Analysis (QGIS)
  - Find overlap between 30 probability models for 50% and 75% probability thresholds, High-risk Area Estimates
4. Sensitivity Analysis for PGV Spatial Resolution (Python)
  - Find overlap between 30 probability models for 50% and 75% probability thresholds, High-risk Area Estimates

## Relevant Resources

## References
