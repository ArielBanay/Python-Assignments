from Task import Task
from TaskScheduler import TaskScheduler
from Worker import Worker
from id_generator import id_generator

scheduler = TaskScheduler()
auto_worker_id_gen = id_generator(12)
auto_task_id_gen = id_generator(20)
# Add tasks
print("Adding tasks to the scheduler:")
task0 = Task(
    task_id=next(auto_task_id_gen),
    description="Task 0: Analyze data",
    urgency=5,
    importance=8,
    time_window=(9, 12),
    needed_skills={"Python": 3, "Data Analysis": 2}
)
task1 = Task(
    task_id=next(auto_task_id_gen),
    description="Task 1: Prepare report",
    urgency=2,
    importance=6,
    time_window=(18, 22),
    needed_skills={"Word Processing": 2}
)
task2 = Task(
    task_id=next(auto_task_id_gen),
    description="Task 2: Team presentation",
    urgency=4,
    importance=7,
    time_window=(10, 11),
    needed_skills={"Presentation Software": 1}
)
task3 = Task(
    task_id=next(auto_task_id_gen),
    description="Task 3: Analyze data",
    urgency=4,
    importance=7,
    time_window=(9, 12),
    needed_skills={"Presentation Software": 3, "Data Analysis": 2}
)

task4 = Task(
    task_id=next(auto_task_id_gen),
    description="Task 4: Analyze data",
    urgency=4,
    importance=8,
    time_window=(18, 20),
    needed_skills={"Java": 5, "Data Analysis v.2": 2}
)
scheduler.add_task(task0)
scheduler.add_task(task1)
scheduler.add_task(task2)
scheduler.add_task(task3)
scheduler.add_task(task4)

print(scheduler.get_tasks())

# Add workers
print("Adding workers to the scheduler:")
worker1 = Worker(
    worker_id=next(auto_worker_id_gen),
    name="Alice",
    skills={"Python": 5, "Data Analysis": 5, "Word Processing": 3},
    availability=[(9, 12), (14, 18)],
    salary=2000
)
worker2 = Worker(
    worker_id=next(auto_worker_id_gen),
    name="Bob",
    skills={"Presentation Software": 2, "Word Processing": 2},
    availability=[(10, 12), (14, 16)],
    salary=20000
)
worker3 = Worker(
    worker_id=next(auto_worker_id_gen),
    name="Jennifer",
    skills={'Data Analysis v.2': 2, "Java": 7},
    availability=[(6, 12), (14, 18)],
    salary=25000
)
scheduler.add_worker(worker1)
scheduler.add_worker(worker2)
scheduler.add_worker(worker3)
worker_gen = scheduler.workers_gen()
for worker in worker_gen:
    print(worker)

# Allocate tasks
print("Allocating tasks to workers:")
scheduler.allocate_task()
scheduler.allocate_task()
scheduler.allocate_task()
print(f"Completed tasks: {[task.description for task in scheduler.completed_tasks_gen()]}")
print()

# Update a task
print("Updating a task...")
try:
    scheduler.update_task(task1.get_task_id(), urgency=10)
    print("Updating ended successfully.")
except Exception as e:
    print(e)
    print(f"Updated Task: {task1}")
    print()

# Generate completed tasks
print("Iterating through completed tasks:")
for completed_task in scheduler.completed_tasks_gen():
    print(completed_task)

print("Iterating through completed tasks post undo task:")
scheduler.undo_task()
for completed_task in scheduler.completed_tasks_gen():
    print(completed_task)

print("Undo another task")
scheduler.undo_task()
for completed_task in scheduler.completed_tasks_gen():
    print(completed_task)

print("Promoting senior....")
scheduler.promote_senior()
worker_gen = scheduler.workers_gen()
for worker in worker_gen:
    print(worker)

print("Yearly updating all workers....")
scheduler.yearly_update()
worker_gen = scheduler.workers_gen()
for worker in worker_gen:
    print(worker)

print(scheduler.peek_task())