import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Configuration
API_KEY = "73208658100c701cd8653b478439b31d"  # Replace this with your OpenWeatherMap API key
CITY = "Delhi"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetching Data
response = requests.get(URL)
data = response.json()

# Parsing Data
dates = []
temperatures = []
humidity = []

for forecast in data['list']:
    date = datetime.datetime.fromtimestamp(forecast['dt'])
    temp = forecast['main']['temp']
    hum = forecast['main']['humidity']
    
    dates.append(date)
    temperatures.append(temp)
    humidity.append(hum)

# Plotting with matplotlib and seaborn
sns.set(style="darkgrid")

# Temperature Plot
plt.figure(figsize=(12, 5))
plt.plot(dates, temperatures, marker='o', label="Temperature (°C)", color='orange')
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()

# Humidity Plot
plt.figure(figsize=(12, 5))
plt.plot(dates, humidity, marker='s', label="Humidity (%)", color='blue')
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
