# -*- coding: utf-8 -*-
"""Fill the TODO cells of Module 05 Practice Project Part 1 (wildfire analysis) and execute."""
import nbformat
from nbclient import NotebookClient

NB_IN = "CISC3015_Assgn02_Module_05_Practice_Lab01_Wildfire_Australia.ipynb"
NB_OUT = "CISC3015_Assgn02_Module_05_Practice_Lab01_Wildfire_Australia_COMPLETED.ipynb"

nb = nbformat.read(NB_IN, as_version=4)

def setcell(i, src):
    nb.cells[i].source = src

# [10] keep pip installs (harmless)

# [17] replace JupyterLite js-fetch with standard pandas read
setcell(17, '''URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv"
df = pd.read_csv(URL)
print('Data read into a pandas dataframe!')''')

# [27] verify columns again
setcell(27, "df.dtypes")

# [33] TASK 1.1
setcell(33, '''plt.figure(figsize=(12, 6))
# Grouping the data by 'Year' and calculating the mean of 'Estimated_fire_area'
df_new = df.groupby('Year')['Estimated_fire_area'].mean()
# Plotting the data
df_new.plot(x=df_new.index, y=df_new.values)
plt.xlabel('Year')
plt.ylabel('Average Estimated Fire Area (km²)')
plt.title('Estimated Fire Area over Time')
plt.show()''')

# [38] TASK 1.2
setcell(38, '''# Grouping the data by both 'Year' and 'Month', and calculating the mean of 'Estimated_fire_area'
df_new = df.groupby(['Year','Month'])['Estimated_fire_area'].mean()
# Plotting the data
df_new.plot(x=df_new.index, y=df_new.values)
plt.xlabel('Year, Month')
plt.ylabel('Average Estimated Fire Area (km²)')
plt.title('Estimated Fire Area over Time')
plt.show()''')

# [46] TASK 1.3
setcell(46, '''# Creating a bar plot using seaborn to visualize the distribution of mean estimated fire brightness across regions
plt.figure(figsize=(10, 6))
# Using seaborn's barplot function to create the plot
sns.barplot(data=df, x='Region', y='Mean_estimated_fire_brightness')
plt.xlabel('Region')
plt.ylabel('Mean Estimated Fire Brightness (Kelvin)')
plt.title('Distribution of Mean Estimated Fire Brightness across Regions')
plt.show()''')

# [51] TASK 1.4
setcell(51, '''# Creating a pie chart to visualize the portion of count of pixels for presumed vegetation fires across regions
plt.figure(figsize=(10, 6))
# Grouping the data by region and summing the counts
region_counts = df.groupby('Region')['Count'].sum()
# Creating the pie chart using plt.pie function
# Labels are set to the region names, and autopct is used to display percentage
plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%')
plt.title('Percentage of Pixels for Presumed Vegetation Fires by Region')
plt.axis('equal')
plt.show()''')

# [54] TASK 1.5
setcell(54, '''# Creating a customized pie chart (autpct removed, percentages moved to legend)
plt.figure(figsize=(10, 6))
region_counts = df.groupby('Region')['Count'].sum()
plt.pie(region_counts, labels=region_counts.index)
plt.title('Percentage of Pixels for Presumed Vegetation Fires by Region')
plt.legend([(i,round(k/region_counts.sum()*100,2)) for i,k in zip(region_counts.index, region_counts)])
plt.axis('equal')
plt.show()''')

# [58] TASK 1.6
setcell(58, '''# Creating a histogram to visualize the distribution of mean estimated fire brightness
plt.figure(figsize=(10, 6))
# Using plt.hist to create the histogram
# Setting the number of bins to 20 for better visualization
plt.hist(x=df['Mean_estimated_fire_brightness'], bins=20)
plt.xlabel('Mean Estimated Fire Brightness (Kelvin)')
plt.ylabel('Count')
plt.title('Histogram of Mean Estimated Fire Brightness')
plt.show()''')

# [61] TASK 1.7
setcell(61, '''# Creating a histogram to visualize the distribution of mean estimated fire brightness across regions using Seaborn
sns.histplot(data=df, x='Mean_estimated_fire_brightness', hue='Region')
plt.show()''')

# [64] TASK 1.7 stacked
setcell(64, '''# Creating a stacked histogram to visualize the distribution of mean estimated fire brightness across regions
sns.histplot(data=df, x='Mean_estimated_fire_brightness', hue='Region', multiple='stack')
plt.xlabel('Mean Estimated Fire Brightness (Kelvin)')
plt.ylabel('Count')
plt.title('Stacked Histogram of Mean Estimated Fire Brightness across Regions')
plt.show()''')

# [69] TASK 1.8
setcell(69, '''# Creating a scatter plot to visualize the relationship between mean estimated fire radiative power and mean confidence
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Mean_confidence', y='Mean_estimated_fire_radiative_power')
plt.xlabel('Mean Confidence')
plt.ylabel('Mean Estimated Fire Radiative Power (MW)')
plt.title('Mean Estimated Fire Radiative Power vs. Mean Confidence')
plt.show()''')

# [74] TASK 1.9
setcell(74, '''# instantiate a feature group
aus_reg = folium.map.FeatureGroup()

# Create a Folium map centered on Australia
Aus_map = folium.Map(location=[-25, 135], zoom_start=4)

# loop through the region and add to feature group
for lat, lng, lab in zip(reg.Lat, reg.Lon, reg.region):
    aus_reg.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            popup=lab,
            radius=5, # define how big you want the circle markers to be
            color='red',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add incidents to map
Aus_map.add_child(aus_reg)
Aus_map''')

client = NotebookClient(nb, timeout=900, kernel_name="python3",
                        resources={"metadata": {"path": "."}})
client.execute()
nbformat.write(nb, NB_OUT)

errs = 0
for i, cell in enumerate(nb.cells):
    if cell.cell_type == "code":
        for out in cell.get("outputs", []):
            if out.get("output_type") == "error":
                errs += 1
                print("ERROR in cell", i, out.get("ename"), str(out.get("evalue"))[:200])
print("executed:", NB_OUT, "| error outputs:", errs)
