from Task import Task
from id_generator import id_generator
gen_task_ids = id_generator(7)
# Example 1: Create a simple task
print("Creating a simple task:")
task1 = Task(
    task_id= next(gen_task_ids),
    description="Complete project proposal",
    urgency=5,
    importance=8,
    time_window=(9, 12),  # 9 AM to 12 PM
    needed_skills={"fixing laptop": 2, "fixing internet": 5}
)
print(task1)
print()

# Example 2: Create another task with different parameters
print("Creating another task:")
task2 = Task(
    task_id= next(gen_task_ids),
    description="Prepare for team meeting",
    urgency=7,
    importance=6,
    time_window=(14, 15),  # 2 PM to 3 PM
    needed_skills={"presentation software": 3, "meeting room": 5}
)
print(task2)
print()

# Example 3: Create a list of tasks and display them
print("Creating multiple tasks:")
tasks = (
    Task(
        task_id=next(gen_task_ids),
        description="Write report summary",
        urgency=4,
        importance=9,
        time_window=(10, 11),
        needed_skills={"word processor": 1, "video production":12}
    ),
    Task(
        task_id=next(gen_task_ids),
        description="Respond to emails",
        urgency=6,
        importance=5,
        time_window=(11, 12),
        needed_skills={"client response": 5}
    ),
    Task(
        task_id= next(gen_task_ids),
        description="Plan team lunch",
        urgency=3,
        importance=4,
        time_window=(12, 13),
        needed_skills={"advanced calendar app": 2}
    )
)

for task in tasks:
    print(task)
print()

# Example 4: Handling invalid task inputs
print("Testing invalid task creation:")
try:
    invalid_task = Task(
        task_id= next(gen_task_ids),
        description="",
        urgency=0,
        importance=-1,
        time_window=(10, 9),  # Invalid time window
        needed_skills="not a dict"  # Invalid resources type
    )
except ValueError as e:
    print(f"Error creating task: {e}")
print()

# Example 5: Access and modify task attributes
print("Accessing and modifying task attributes:")
print("Before modification:", task1)
task1.description = "Complete updated project proposal"
task1.urgency = 10
print("After modification:", task1)

print("Checking generator:")
for i in gen_task_ids:
    print(i)
