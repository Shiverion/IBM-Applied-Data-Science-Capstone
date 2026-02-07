
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create images directory
if not os.path.exists('images'):
    os.makedirs('images')

# Load Dataset
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"
df = pd.read_csv(url)

# Set style
sns.set_theme(style="whitegrid")

# 1. Flight Number vs. Launch Site
plt.figure(figsize=(12, 6))
sns.catplot(y="LaunchSite", x="FlightNumber", hue="Class", data=df, aspect=2.5)
plt.title("Flight Number vs. Launch Site", fontsize=20)
plt.xlabel("Flight Number", fontsize=20)
plt.ylabel("Launch Site", fontsize=20)
plt.savefig('images/FlightNumber_vs_LaunchSite.png', bbox_inches='tight')
plt.close()

# 2. Payload Mass vs. Launch Site
plt.figure(figsize=(12, 6))
sns.catplot(y="LaunchSite", x="PayloadMass", hue="Class", data=df, aspect=2.5)
plt.title("Payload Mass vs. Launch Site", fontsize=20)
plt.xlabel("Payload Mass (kg)", fontsize=20)
plt.ylabel("Launch Site", fontsize=20)
plt.savefig('images/PayloadMass_vs_LaunchSite.png', bbox_inches='tight')
plt.close()

# 3. Success Rate vs. Orbit Type
plt.figure(figsize=(12, 6))
orbit_success = df.groupby('Orbit')['Class'].mean().reset_index()
sns.barplot(x="Orbit", y="Class", data=orbit_success, hue='Orbit', palette='viridis', legend=False)
plt.title("Success Rate by Orbit Type", fontsize=20)
plt.xlabel("Orbit Type", fontsize=20)
plt.ylabel("Success Rate", fontsize=20)
plt.savefig('images/SuccessRate_vs_Orbit.png', bbox_inches='tight')
plt.close()

# 4. Flight Number vs. Orbit Type
plt.figure(figsize=(12, 6))
sns.catplot(y="Orbit", x="FlightNumber", hue="Class", data=df, aspect=2.5)
plt.title("Flight Number vs. Orbit Type", fontsize=20)
plt.xlabel("Flight Number", fontsize=20)
plt.ylabel("Orbit Type", fontsize=20)
plt.savefig('images/FlightNumber_vs_Orbit.png', bbox_inches='tight')
plt.close()

# 5. Payload vs. Orbit Type
plt.figure(figsize=(12, 6))
sns.catplot(y="Orbit", x="PayloadMass", hue="Class", data=df, aspect=2.5)
plt.title("Payload Mass vs. Orbit Type", fontsize=20)
plt.xlabel("Payload Mass (kg)", fontsize=20)
plt.ylabel("Orbit Type", fontsize=20)
plt.savefig('images/PayloadMass_vs_Orbit.png', bbox_inches='tight')
plt.close()

# 6. Launch Success Yearly Trend
# Extract year
def Extract_year(date):
    return date.split("-")[0]

df['Year'] = df['Date'].apply(Extract_year)
yearly_success = df.groupby('Year')['Class'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x="Year", y="Class", data=yearly_success)
plt.title("Yearly Launch Success Rate", fontsize=20)
plt.xlabel("Year", fontsize=20)
plt.ylabel("Success Rate", fontsize=20)
plt.savefig('images/LaunchSuccess_YearlyTrend.png', bbox_inches='tight')
plt.close()

print("All plots generated and saved to 'images/' directory.")
