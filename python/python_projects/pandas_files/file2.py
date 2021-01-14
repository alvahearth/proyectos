import pandas as pd

pd1 = pd.DataFrame({
    "city" : ["Chile","Argentina","Brazil","falkland_islands"],
    "population" : [212889367,19152108,45286600,3480],
    "median_age" : [33.5,35.3,31.5,30]
})

pd2 = pd.DataFrame({
    "city" : ["Chile","Argentina","Brazil","falkland_islands"],
    "density(P/KM**2)" : [26,17,25,0],
    "Share_of_world_population_%" : [0.25,0.58,2.73,0.00]
})

pd3 = pd.merge(pd1,pd2,on="city")

print(pd3)