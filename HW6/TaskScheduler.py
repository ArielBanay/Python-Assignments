import copy
from ADTs import Stack, MyQueue
from Task import Task
from Worker import Worker


class TaskScheduler:
    def __init__(self):
        self.__tasks = Stack()
        self.__workers = MyQueue()
        self.__completed_tasks = Stack()

    def add_task(self, task):
        if not isinstance(task,Task):
            raise TypeError(f"The given task isn't instance of 'Task'.")

        if self.__tasks.is_empty():
            self.__tasks.push(task)
            return
        temp_stack = Stack()
        try:
            a = self.__tasks.pop()
            while a.urgency > task.urgency:
                temp_stack.push(a)
                a = self.__tasks.pop()
            while a.urgency == task.urgency and a.importance > task.importance:
                temp_stack.push(a)
                a = self.__tasks.pop()
            while a.urgency == task.urgency and a.importance == task.importance and  a.time_window[0]<task.time_window[0]:
                temp_stack.push(a)
                a = self.__tasks.pop()
            while a.urgency == task.urgency and a.importance == task.importance and a.time_window[0]==task.time_window[0] and a.time_window[1]<task.time_window[1]:
                temp_stack.push(a)
                a = self.__tasks.pop()
            self.__tasks.push(a)
            self.__tasks.push(task)
        except IndexError:
            self.__tasks.push(task)
        finally:
            while not temp_stack.is_empty():
                self.__tasks.push(temp_stack.pop())

    def completed_tasks_gen(self):
        demo_ct = copy.deepcopy(self.__completed_tasks)
        for _ in range(len(demo_ct)):
            yield demo_ct.pop()

    def workers_gen(self):
        demo_w = copy.deepcopy(self.__workers)
        for _ in range(len(demo_w)):
            yield demo_w.dequeue()

    def add_worker(self, worker):
        if not isinstance(worker,Worker):
            raise TypeError(f'The argument should be a Workers type.')

        self.__workers.enqueue(worker)

    def allocate_task(self):
        if self.__tasks.is_empty(): #There is no task to do.
            return
        mtd = self.__tasks.pop() #mission to do
        if self.__workers.is_empty(): #There is no workers to do that task.
            self.add_task(mtd)
            return
        w_gen = self.workers_gen()
        have_time = False
        for w in w_gen:
            idx = 0
            for s,y in mtd.needed_skills.items(): #checking about the skills
                if w.get_skills().get(s,0)>=y:
                    idx += 1
                    continue
                else:
                    break
            for t in w.get_availability():
                if t[0]<=mtd.time_window[0] and mtd.time_window[1]<=t[1]:
                    have_time = True
                    break
            if idx==len(mtd.needed_skills) and have_time:
                self.__completed_tasks.push(mtd)
                return
        #There is no worker with the needed skills.
        self.add_task(mtd)

    def update_task(self, task_id, **kwargs):
        # input test
        if type(task_id) != int:
            raise TypeError(f'{task_id} supposed to be int.')
        elif task_id < 0:
            raise ValueError(f'{task_id} supposed to be at least 0.')
        elif self.__check_ti(task_id):
            raise ValueError('There is no task with this ID number.')
        if kwargs=={}:
            return
        t_i = self.peek_task()
        for i in kwargs.keys():
            if not hasattr(t_i, i):
                raise ValueError(f"task instance doesn't have attribute '{i}'")

        temp_stack = Stack()
        for i in range(len(self.__tasks)):
            t = self.__tasks.pop()
            if t.get_task_id()!=task_id:
                temp_stack.push(t)
            elif t.get_task_id()==task_id:
                for k,v in kwargs.items():
                    setattr(t,k,v)
                self.add_task(t)
                break
        while not temp_stack.is_empty():
            self.add_task(temp_stack.pop())

    def undo_task(self):
        try:
            undo = self.__completed_tasks.pop()
            self.add_task(undo)
        except IndexError:
            print('No tasks to undo.')

    def promote_senior(self):
        try:
            w = self.__workers.dequeue()
            w.update_salary(1000)
            self.__workers.enqueue(w)
        except RuntimeError:
            print('There is no worker to promote.')

    def yearly_update(self):
        for i in range(len(self.__workers)):
            w = self.__workers.dequeue()
            for k,v in w.get_skills().items():
                w.get_skills()[k]=v+1
            self.__workers.enqueue(w)

    def peek_task(self):
        try:
            return self.__tasks.peek()
        except IndexError:
            print('No tasks in waiting tasks.')

    def get_tasks(self):
        return self.__tasks

    def __check_ti(self,x):
        if self.__tasks.is_empty():
            return True

        demo = copy.deepcopy(self.__tasks)
        t = demo.pop()
        while t.get_task_id()!=x:
            try:
                t = demo.pop()
            except IndexError:
                return True
        return False