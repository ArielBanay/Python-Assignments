class Task:
    def __init__(self, task_id, description, urgency, importance, time_window, needed_skills):
        #input test
        if type(task_id)!=int:
            raise TypeError(f'{task_id} supposed to be int.')
        elif task_id<0:
            raise ValueError(f'{task_id} supposed to be at least 0.')
        elif type(description)!=str:
            raise TypeError(f'{description}supposed to be str.')
        elif len(description)==0:
            raise ValueError(f'The string must contain at least one character.')
        elif type(urgency)!= int:
            raise TypeError(f'{urgency} supposed to be int.')
        elif urgency<=0:
            raise ValueError(f'{urgency} need to be at lesat 1.')
        elif type(urgency)!= int:
            raise TypeError(f'{importance} supposed to be int.')
        elif urgency<=0:
            raise ValueError(f'{importance} need to be at lesat 1.')
        elif type(time_window)!=tuple:
            raise TypeError(f'{time_window} type is not tuple')
        elif type(time_window[0])!=int or type(time_window[1])!=int:
            raise TypeError(f'{time_window} can contain only int.')
        elif time_window[0]<0 or time_window[1]>23:
            raise ValueError(f'Invalid values fot "time_window" argument.')
        elif time_window[0]>time_window[1]:
            raise ValueError(f'{time_window[0]} supposed to be smaller than {time_window[1]}')
        elif type(needed_skills)!=dict:
            raise TypeError(f'{needed_skills} type is not dict.')
        elif self.__check_dict(needed_skills): # Checks that all dictionary values are correct.
            raise ValueError(f'One of the entries in needed_skills={needed_skills} is incorrect')

        #set fields
        self.__task_id = task_id
        self.description = description
        self.urgency = urgency
        self.importance = importance
        self.time_window = time_window
        self.needed_skills = needed_skills

    def __repr__(self):
        return f"Task ID: {self.get_task_id()}, Description: {self.description}, Urgency: {self.urgency}, Importance: {self.importance}, Time Window: {self.time_window}, Needed skills: {self.needed_skills}"

    def get_task_id(self):
        return self.__task_id

    def __check_dict(self,x):
        if x=={}:
            return True
        for k,v in x.items():
            if type(k)!=str:
                return True
            elif len(k)==0:
                return True
            elif type(v)!=int:
                return True
            elif v<=0:
                return True