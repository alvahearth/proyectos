import os
import pandas as pd

main_file = os.path.dirname(__file__)

data = os.path.join(main_file,"vgsales.csv")

vg_data = pd.read_csv(data)

print(vg_data)