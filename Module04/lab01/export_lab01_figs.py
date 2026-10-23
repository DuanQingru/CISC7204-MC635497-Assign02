# -*- coding: utf-8 -*-
"""Re-render the 7 exercise figures of the completed Lab01 notebook as PNGs for visual check."""
import nbformat

nb = nbformat.read("CISC3015_Assgn02_Module_04_Lab01_Plotly_Basics_COMPLETED.ipynb", as_version=4)

names = ["1_scatter", "2_line", "3_bar", "4_histogram", "5_bubble", "6_pie", "7_sunburst"]
render_cells = []
for cell in nb.cells:
    src = "".join(cell.source)
    if cell.cell_type == "code" and any(k in src for k in
        ["Distance vs Departure Time", "Month vs Average Flight Delay Time",
         "Total number of flights to the destination state split",
         'x="ArrDelay"', "Reporting Airline vs Number of Flights",
         "Distance group proportion by month", "Flight Distribution Hierarchy"]):
        if "fig.show()" in src:
            render_cells.append(src)

print("render cells:", len(render_cells))

ns = {}
preamble = '''
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                           encoding="ISO-8859-1",
                           dtype={"Div1Airport": str, "Div1TailNum": str,
                                  "Div2Airport": str, "Div2TailNum": str})
data = airline_data.sample(n=500, random_state=42)
line_data = data.groupby("Month")["ArrDelay"].mean().reset_index()
bar_data = data.groupby(["DestState"])["Flights"].sum().reset_index()
data["ArrDelay"] = data["ArrDelay"].fillna(0)
bub_data = data.groupby("Reporting_Airline")["Flights"].sum().reset_index()
'''
exec(compile(preamble, "<pre>", "exec"), ns)
for name, src in zip(names, render_cells):
    exec(compile(src, "<cell>", "exec"), ns)
    ns["fig"].write_image(f"lab01_fig_{name}.png", width=1000, height=600, scale=1)
    print("saved", name)
