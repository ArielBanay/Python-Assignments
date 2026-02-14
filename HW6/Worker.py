
class Worker:
    def __init__(self, worker_id, name, skills, availability, salary):
        #input tests
        if type(worker_id)!=int:
            raise TypeError(f'{worker_id} supposed to be int.')
        elif worker_id<0:
            raise ValueError(f'{worker_id} cannot be smaller than 0 ')
        elif type(name)!=str:
            raise TypeError(f'{name} type is not str.')
        elif len(name)==0:
            raise ValueError('the name must contain at least 1 char.')
        elif type(skills)!= dict:
            raise TypeError(f'{skills} type is not dict.')
        elif self.__check_skills(skills):
            raise ValueError(f'One or more of the keys and values in the dictionary are invalid.')
        elif type(availability)!=list:
            raise TypeError(f'availability type is not list')
        elif self.__check_type(availability):
            raise TypeError('One of the element in the list is not tuple or the tuple may contain not int.')
        elif self.__check_val(availability):
            raise ValueError('There is an invalid value in the array.')
        elif not isinstance(salary, (int, float)):
            raise TypeError(f'{salary} type is not float.')
        elif salary<0:
            raise ValueError(f'{salary}<=0.')

        # set fields
        self.__worker_id = worker_id
        self.name = name
        self.__skills = skills
        self.__availability = availability
        self.__salary = salary

    def __repr__(self):
        return f"Worker ID: {self.get_worker_id()}, Name: {self.name}, Skills: {self.get_skills()}, Availability: {self.get_availability()}, Salary:{self.get_salary()}"
    
    def update_salary(self, additional_salary):
        if not isinstance(additional_salary, (int, float)):
            raise TypeError(f'{additional_salary} is not int or float.')
        elif additional_salary<0:
            raise ValueError(f'{additional_salary}<0.')
        self.__salary = self.get_salary()+additional_salary

    def update_skills(self, new_skills):
        if not isinstance(new_skills,list):
            raise TypeError('new_skills is not list.')
        for i in new_skills:
            if not isinstance(i,str):
                raise TypeError(f'{i} is not str.')
            elif not len(i):
                raise ValueError(f'There is an empty string in new_skills.')
        for i in new_skills:
            self.get_skills()[i]=self.get_skills().get(i,0)+1

    def update_availability(self, new_availability):
        # input tests
        if type(new_availability)!=tuple:
            raise TypeError(f'new_availability argument type is not tuple.')
        elif type(new_availability[0])!=int or type(new_availability[1])!=int:
            raise TypeError(f'new_availability not contains only ints.')
        elif new_availability[0]<0 or new_availability[1]>23:
            raise ValueError('new_availability contains number out of range 0-23.')
        elif new_availability[0]>new_availability[1]:
            raise ValueError('new_availability[0] greater than new_availability[1].')

        # real func
        if not self.get_availability():
            self.get_availability().append(new_availability)
            return
        for f,l in self.get_availability(): #f-first l-last
            if l < new_availability[0] or f > new_availability[1]:
                self.get_availability().append(new_availability)
                return
            elif f<new_availability[0] and new_availability[1]<l:
                return
            elif f<=new_availability[0]<=l:
                tup = (min(f,new_availability[0],l),max(l,new_availability[1]))
                self.get_availability().append(tup)
                return
            elif f<=new_availability[1]<=l:
                tup = (min(f, new_availability[0]),max(f, new_availability[1],l))
                self.get_availability().append(tup)
                return

    def get_availability(self):
        return self.__availability
    
    def get_skills(self):
        return self.__skills

    def get_salary(self):
        return self.__salary
    
    def get_worker_id(self):
        return self.__worker_id

    #auxiliary functions
    def __check_skills(self,x):
        if x=={}:
            return True
        for k,v in x.items():
            if type(k)!=str:
                return True
            elif type(v)!=int or v<=0:
                return True

    def __check_type(self,x):
        for i in x:
            if type(i)!=tuple:
                return True
            elif type(i[0]) != int or type(i[1]) != int:
                return True

    def __check_val(self,x):
        for i in x:
            if i[0]<0 or i[1]>23:
                return True
            elif i[0] > i[1]:
                return True