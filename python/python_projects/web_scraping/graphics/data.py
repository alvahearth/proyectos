import pandas as pd
import matplotlib.pyplot as plt
import os

data = os.path.dirname(__file__)

filex = os.path.join(data,"graphic_cards.csv")

data_df = pd.read_csv(filex)

affordable = data_df[data_df.Price < 100]

plt.figure(figsize=(15,7))
plt.plot(data_df["Price"],data_df["Name"])
plt.show()


