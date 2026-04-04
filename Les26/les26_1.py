import pandas as pd
import matplotlib.pyplot as plt
path = "putty.csv"
data = pd.read_csv(path,skiprows=1,names=["time","distance"])
print(data.distance.describe())
plt.figure(figsize=(10,5))
plt.plot(data['time'],data['distance'])
plt.xlabel('time')
plt.title('distance')
plt.ylabel('distance')
plt.grid(True)
plt.show()