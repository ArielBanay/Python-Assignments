from abc import ABC,abstractmethod

class Mood(ABC):
    def __init__(self,strength=2):
        self._strength=strength

    @abstractmethod
    def get_patience_factor(self, waiting_time):
        pass

    @abstractmethod
    def __repr__(self):
        pass