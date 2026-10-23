# -*- coding: utf-8 -*-
"""Verify all Dash lab apps: layout serves, callbacks produce figures; export sample figures."""
import importlib.util, os, sys
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Patch read_csv so the airline URL loads the local copy (scripts keep the official URL)
LOCAL_CSV = os.path.abspath("airline_data.csv")
_orig_read_csv = pd.read_csv
def _patched(url, *a, **k):
    if isinstance(url, str) and "airline_data" in url:
        return _orig_read_csv(LOCAL_CSV, *a, **k)
    return _orig_read_csv(url, *a, **k)
pd.read_csv = _patched

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m

results = {}

# --- Lab 02 ---
m = load("dash_basics.py", "lab02")
c = m.app.server.test_client()
html_text = c.get("/").get_data(as_text=True)
results["dash_basics.py"] = ("Airline Dashboard" in html_text) and c.get("/").status_code == 200

m = load("dash_basics_practice.py", "lab02p")
html_text = m.app.server.test_client().get("/").get_data(as_text=True)
results["dash_basics_practice.py"] = ("Airline On-time Performance Dashboard" in html_text)

# export lab02 pie figure
fig = m.__dict__.get("fig")
# note: fig belongs to the last loaded module that defines it (practice); re-export from basics instead
m2 = sys.modules["lab02"]
m2.fig.write_image("lab02_dash_basics_pie.png", width=1100, height=700)
print("saved lab02_dash_basics_pie.png")

# --- Lab 03 ---
m = load("dash_interactivity.py", "lab03")
c = m.app.server.test_client()
results["dash_interactivity.py GET /"] = c.get("/").status_code == 200
fig = m.get_graph("2010")
assert len(fig.data) > 0, "lab03 callback empty"
fig.write_image("lab03_line_plot_2010.png", width=1100, height=600)
print("saved lab03_line_plot_2010.png")
results["dash_interactivity.py callback"] = True

m = load("dash_interactivity_barplot.py", "lab03b")
c = m.app.server.test_client()
results["dash_interactivity_barplot.py GET /"] = c.get("/").status_code == 200
fig = m.get_graph("2010")
assert len(fig.data) > 0, "lab03 bar callback empty"
fig.write_image("lab03_bar_plot_2010.png", width=1100, height=600)
print("saved lab03_bar_plot_2010.png")
results["dash_interactivity_barplot.py callback"] = True

# --- Lab 04 ---
m = load("flight_delay.py", "lab04")
c = m.app.server.test_client()
results["flight_delay.py GET /"] = c.get("/").status_code == 200
figs = m.get_graph("2010")
assert len(figs) == 5 and all(len(f.data) > 0 for f in figs), "lab04 callback incomplete"
figs[0].write_image("lab04_carrier_plot_2010.png", width=1000, height=550)
figs[4].write_image("lab04_late_plot_2010.png", width=1000, height=550)
print("saved lab04_carrier_plot_2010.png, lab04_late_plot_2010.png")
results["flight_delay.py callback"] = True

m = load("flight_details.py", "lab04p")
c = m.app.server.test_client()
html_text = c.get("/").get_data(as_text=True)
results["flight_details.py"] = ("Flight Details Statistics Dashboard" in html_text)

print("\n=== RESULTS ===")
for k, v in results.items():
    print(("PASS " if v else "FAIL ") + k)
if not all(results.values()):
    sys.exit(1)
print("ALL OK")
