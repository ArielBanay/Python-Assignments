from Mood import Mood
class Angry(Mood):
    def __init__(self,strength=2):
        super().__init__(strength)

    def get_patience_factor(self,waiting_time):
        fact =round((1.3**(waiting_time/5)) * self._strength, 2)
        return fact

    def __repr__(self):
        return "Angry"