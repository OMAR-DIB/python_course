import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DailyDelhiClimateTrain.csv')

print(df.head(5))

print(df.describe())

windSpeed = df['wind_speed']
plt.hist(windSpeed,20)
plt.show()

df.plot(kind = 'scatter', x = 'wind_speed', y= 'humidity')
plt.show()
date = df['date']
date=pd.to_datetime(date)

meantemp = df['meantemp']
hum = df['humidity']
speed = df['wind_speed']

plt.plot(date,meantemp)
plt.xlabel("year")
plt.ylabel("meanTemp")
plt.show()

plt.plot(date,hum)
plt.xlabel("year")
plt.ylabel("humidity")
plt.show()

plt.plot(date,speed)
plt.xlabel("year")
plt.ylabel("wind_speed")
plt.show()

#10) yes there are a good correlation

df.plot(kind = 'scatter', x = 'humidity', y= 'meantemp')
plt.show()
