#SBATCH --job-name=habit-tracker-hpc
#SBATCH --time=00:30:00
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=128M        # 128 MB memory per CPU
#SBATCH --output=habit_output.txt
#SBATCH --error=habit_error.txt

module purge
module load StdEnv/2023
module load python/3.11.5

if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi

source myenv/bin/activate

pip install --upgrade pip
pip install asteval

python /home/damindra96/project-hpc-dgalbokkah.py
