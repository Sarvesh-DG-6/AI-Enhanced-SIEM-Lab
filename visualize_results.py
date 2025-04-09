import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/anomaly_output.csv")
sns.pairplot(df, hue="anomaly")
plt.show()
