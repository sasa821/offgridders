#%%
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.indexes.base import InvalidIndexError

%pylab inline

# Load data
df = pd.read_csv(
    "/Users/Saeed/Documents/Git/offgridders/simulation_results/results.csv",
    delimiter=",",
)

# Plot PV-Diesel-Storage
df_cs1 = df[df["case"]=="pv-diesel-storage-mg"]
x = df_cs1["genset_cost_opex"]
plt.plot(x, df_cs1["lcoe"])
plt.xlabel("Genset OPEX")
plt.ylabel("LCOE [$/kWh]")
plt.show()
# %%
# Plot PV-Storage
df_cs2 = df[df["case"]=="pv-storage-mg"]
x = df_cs2["genset_cost_opex"]
plt.plot(x, df_cs2["lcoe"])
plt.xlabel("Genset OPEX")
plt.ylabel("LCOE [$/kWh]")
plt.show()

# %%
