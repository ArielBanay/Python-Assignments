import time
from copy import copy
from Mood import Mood

class Customer():
    def __init__(self,name,mood,personality,initial_patience=100,arrive_time=None):
        self.__name = name
        self.__mood = mood
        self.__personality = personality
        self.__initial_patience = initial_patience
        self.__arrive_time = arrive_time if arrive_time is not None else int(time.time())
        self.__patience = initial_patience

    def get_mood(self):
        return self.__mood

    def get_waiting_time(self,current_time=None):
        if current_time is None:
            current_time=int(time.time())
        dif = current_time-self.__arrive_time
        return dif

    def get_patience(self):
        temp_patience = self.__patience
        return (round(temp_patience, 2))

    def update(self,waiting_time=None):
        if waiting_time is None:
            waiting_time=self.get_waiting_time()
        self.__patience = self.__initial_patience - self.__mood.get_patience_factor(waiting_time)
        self.__mood = self.__personality.adjust_mood(self.get_mood(), waiting_time)

    def __repr__(self):
        lst = ["name: " + str(self.__name),"mood: " + str(self.get_mood()), "personality: " + str(self.__personality), "patience: " + str(self.get_patience())]
        len_max = len(max(lst,key=len))+4
        ret_str = "*"*len_max+"\n"
        for i in lst:
            ret_str = ret_str+"* "+i+" "*(len_max-4-len(i))+" *\n"
        ret_str += "*"*len_max
        return ret_str
