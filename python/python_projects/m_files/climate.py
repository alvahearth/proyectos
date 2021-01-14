import numpy as np

climate_data = np.genfromtxt("climate.txt",delimiter=",",skip_header=1)

weights = np.array([0.3,0.2,0.5])

yields = climate_data @ weights

results = np.concatenate((climate_data,yields.reshape(10000,1)),axis=1)

print(results)

np.savetxt("climate_results.txt",
        results,fmt="%.2f",
        header="temperature,rainfall,humidity,yield_apples",
        comments=""
        )