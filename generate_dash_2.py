
import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import BytesIO
import os

# Create images directory if not exists
if not os.path.exists('images'):
    os.makedirs('images')

# Download Dataset
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
response = requests.get(url)
df = pd.read_csv(BytesIO(response.content))

# Task 2: Pie Chart for specific site (KSC LC-39A has high success)
site = 'KSC LC-39A'
filtered_df = df[df['Launch Site'] == site]
counts = filtered_df['class'].value_counts()

# Plot
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=['Success', 'Failure'] if counts.index[0]==1 else ['Failure', 'Success'], 
        autopct='%1.1f%%', colors=['green', 'red'], startangle=90)
plt.title(f'Total Success Launches for site {site}', fontsize=20)
plt.savefig('images/plotlydash_2.png', bbox_inches='tight')
plt.close()

print("Generated images/plotlydash_2.png")
