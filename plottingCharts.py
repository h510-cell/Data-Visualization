import csv
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv("gravity.csv")

df.head()

mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

mass.sort()
radius.sort()
gravity.sort()
plt.plot(radius,mass)
#plt.plot(radius,gravity)

plt.title("Radius and Mass of the Stars")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass,gravity)
plt.title("Mass and Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()