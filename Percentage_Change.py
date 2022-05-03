## Import modules
import pandas as pd

## area_probability_threshold = [100m, 50m]
area_50_pt = [15.4, 15.2]
area_75_pt = [4.5, 5.1]

## Create series
area_50_pt_pd = pd.Series(area_50_pt)
area_75_pt_pd = pd.Series(area_75_pt)

## Calculate percentage change
area_50_pc = (area_50_pt_pd.pct_change())*100
area_75_pc = (area_75_pt_pd.pct_change())*100

## Print percentage change
print("Percentage change for 50%: " + str(round(area_50_pc[1], 1)) + '%')
print("Percentage change for 75%: " + str(round(area_75_pc[1], 1)) + '%')

