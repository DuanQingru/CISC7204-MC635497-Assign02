# -*- coding: utf-8 -*-
"""Fill in the 7 'Write your code here' cells of Lab01 Plotly Basics notebook and execute it."""
import nbformat
from nbclient import NotebookClient

NB_IN = "CISC3015_Assgn02_Module_04_Lab01_Plotly_Basics.ipynb"
NB_OUT = "CISC3015_Assgn02_Module_04_Lab01_Plotly_Basics_COMPLETED.ipynb"

solutions = [
    # 1. Scatter Plot: Distance vs Departure Time (red markers)
    """##First we will create an empty figure ising go.Figure()
fig=go.Figure()
#Next we will create a scatter plot by using the add_trace function and use the go.scatter() function within it
# In go.Scatter we define the x-axis data,y-axis data and define the mode as markers with color of the marker as red
fig.add_trace(go.Scatter(x=data['Distance'], y=data['DepTime'], mode='markers', marker=dict(color='red')))
fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DepTime')
# Display the figure
fig.show()""",
    # 2. Line Plot: Month vs Average Flight Delay Time (green line)
    """##First we will create an empty figure ising go.Figure()
fig=go.Figure()
##Next we will create a line plot by using the add_trace function and use the go.scatter() function within it
# In go.Scatter we define the x-axis data,y-axis data and define the mode as lines with color of the marker as green
fig.add_trace(go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
# Create line plot here
## Here we update these values under function attributes such as title,xaxis_title and yaxis_title
fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
fig.show()""",
    # 3. Bar Chart: flights per destination state
    """# Use plotly express bar chart function px.bar. Provide input data, x and y axis variable, and title of the chart.
# This will give total number of flights to the destination state.
fig = px.bar(bar_data, x="DestState", y="Flights", title='Total number of flights to the destination state split by reporting airline')
fig.show()""",
    # 4. Histogram: distribution of arrival delay
    """## Use plotly express histogram chart function px.histogram.Provide input data x to the histogram
fig = px.histogram(data, x="ArrDelay",title="Total number of flights to the destination state split by reporting air.")
fig.show()""",
    # 5. Bubble Plot: Reporting Airline vs Number of Flights
    """## Bubble chart using px.scatter function with x ,y and size variables defined.Title defined as Reporting Airline vs Number of Flights
fig = px.scatter(bub_data, x="Reporting_Airline", y="Flights", size="Flights",
                 hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
fig.show()""",
    # 6. Pie Chart: distance group proportion by month
    """# Use px.pie function to create the chart. Input dataset.
# Values parameter will set values associated to the sector. 'Month' feature is passed to it.
# labels for the sector are passed to the `names` parameter.
fig = px.pie(data, values='Month', names='DistanceGroup', title='Distance group proportion by month')
fig.show()""",
    # 7. Sunburst: Flight Distribution Hierarchy
    """## Define path as Month and DestStateName and values as Flights.
fig = px.sunburst(data, path=['Month', 'DestStateName'], values='Flights',title='Flight Distribution Hierarchy')
fig.show()""",
]

nb = nbformat.read(NB_IN, as_version=4)
idx = 0
for cell in nb.cells:
    if cell.cell_type == "code" and "## Write your code here" in "".join(cell.source):
        cell.source = solutions[idx]
        idx += 1
print("cells filled:", idx)
assert idx == 7, f"expected 7 blank cells, found {idx}"

client = NotebookClient(nb, timeout=900, kernel_name="python3",
                        resources={"metadata": {"path": "."}})
client.execute()
nbformat.write(nb, NB_OUT)
print("executed and saved:", NB_OUT)

# quick sanity: report any error outputs
errs = 0
for i, cell in enumerate(nb.cells):
    if cell.cell_type == "code":
        for out in cell.get("outputs", []):
            if out.get("output_type") == "error":
                errs += 1
                print("ERROR in cell", i, out.get("ename"), out.get("evalue"))
print("total error outputs:", errs)
