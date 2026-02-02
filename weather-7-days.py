import requests
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
latitude = 59.354310202406474 
longitude = 18.007472168811216
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

#-------------------------------------------
##Process the data into table


# Extract the daily data
daily_data = data['daily']

# Create a DataFrame or in mem table
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)

#----------------------------------------------
#visualize the data


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

#------------------------------------------
#save to csv

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/solna_weather.csv', index=False)
print("Data saved to data/solna_weather.csv")


"""
What you’ve accomplished
Look at what you just did:
Connected to a real API
Worked with dates and time
Processed data with pandas
Created a visualization
Handled files and folders
Saved your results
This is exactly how data analysis works in the real world!
"""