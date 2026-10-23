# -*- coding: utf-8 -*-
"""Fill the blank cells of Module 05 Final Project Part 1 (recession & automobile sales) and execute."""
import nbformat
from nbclient import NotebookClient

NB_IN = "CISC3015_Assgn02_Module_05_Final_Lab01_Recession_Automobile_Sales.ipynb"
NB_OUT = "CISC3015_Assgn02_Module_05_Final_Lab01_Recession_Automobile_Sales_COMPLETED.ipynb"

nb = nbformat.read(NB_IN, as_version=4)

def setcell(i, src):
    nb.cells[i].source = src

# [24] TASK 1.1 line chart of average automobile sales per year
setcell(24, '''#create data for plotting
df_line = df.groupby(df['Year'])['Automobile_Sales'].mean()
#create figure
plt.figure(figsize=(10, 6))
df_line.plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Average Automobile Sales')
plt.title('Average Automobile Sales fluctuation from year to year')
plt.show()''')

# [28] TASK 1.1 (continued) with year ticks and recession annotations
setcell(28, '''plt.figure(figsize=(10, 6))
df_line = df.groupby(df['Year'])['Automobile_Sales'].mean()
df_line.plot(kind='line')
plt.xticks(list(range(1980, 2024)), rotation=75)
plt.xlabel('Year')
plt.ylabel('Average Automobile Sales')
plt.title('Automobile Sales during Recession')
plt.text(1982, 650, '1981-82 Recession')
plt.text(2008, 650, '2007-09 Recession')
plt.legend()
plt.show()''')

# [33] TASK 1.2 advertising expenditure vs sales (non-recession)
setcell(33, '''# Assuming 'df' is your dataset
df_non_rec = df[df['Recession'] == 0]

# Calculate average automobile sales and average advertising expenditure by year (non-recession)
df_trends = df_non_rec.groupby('Year', as_index=False).agg(
    Avg_Sales=('Automobile_Sales', 'mean'),
    Avg_Ad_Spend=('Advertising_Expenditure', 'mean')
)

# Create line plots for average sales and advertising expenditure over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_trends, x='Year', y='Avg_Sales', marker='o', linestyle='-', color='green', label='Average Automobile Sales')
sns.lineplot(data=df_trends, x='Year', y='Avg_Ad_Spend', marker='s', linestyle='--', color='blue', label='Average Advertising Expenditure')

# Add labels, legend, title, and grid
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.title('Trends in Advertising Expenditure and Automobile Sales during Non-Recession Periods')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()''')

# [36] TASK 1.2 insight
setcell(36, '''# Insight:
# The graph shows that during non-recession periods, automobile sales are more volatile than
# advertising expenditure. While there are moments of alignment, sales often spike independently,
# suggesting other factors like market demand or economic conditions also play a significant role.
# The correlation between advertising and sales appears inconsistent over time.
print("See comment above for the insight.")''')

# [41] TASK 1.3 average sales recession vs non-recession
setcell(41, '''new_df = df.groupby('Recession')['Automobile_Sales'].mean().reset_index()

# Create the bar chart using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Recession', y='Automobile_Sales', hue='Recession', data=new_df)
plt.xlabel('Period')
plt.ylabel('Average Automobile Sales')
plt.title('Average Automobile Sales during Recession and Non-Recession')
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
plt.show()''')

# [45] TASK 1.3 vehicle-wise sales comparison
setcell(45, '''grouped_df = df.groupby(['Recession', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
# Create the grouped bar chart using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Recession', y='Automobile_Sales', hue='Vehicle_Type', data=grouped_df)
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
plt.xlabel('Period')
plt.ylabel('Average Automobile Sales')
plt.title('Vehicle-Wise Sales during Recession and Non-Recession Period')
plt.legend(title='Vehicle Type')
plt.show()''')

# [48] TASK 1.3 insight
setcell(48, '''# Insight:
# From this plot, we can understand that there is a drastic decline in the overall sales of the
# automobiles during recession. However, the most affected type of vehicle is executivecar and sports.
print("See comment above for the insight.")''')

# [52] TASK 1.4 GDP variation subplots
setcell(52, '''#Create dataframes for recession and non-recession period
rec_data = df[df['Recession'] == 1]
non_rec_data = df[df['Recession'] == 0]

#Figure
fig = plt.figure(figsize=(12, 6))

#Create different axes for subploting
ax0 = fig.add_subplot(1, 2, 1)  # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(1, 2, 2)  # add subplot 2 (1 row, 2 columns, second plot)

sns.lineplot(x='Year', y='GDP', data=rec_data, label='Recession', ax=ax0)
ax0.set_xlabel('Year')
ax0.set_ylabel('GDP')
ax0.set_title('GDP Variation during Recession Period')

sns.lineplot(x='Year', y='GDP', data=non_rec_data, label='Non-Recession', ax=ax1)
ax1.set_xlabel('Year')
ax1.set_ylabel('GDP')
ax1.set_title('GDP Variation during Non-Recession Period')

plt.tight_layout()
plt.show()''')

# [58] TASK 1.5 bubble plot seasonality
setcell(58, '''non_rec_data = df[df['Recession'] == 0]

size = non_rec_data['Seasonality_Weight']  # for bubble effect

sns.scatterplot(data=non_rec_data, x='Month', y='Automobile_Sales', size=size, hue='Seasonality_Weight', legend=False)

plt.xlabel('Month')
plt.ylabel('Automobile_Sales')
plt.title('Seasonality impact on Automobile Sales')

plt.show()''')

# [64] TASK 1.6 scatter consumer confidence vs sales
setcell(64, '''#Create dataframes for recession period
rec_data = df[df['Recession'] == 1]
plt.scatter(rec_data['Consumer_Confidence'], rec_data['Automobile_Sales'])

plt.xlabel('Consumer Confidence')
plt.ylabel('Automobile Sales')
plt.title('Consumer Confidence and Automobile Sales during Recessions')
plt.show()''')

# [67] TASK 1.6 scatter price vs sales
setcell(67, '''#Create dataframes for recession period
rec_data = df[df['Recession'] == 1]
plt.scatter(rec_data['Price'], rec_data['Automobile_Sales'])

plt.xlabel('Price')
plt.ylabel('Automobile Sales')
plt.title('Relationship between Vehicle Price and Sales during Recessions')
plt.show()''')

# [73] TASK 1.7 pie advertising expenditure recession vs non-recession
setcell(73, '''# Filter the data
Rdata = df[df['Recession'] == 1]
NRdata = df[df['Recession'] == 0]

# Calculate the total advertising expenditure for both periods
RAtotal = Rdata['Advertising_Expenditure'].sum()
NRAtotal = NRdata['Advertising_Expenditure'].sum()

# Create a pie chart for the advertising expenditure
plt.figure(figsize=(8, 6))

labels = ['Recession', 'Non-Recession']
sizes = [RAtotal, NRAtotal]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title('Advertising Expenditure during Recession and Non-Recession Periods')

plt.show()''')

# [76] TASK 1.7 insight
setcell(76, '''# Insight:
# It seems XYZAutomotives has been spending much more on the advertisements during non-recession
# periods as compared to during recession times. Fair enough!
print("See comment above for the insight.")''')

# [81] TASK 1.8 pie expenditure share by vehicle type during recession
setcell(81, '''# Filter the data
Rdata = df[df['Recession'] == 1]

# Calculate the sales volume by vehicle type during recessions
VTexpenditure = Rdata.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()

# Create a pie chart for the share of each vehicle type in total expenditure during recessions
plt.figure(figsize=(10, 6))

labels = VTexpenditure.index
sizes = VTexpenditure.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title('Share of Each Vehicle Type in Total Expenditure during Recessions')

plt.show()''')

# [87] TASK 1.9 lineplot unemployment effect
setcell(87, '''# Assuming 'df' is your dataset
df_rec = df[df['Recession'] == 1]

# Set figure size
plt.figure(figsize=(16, 6))

# Create line plot showing effect of unemployment rate on automobile sales, by vehicle type
sns.lineplot(
    data=df_rec,
    x='unemployment_rate',
    y='Automobile_Sales',
    hue='Vehicle_Type',
    marker='o'
)

# Customize labels, legend, and title
plt.title('Effect of Unemployment Rate on Vehicle Type and Sales')
plt.xlabel('Unemployment Rate')
plt.ylabel('Automobile Sales')
plt.legend(title='Vehicle Type')

# Show plot
plt.tight_layout()
plt.show()''')

# [90] TASK 1.9 insight
setcell(90, '''# Insight:
# The plot shows that automobile sales decline as unemployment rates rise during a recession, with
# sharp drops beyond 3%. SuperMiniCars, SmallFamilyCars, and MediumFamilyCars exhibit high volatility,
# reflecting their sensitivity to economic uncertainty and changing consumer priorities.
print("See comment above for the insight.")''')

# [94] OPTIONAL TASK 1.10 - neutralize the pyodide-only cell so the notebook runs in standard Jupyter
setcell(94, '''# OPTIONAL TASK 1.10 (choropleth map) is skipped here:
# the original cell requires the JupyterLite/pyodide environment (pyfetch) to download us-states.json.
# It can be completed in the Skills Network Labs environment if desired.
print("Optional Task 1.10 skipped (requires pyodide/JupyterLite environment).")''')

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
                print("ERROR in cell", i, out.get("ename"), str(out.get("evalue"))[:300])
print("executed:", NB_OUT, "| error outputs:", errs)
