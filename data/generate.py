import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of rows in the dataset
n_samples = 1000

# Generate synthetic data
data = {
    "Machine_ID": range(1, n_samples + 1),
    "Temperature": np.random.randint(50, 120, n_samples),  # Temperature in range 50-120°C
    "Run_Time": np.random.randint(30, 300, n_samples),      # Run time in range 30-300 minutes
}

# Downtime_Flag based on conditions
data["Downtime_Flag"] = [
    1 if (temp > 90 and runtime > 200) else 0
    for temp, runtime in zip(data["Temperature"], data["Run_Time"])
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/sample_data.csv", index=False)

print("Synthetic dataset created and saved as 'sample_data.csv'.")
