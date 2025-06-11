# Acenet Final project
# Weekly Task and Habit Tracker
This project is a built in Python command tool that allows the user to add, track and view their daily/weekly tasks and habits.
It includes functions for adding, removing, tracking and viewing tasks and habits on all days of the week.
# Features
- Add new tasks and habits for specific days of the week
- Mark tasks and habits as completed even once overdue
- Remove tasks or habits when no longer needed
- Create and update weekly habits
- Generate daily and weekly summary reports for both habits and tasks
- Supports batch processing for High Performance Computing (HPC)


  ## Instructions of how to use:
  ## For local use (Jupyter notebook or terminal)
  1. Clone the repo:
     
     ``bash
     git clone https://github.com/damindra94/projectD-GalbokkaH.git
     cd projectD-GalbokkaH
     
  2.Open the Jupyter notebook:
  
    * Launch Jupyter
    * Run the D.GalbokkaHewageProjectFinal.ipynb
    * Follow the prompts to add or update your tasks and habits
 
  3.Functions/Features you can access

    * **add_task()** to add a task to a specific day
    * **enter_habit(habits_week)** to add and track a habit
    * **update_task()** to mark a task as completed
    * **mark_habits** to mark a habit as completed
    * **remove_task()** to delete a task
    * **remove_habits()** to delete a habit from the tracker
    * **weekly_report(habits_week)** to display the weekly habit report
    * **task_weekly_report(days_keys)** to display the weekly task report
    * **daily_report(days_keys, habits_week)** to display all incomplete and completed tasks and habits
    * **main_menu** to provide the user the possibilty to toggle through the options
 
    * 
  ## For HPC use (Cluster Execution)
  1.Upload the folowwing to the HPC CLuster
   * Project-HPC-DGalbokkaH.py
   * Your .csv or .txt data files
   * damindra_job_script (job submission script)
  
  2. Log into the cluster and submit the job:
  3. Monitor the job
     










    
     
