import os
import subprocess
from datetime import datetime, timedelta

# Change this to set how many days back you want to start committing
start_date = datetime(2023, 1, 1)  # YYYY, MM, DD

# Number of days to create commits
days = 365  # A full year

for day in range(days):
    date = start_date + timedelta(days=day)
    formatted_date = date.strftime("%Y-%m-%dT12:00:00")  # Noon UTC time

    with open("commit.txt", "w") as file:
        file.write(f"Commit for {formatted_date}")

    subprocess.run(["git", "add", "commit.txt"])
    subprocess.run(["git", "commit", "--date", formatted_date, "-m", f"Commit on {formatted_date}"])

print("Commits created! Now push them to GitHub.")
