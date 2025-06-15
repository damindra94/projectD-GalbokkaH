#!/bin/bash
#SBATCH --job-name=habit-tracker-hpc
#SBATCH --time=00:05:00
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=128M
#SBATCH --output=/home/damindra96/logs/habit_output.txt
#SBATCH --error=/home/damindra96/logs/habit_error.txt

# Ensure the output directory exists
mkdir -p /home/damindra96/logs/

# Load necessary modules
module purge
module load StdEnv/2023
module load python/3.12.7

# Print the current working directory
echo "Current working directory: $(pwd)"

# Set up virtual environment if it doesn't exist
if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi

# Activate the virtual environment
source myenv/bin/activate

# Install required packages
pip install --upgrade pip
pip install asteval

# Run the Python script
python /home/damindra96/Project-HPC-dgalbokkah.py

# Deactivate the virtual environment
deactivate
