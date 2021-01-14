import matplotlib as plt
import pandas as pd
import os
import opendatasets as od

data = os.path.dirname(__file__)
df_folder = os.path.join(data,"csv_files")
df_file = os.path.join(df_folder,"worldometer_data.csv")

covid_df = pd.read_csv(df_file)

print(covid_df)


