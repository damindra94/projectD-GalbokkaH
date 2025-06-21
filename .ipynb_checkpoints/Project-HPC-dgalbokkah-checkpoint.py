# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Insert your weekly report function
# Ensure the function takes 3 pieces of input - the task dictionary,
# habit dictionary, and file name to read the data.

def report_week(habits,tasks,file_name):
    print(f"\n======Weekly Report for {file_name}======\n")
    #reporting habits
    if not habits:
        print("No habits tracked this week!")
    else:
        print("Habit Completed: ")
        for habit,days_dict in habits.items():
            completed_days=sum(1 for day, done in days_dict.items() if done)
            print(f"-{habit}:{completed_days}/7 days")
    #reporting tasks
    if not tasks:
        print("No Tasks tracked this week!")
    else:
        print("\nTask Completed:")
        for day, day_tasks in tasks.items():
            for task in day_tasks:
                if not isinstance(task,dict):
                    continue
                status="✅" if task.get('completed') else "❌"
                name=task.get('task_name','no name task')
                print(f"-{name} ({day}):{status}")



# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.
file_list = [
    "dictionaries_1.txt",
    "dictionaries_2.txt",
    "dictionaries_3.txt",
    "dictionaries_4.txt",
    "dictionaries_5.txt",
    "dictionaries_6.txt",
    "dictionaries_7.txt",
    "dictionaries_8.txt",
    "dictionaries_9.txt",
    "dictionaries_10.txt"
    
] 

# This section will loop through the files in the list above, and 
# run the report_week() function for each file. 

# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the report_week() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        report_week(data[0], data[1], file_name)