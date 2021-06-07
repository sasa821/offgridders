#%%
import matplotlib.pyplot as plt
import pandas as pd

%pylab inline

# Load data
df = pd.read_csv("../simulation_results/results.csv",
    delimiter=",",
)
# Plot
df_cs1 = df[df["case"]=="pv-diesel-storage-mg"]
df_cs2 = df[df["case"]=="diesel_mg"]
df_cs3 = df[df["case"]=="pv-storage-mg"]
x = df_cs1["fuel_price"]
plt.plot(x, df_cs1["lcoe"], x, df_cs2["lcoe"], x, df_cs3["lcoe"])
plt.xlabel("Ful Price")
plt.ylabel("LCOE [$/kWh]")
plt.show()

# %%